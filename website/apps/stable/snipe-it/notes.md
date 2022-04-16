# Initial install

`Snipe-it`'s pre-flight check [can't detect](https://github.com/snipe/snipe-it/issues/10779) if you are running behind a proxy, so for the initial installation it's suggested to go without ingress.

Complete the setup then go back and enable ingress.

Also keep in mind that you should have `172.16.0.0/16` in your `APP_TRUSTED_PROXIES`. If you want to add more trusted proxies. It's a comma separated list and you can do it like that `172.16.0.0/16,192.168.1.0/24`.
