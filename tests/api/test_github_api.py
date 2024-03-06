import pytest
from modules.api.clients.github import GitHub


# test_1 verifies that user naftysa exists in GitHub
@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('naftysa')
    assert user['login'] == 'naftysa'


# test_2 verifies that mentioned user does not exists in GitHub
@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user('nataliia_ketova')
    assert r['message'] == 'Not Found'

# test_3 
@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('CourseProject23NataKetova')
    assert 'CourseProject23NataKetova' in r['items'][0]['name']

# test_4
@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('nataliia_ketova_repo_non_exist')
    assert r['total_count'] == 0

# test_5
@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0

# test_6
@pytest.mark.api
def test_emoji_climbing_can_be_found(github_api):
    emojiname = 'climbing' #move this to fixture
    r = github_api.get_emojis()
    assert emojiname in r

# test_7
@pytest.mark.api
def test_emoji_ukraine_can_be_found(github_api):
    emojiname = 'fire' #move this to fixture
    r = github_api.get_emojis()
    assert emojiname in r
    