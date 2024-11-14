from flask import Blueprint, jsonify, request
from .email_service import get_emails, mark_email_as_read, delete_email, add_email

main = Blueprint('main', __name__)

@main.route('/emails', methods=['GET'])
def get_all_emails():
    emails = get_emails()
    return jsonify(emails)

@main.route('/emails/<int:email_id>/read', methods=['POST'])
def mark_as_read(email_id):
    result = mark_email_as_read(email_id)
    return jsonify({'message': result})

@main.route('/emails/<int:email_id>', methods=['DELETE'])
def delete_single_email(email_id):
    result = delete_email(email_id)
    return jsonify({'message': result})

@main.route('/emails', methods=['POST'])
def create_email():
    data = request.get_json()
    email = add_email(data)
    return jsonify(email), 201
