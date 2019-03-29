#!/usr/bin/env python
import travis_generator


class Travis(travis_generator.Travis):
    notifications = {"email": False}
    install = "curl -fLs https://git.io/fpfTa | bash -s"
    after_failure = ["wget https://raw.githubusercontent.com/DiscordHooks/travis-ci-discord-webhook/master/send.sh",
                     "chmod +x send.sh",
                     "./send.sh failure $WEBHOOK_URL"
                     ]

    def python(self):
        return [travis_generator.quote("3.6")]

    @property
    def script(self):
        return True


if __name__ == "__main__":
    print(Travis())
