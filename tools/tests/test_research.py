import pytest

from tools import yt_research


@pytest.mark.parametrize(
    "text, expected",
    [
        ("1.2M views", 1_200_000),
        ("12K views", 12_000),
        ("1,234,567 views", 1_234_567),
        ("987 views", 987),
        ("No views", 0),
        (4321, 4321),
        ("2.5B views", 2_500_000_000),
        (None, None),
        ("members only", None),
    ],
)
def test_parse_views(text, expected):
    assert yt_research.parse_views(text) == expected


def test_outlier_scores_sorted_and_relative_to_baseline():
    videos = [
        {"videoId": "a", "viewCountText": "10K views"},
        {"videoId": "b", "viewCountText": "1M views"},
        {"videoId": "c", "viewCountText": None},
    ]
    ranked = yt_research.outlier_scores(videos, baseline=10_000)
    assert [v["videoId"] for v in ranked] == ["b", "a"]
    assert ranked[0]["outlier"] == 100.0
    assert ranked[1]["outlier"] == 1.0


def test_missing_key_gives_vietnamese_hint(monkeypatch, tmp_path):
    monkeypatch.delenv("TRANSCRIPT_API_KEY", raising=False)
    monkeypatch.setattr(yt_research.config, "CACHE_DIR", tmp_path)
    with pytest.raises(yt_research.ApiError, match="TRANSCRIPT_API_KEY"):
        yt_research.profile("@nobody")
