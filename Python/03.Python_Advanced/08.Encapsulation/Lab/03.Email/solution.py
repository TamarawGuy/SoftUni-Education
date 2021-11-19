class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __validate_name(self, name):
        return self.min_length <= len(name)

    def __validate_mail(self, mail):
        return mail in self.mails

    def __validate_domain(self, domain):
        return domain in self.domains

    def validate(self, email: str):
        first_part_email = email.split("@")
        second_part_email = email.split(".")
        name = first_part_email[0]
        mail = second_part_email[0].split("@")[1]
        domain = second_part_email[1]

        return self.__validate_name(name) \
            and self.__validate_mail(mail) \
            and self.__validate_domain(domain)