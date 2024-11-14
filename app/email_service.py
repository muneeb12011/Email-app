from .models import emails

def get_emails():
    return emails

def mark_email_as_read(email_id):
    for email in emails:
        if email['id'] == email_id:
            email['isRead'] = True
            return f"Email {email_id} marked as read."
    return "Email not found."

def delete_email(email_id):
    global emails
    emails = [email for email in emails if email['id'] != email_id]
    return f"Email {email_id} deleted."

def add_email(data):
    new_id = max(email['id'] for email in emails) + 1 if emails else 1
    new_email = {**data, 'id': new_id, 'isRead': False}
    emails.append(new_email)
    return new_email
