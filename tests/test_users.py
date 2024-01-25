from assertpy import assert_that, soft_assertions


class TestUsers:

    def test_get_list_users(self, client):
        response = client.send_request('GET', '/api/users')
        with soft_assertions():
            assert_that(response.status_code).is_equal_to(200)
            assert_that(response.as_dict).is_not_empty()

    def test_get_user_not_found(self, client):
        response = client.send_request('GET', '/api/users/123')
        with soft_assertions():
            assert_that(response.status_code).is_equal_to(404)
            assert_that(response.as_dict).is_empty()
