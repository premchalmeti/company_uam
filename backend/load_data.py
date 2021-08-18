
def load_data():
    from companies.models import Company
    from companies.models import (
        CompanyPermission, CompanyRole
    )
    from employees.models import Employee

    veritas = Company.objects.create(name='veritas', address='Pune')

    laptop_perm = CompanyPermission(name='laptop', company=veritas)
    email_perm = CompanyPermission(name='email', company=veritas)
    vcenter_perm = CompanyPermission(name='vcenter', company=veritas)
    cloud_access = CompanyPermission(name='cloud', company=veritas)

    default_permissions = [laptop_perm, email_perm, vcenter_perm]

    CompanyPermission.objects.bulk_create(default_permissions+[cloud_access])

    se = CompanyRole.objects.create(name='software engineer', company=veritas)
    se.permissions.add(*default_permissions)

    sse = CompanyRole.objects.create(name='senior software engineer', company=veritas)
    sse.permissions.add(*(default_permissions+[cloud_access]))

    ragini = Employee.objects.create(
        username='raginidahihande', email='ragini.dahihande@veritas.com',
        mobile_no='+91-9999999999', company=veritas, role=se
    )
    ankur = Employee.objects.create(
        username='ankurmathur', email='ankur.mathur@veritas.com',
        mobile_no='+91-8888888888', company=veritas, role=sse
    )


if __name__ == '__main__':
    from manage import django_setup
    django_setup()
    load_data()
