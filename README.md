# email_sms

This package implements an email to SMS gateway.
Many cell carriers offer a service where you can send text messages to
your phone by sending an email to a particular email address. Sending a
message in the form of "send <message> to <recipient>" to an SMSNode will send `<message>`
to the SMS gateway email address associated with the recipient in the
configuration, and the recipient will receive `<message>` as an SMS message
on their phone.

## Configuration

Before setting up this package, you must have a gmail address set up in order
to have an account to send emails from. The email and password for this
account should be added to the configuration below.

To install this package, clone this repo in the `packages` directory for the
automation system. In the `config.yml` file, add the following under `nodes`:

```yaml
sms_node:
  node_type: email_sms.sms_node
  config:
    email: <email>
    password: <password>
    recipients:
      # Mapping of recipients to their SMS gateway emails
      <recipient_name>: <recipient_sms_gateway_email>
```

and the following under `conditions`:
```yaml
email_sms.sms_conditions:
```
