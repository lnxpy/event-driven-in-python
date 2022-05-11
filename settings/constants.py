from faker import Faker

fake = Faker()

volumes = {
    'id': fake.ean,
    'first_name': fake.first_name,
    'last_name': fake.last_name,
    'email': fake.email,
    'number': fake.phone_number,
    'serial': fake.ean,
    'address': fake.address,
}