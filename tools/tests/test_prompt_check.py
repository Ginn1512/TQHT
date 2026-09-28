from tools import prompt_check

BLOCK = """# chú thích
Rui
i:straw hat
"""


def board(*prompts):
    return {"scenes": [{"id": f"s{i}", "image_prompt": p} for i, p in enumerate(prompts, 1)]}


def test_names_are_case_sensitive_whole_words():
    pats = prompt_check.load_patterns(BLOCK)
    assert prompt_check.violations(board("ancient ruins", "a spider named Rui"), pats) == [("s2", "image_prompt", "Rui")]


def test_design_terms_ignore_case():
    pats = prompt_check.load_patterns(BLOCK)
    assert prompt_check.violations(board("A Straw Hat on a rock"), pats) == [("s1", "image_prompt", "Straw Hat")]


def test_video_prompt_is_checked_and_clean_board_passes():
    pats = prompt_check.load_patterns(BLOCK)
    b = {"scenes": [{"id": "s1", "image_prompt": "sea", "video_prompt": "straw hat flies"}]}
    assert prompt_check.violations(b, pats) == [("s1", "video_prompt", "straw hat")]
    assert prompt_check.violations(board("a calm sea"), pats) == []
