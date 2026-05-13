from insert_pgvector import insert_qa


SAMPLE_ENTRIES = [
    {
        "question": "I can access Outlook and Teams, but the VPN says my credentials are invalid.",
        "answer": "Verify whether the VPN authenticates against Active Directory or a separate MFA provider. Reset cached VPN credentials and confirm the account is not locked.",
        "category": "IAM",
    },
    {
        "question": "Internal company websites load on office Wi-Fi but fail completely from home.",
        "answer": "Test from another network or mobile hotspot to determine whether the ISP or IP range is blocked. Verify split-tunnel VPN configuration and DNS resolution.",
        "category": "Networking",
    },
    {
        "question": "The classroom projector powers on, but the laptop only shows a black screen during presentations.",
        "answer": "Verify the correct input source is selected on the projector, check HDMI or DisplayPort cable integrity, and confirm the operating system detects the external display.",
        "category": "AV Support",
    },
    {
        "question": "The password reset portal says my account does not exist, but I can still access email on my phone.",
        "answer": "Check whether the user is authenticating with an old cached mobile session. Verify the UPN and confirm the account was not moved to a disabled organizational unit.",
        "category": "IAM",
    },
    {
        "question": "VPN connects successfully but no internal resources are reachable afterward.",
        "answer": "Check whether routes are being pushed correctly after VPN connection. Verify DNS settings, split tunneling policy, and firewall restrictions.",
        "category": "Networking",
    },
    {
        "question": "After a Windows update, the external monitor connected through the docking station is no longer detected.",
        "answer": "Update docking station firmware and graphics drivers, then verify the USB-C or DisplayPort connection chain.",
        "category": "Endpoint",
    },
    {
        "question": "Outgoing emails remain stuck in Outlook's Outbox and never send.",
        "answer": "Verify Exchange connectivity, mailbox quota limits, and whether Outlook is operating in offline mode.",
        "category": "Email",
    },
    {
        "question": "The printer appears online, but every print job stays in the queue indefinitely.",
        "answer": "Restart the print spooler service and verify the printer driver matches the installed hardware model.",
        "category": "Printer",
    },
    {
        "question": "The laptop becomes extremely slow whenever Teams and Chrome are open together.",
        "answer": "Check memory utilization, background startup processes, and hardware acceleration settings in Teams and the browser.",
        "category": "Endpoint",
    },
    {
        "question": "Remote desktop works for several minutes and then disconnects unexpectedly.",
        "answer": "Investigate VPN stability, idle timeout policies, and packet drops between the client and gateway firewall.",
        "category": "Networking",
    },
    {
        "question": "A shared mailbox suddenly disappeared from Outlook for multiple employees.",
        "answer": "Confirm mailbox permissions were not modified and force Outlook to refresh autodiscover and mailbox mappings.",
        "category": "Email",
    },
    {
        "question": "The application works locally but cannot connect to the PostgreSQL database after deployment.",
        "answer": "Verify environment variables, Docker networking configuration, exposed ports, and firewall rules between containers and the database host.",
        "category": "Backend",
    },
    {
        "question": "Users can connect to Wi-Fi, but webpages load extremely slowly and video calls freeze.",
        "answer": "Check for DNS latency, packet loss, bandwidth saturation, and access point congestion. Verify QoS configuration for real-time traffic.",
        "category": "Networking",
    },
    {
        "question": "The customer receives MFA prompts repeatedly throughout the day even after successful login.",
        "answer": "Review conditional access policies, token expiration settings, and device trust registration. Check for repeated failed login attempts.",
        "category": "Security",
    },
    {
        "question": "PDF files fail to print, but Word documents print normally.",
        "answer": "Check for corrupted PDF rendering, outdated Adobe Reader versions, or PostScript driver incompatibilities.",
        "category": "Printer",
    },
]


def seed_cache() -> None:
    for entry in SAMPLE_ENTRIES:
        insert_qa(
            question=entry["question"],
            answer=entry["answer"],
            category=entry["category"],
        )

    print(f"Seeded {len(SAMPLE_ENTRIES)} entries.")


if __name__ == "__main__":
    seed_cache()