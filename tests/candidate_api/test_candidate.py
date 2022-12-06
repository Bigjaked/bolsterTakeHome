import requests

host = "http://localhost:8081"


def endpoint(*args) -> str:
    return f"{host}/{'/'.join(args)}"


class TestCandidate:
    def test_list_candidate(self):
        resp = requests.get(endpoint("candidates"))
        assert resp.json() == {
            "results": [
                {
                    "id": "cindyhall",
                    "bio": "I have over 20 years of experience running People/HR teams and creating company cultures. I believe that great cultures drive great businesses. I love to help companies leverage their values to create and maintain great cultures to drive their business.",
                    "name": "Cindy Hall",
                    "picture": "https://ti.bolster.com/a/5ffe2989cbf0a1006f2593de/1611263724",
                },
                {
                    "id": "samnewton",
                    "bio": "Technical leader and problem solver with over 25-years of experience developing software and leading high-performing teams.",
                    "name": "Sam Newton",
                    "picture": "https://ti.bolster.com/a/630e328375b819c626b18685/1665609168",
                },
                {
                    "id": "noahbraxton",
                    "bio": "Experienced B2B Marketing Leader. Passionate about technology, collaboration, leadership and learning.",
                    "name": "Noah Braxton",
                    "picture": "https://ti.bolster.com/a/630e328375b819c626b18685/1665609168",
                },
                {
                    "id": "michaelboyd",
                    "bio": "Founder/CEO with 25+ years of experience",
                    "name": "Michael Boyd",
                    "picture": "https://ti.bolster.com/a/630e328375b819c626b18685/1665609168",
                },
                {
                    "id": "dandutch",
                    "bio": "25 years of experience working on security/privacy issues, DATA governance issues, and protecting and improving DATA through industry policy, regulatory policy relations, and technical solutions.",
                    "name": "Dan Dutch",
                    "picture": "https://ti.bolster.com/a/630e328375b819c626b18685/1665609168",
                },
            ]
        }
