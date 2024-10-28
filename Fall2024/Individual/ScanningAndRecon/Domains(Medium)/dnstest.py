import dns.resolver

def check_dns_records(domain):
    record_types = ['A', 'AAAA', 'CNAME', 'MX', 'TXT', 'NS', 'SOA', 'PTR', 'SRV', 'CAA', 'DS', 'DNSKEY']
    found_records = {}

    for record_type in record_types:
        try:
            answers = dns.resolver.resolve(domain, record_type)
            found_records[record_type] = answers
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.Timeout):
            found_records[record_type] = None

    return found_records




domain = "answer.domain.cityinthe.cloud"
records = check_dns_records(domain)

print(f"DNS records for {domain}:")
for record_type, answers in records.items():
    if answers:
        print(f"{record_type}: {', '.join(str(answer) for answer in answers)}")
    else:
        print(f"{record_type}: Not found")


