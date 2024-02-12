# bff_api_gateway_example

## Description

BFF と API ゲートウェイの連携部分のサンプル

## Install

```bash
pip install -r requirements.txt
```

## Command

```bash
curl -X POST -H "Content-Type: application/json" -d '{"username": "user1", "password": "password1"}' http://localhost:2000/bff/login
# {
#   "token": "a7342ad288b0e571cc7d00d32c5a80a2"
# }

curl -X GET -H "Authorization: a7342ad288b0e571cc7d00d32c5a80a2" http://localhost:2000/bff/resource
# {
#   "message": "This is the resource for user1"
# }

curl -X GET -H "Authorization: invalid_token" http://localhost:2000/bff/resource
# {
#   "message": "Invalid token"
# }
```

## Contribution

1. Fork it ( https://github.com/zdogma/bff_api_gateway_example/fork )
2. Create your feature branch (git checkout -b my-new-feature)
3. Commit your changes (git commit -am 'Add some feature')
4. Push to the branch (git push origin my-new-feature)
5. Create new Pull Request

## Author

<div style="display: flex;">
  <img src="https://avatars3.githubusercontent.com/u/1973683?v=3&s=460" width="45px;" height="45px;" style="margin-right: 10px;">
  <a href="https://github.com/zdogma/" style="align-self: center;">zdogma</a>
</div>
