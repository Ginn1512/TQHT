import pytest

from tools import timing


def test_scene_durations_add_padding():
    assert timing.scene_durations([1.0, 2.5], padding_s=0.4) == [1.4, 2.9]


def test_fit_shorter_speech_is_padded():
    assert timing.fit_to_scene(4.0, 5.0) == timing.Fit(tempo=1.0, pad_s=1.0)


def test_fit_slightly_longer_speech_is_sped_up():
    fit = timing.fit_to_scene(5.5, 5.0, max_tempo=1.2)
    assert fit.tempo == pytest.approx(1.1)
    assert fit.pad_s == 0.0


def test_fit_too_long_needs_shorter_translation():
    with pytest.raises(timing.NeedsShorterTranslation):
        timing.fit_to_scene(6.5, 5.0, max_tempo=1.2)


def test_starts_are_cumulative():
    assert timing.starts([1.5, 2.0, 3.0]) == [0.0, 1.5, 3.5]


@pytest.mark.parametrize(
    "seconds, expected",
    [(0, "00:00:00,000"), (61.5, "00:01:01,500"), (3723.004, "01:02:03,004")],
)
def test_srt_timestamp(seconds, expected):
    assert timing.srt_timestamp(seconds) == expected


def test_chapter_timestamp():
    assert timing.chapter_timestamp(5.9) == "0:05"
    assert timing.chapter_timestamp(754) == "12:34"
    assert timing.chapter_timestamp(3725) == "1:02:05"


def test_split_caption_prefers_sentence_boundaries():
    assert timing.split_caption("Câu một. Câu hai!") == ["Câu một.", "Câu hai!"]


def test_split_caption_wraps_long_sentences_by_word():
    text = " ".join(["từ"] * 60)
    chunks = timing.split_caption(text, max_chars=20)
    assert all(len(c) <= 20 for c in chunks)
    assert " ".join(chunks) == text


def test_split_caption_handles_text_without_spaces():
    chunks = timing.split_caption("這" * 50, max_chars=20)
    assert [len(c) for c in chunks] == [20, 20, 10]


def test_build_srt_spans_speech_of_each_scene():
    srt = timing.build_srt(["Một. Hai.", "Ba."], [0.0, 3.0], [2.0, 1.0])
    blocks = srt.strip().split("\n\n")
    assert len(blocks) == 3
    assert blocks[0].splitlines()[1] == "00:00:00,000 --> 00:00:01,000"
    assert blocks[2].splitlines()[1] == "00:00:03,000 --> 00:00:04,000"
