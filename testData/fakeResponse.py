import json

rawListUser = '''
    [
      {
        "id": 1,
        "name": "bencini-informatica",
        "url": "",
        "description": "",
        "link": "http://www.commercialista-on-line.it/demo/author/bencini-informatica/",
        "slug": "bencini-informatica",
        "avatar_urls": {
          "24": "http://0.gravatar.com/avatar/33ca7c6812bb19a8393508e387af5733?s=24&d=mm&r=g",
          "48": "http://0.gravatar.com/avatar/33ca7c6812bb19a8393508e387af5733?s=48&d=mm&r=g",
          "96": "http://0.gravatar.com/avatar/33ca7c6812bb19a8393508e387af5733?s=96&d=mm&r=g"
        },
        "meta": [],
        "_links": {
          "self": [
            {
              "href": "http://www.commercialista-on-line.it/demo/wp-json/wp/v2/users/1"
            }
          ],
          "collection": [
            {
              "href": "http://www.commercialista-on-line.it/demo/wp-json/wp/v2/users"
            }
          ]
        }
      },
      {
        "id": 2,
        "name": "filippo",
        "url": "",
        "description": "",
        "link": "http://www.commercialista-on-line.it/demo/author/filippo/",
        "slug": "filippo",
        "avatar_urls": {
          "24": "http://1.gravatar.com/avatar/1ed3e07e9bbfc3ad3b10fe68032072d5?s=24&d=mm&r=g",
          "48": "http://1.gravatar.com/avatar/1ed3e07e9bbfc3ad3b10fe68032072d5?s=48&d=mm&r=g",
          "96": "http://1.gravatar.com/avatar/1ed3e07e9bbfc3ad3b10fe68032072d5?s=96&d=mm&r=g"
        },
        "meta": [],
        "_links": {
          "self": [
            {
              "href": "http://www.commercialista-on-line.it/demo/wp-json/wp/v2/users/2"
            }
          ],
          "collection": [
            {
              "href": "http://www.commercialista-on-line.it/demo/wp-json/wp/v2/users"
            }
          ]
        }
      },
      {
        "id": 7,
        "name": "Pietro",
        "url": "",
        "description": "",
        "link": "http://www.commercialista-on-line.it/demo/author/pietroleoni1994/",
        "slug": "pietroleoni1994",
        "avatar_urls": {
          "24": "http://2.gravatar.com/avatar/2865c36f6717aa73ca6685959329829d?s=24&d=mm&r=g",
          "48": "http://2.gravatar.com/avatar/2865c36f6717aa73ca6685959329829d?s=48&d=mm&r=g",
          "96": "http://2.gravatar.com/avatar/2865c36f6717aa73ca6685959329829d?s=96&d=mm&r=g"
        },
        "meta": [],
        "_links": {
          "self": [
            {
              "href": "http://www.commercialista-on-line.it/demo/wp-json/wp/v2/users/7"
            }
          ],
          "collection": [
            {
              "href": "http://www.commercialista-on-line.it/demo/wp-json/wp/v2/users"
            }
          ]
        }
      },
      {
        "id": 6,
        "name": "pippo",
        "url": "",
        "description": "",
        "link": "http://www.commercialista-on-line.it/demo/author/pippo/",
        "slug": "pippo",
        "avatar_urls": {
          "24": "http://1.gravatar.com/avatar/aaa251addba914ed521eeed12b08daf3?s=24&d=mm&r=g",
          "48": "http://1.gravatar.com/avatar/aaa251addba914ed521eeed12b08daf3?s=48&d=mm&r=g",
          "96": "http://1.gravatar.com/avatar/aaa251addba914ed521eeed12b08daf3?s=96&d=mm&r=g"
        },
        "meta": [],
        "_links": {
          "self": [
            {
              "href": "http://www.commercialista-on-line.it/demo/wp-json/wp/v2/users/6"
            }
          ],
          "collection": [
            {
              "href": "http://www.commercialista-on-line.it/demo/wp-json/wp/v2/users"
            }
          ]
        }
      },
      {
        "id": 5,
        "name": "Pippo",
        "url": "",
        "description": "",
        "link": "http://www.commercialista-on-line.it/demo/author/pietro/",
        "slug": "pietro",
        "avatar_urls": {
          "24": "http://1.gravatar.com/avatar/d43edc8b4fbfac59088e243c1897142b?s=24&d=mm&r=g",
          "48": "http://1.gravatar.com/avatar/d43edc8b4fbfac59088e243c1897142b?s=48&d=mm&r=g",
          "96": "http://1.gravatar.com/avatar/d43edc8b4fbfac59088e243c1897142b?s=96&d=mm&r=g"
        },
        "meta": [],
        "_links": {
          "self": [
            {
              "href": "http://www.commercialista-on-line.it/demo/wp-json/wp/v2/users/5"
            }
          ],
          "collection": [
            {
              "href": "http://www.commercialista-on-line.it/demo/wp-json/wp/v2/users"
            }
          ]
        }
      }
    ]
'''
rawListSubscription = '''
    [
      {
        "id": 53,
        "parent_id": 52,
        "status": "on-hold",
        "order_key": "wc_order_589c44ab81aac",
        "number": 53,
        "currency": "EUR",
        "version": "2.6.14",
        "prices_include_tax": false,
        "date_created": "2017-02-09T10:30:03",
        "date_modified": "2017-02-10T14:41:37",
        "customer_id": 7,
        "discount_total": "0.00",
        "discount_tax": "0.00",
        "shipping_total": "0.00",
        "shipping_tax": "0.00",
        "cart_tax": "0.00",
        "total": "10.00",
        "total_tax": "0.00",
        "billing": {
          "first_name": "Pietro",
          "last_name": "Rossi",
          "company": "",
          "address_1": "via rossi 55",
          "address_2": "",
          "city": "Sesto F.no",
          "state": "FI",
          "postcode": "50019",
          "country": "IT",
          "email": "pietroleoni1994@gmail.com",
          "phone": "3333333"
        },
        "shipping": {
          "first_name": "Pietro",
          "last_name": "Rossi",
          "company": "",
          "address_1": "via rossi 55",
          "address_2": "",
          "city": "Sesto F.no",
          "state": "FI",
          "postcode": "50019",
          "country": "IT"
        },
        "payment_method": "bacs",
        "payment_method_title": "Bonifico bancario",
        "transaction_id": "",
        "customer_ip_address": "31.193.24.204",
        "customer_user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:51.0) Gecko/20100101 Firefox/51.0",
        "created_via": "checkout",
        "customer_note": "",
        "date_completed": "2017-02-10T15:41:37",
        "date_paid": "",
        "cart_hash": "b74d0f6231907493a5c17a453bc57f02",
        "line_items": [
          {
            "id": 9,
            "name": "Test abbonamento 2",
            "sku": "",
            "product_id": 39,
            "variation_id": 0,
            "quantity": 1,
            "tax_class": "",
            "price": "10.00",
            "subtotal": "10.00",
            "subtotal_tax": "0.00",
            "total": "10.00",
            "total_tax": "0.00",
            "taxes": [],
            "meta": []
          }
        ],
        "tax_lines": [],
        "shipping_lines": [],
        "fee_lines": [],
        "coupon_lines": [],
        "refunds": [],
        "billing_period": "day",
        "billing_interval": "1",
        "start_date": "2017-02-09T10:30:03",
        "trial_end_date": null,
        "next_payment_date": "2017-02-10T10:30:03",
        "end_date": "2017-02-19T10:30:03",
        "_links": {
          "self": [
            {
              "href": "http://www.commercialista-on-line.it/demo/wp-json/wc/v1/subscriptions/53"
            }
          ],
          "collection": [
            {
              "href": "http://www.commercialista-on-line.it/demo/wp-json/wc/v1/subscriptions"
            }
          ],
          "customer": [
            {
              "href": "http://www.commercialista-on-line.it/demo/wp-json/wc/v1/customers/7"
            }
          ],
          "up": [
            {
              "href": "http://www.commercialista-on-line.it/demo/wp-json/wc/v1/orders/52"
            }
          ]
        }
      },
      {
        "id": 41,
        "parent_id": 40,
        "status": "expired",
        "order_key": "wc_order_5899ffbe241a8",
        "number": 41,
        "currency": "EUR",
        "version": "2.6.14",
        "prices_include_tax": false,
        "date_created": "2017-02-07T17:11:25",
        "date_modified": "2017-02-09T10:05:14",
        "customer_id": 7,
        "discount_total": "0.00",
        "discount_tax": "0.00",
        "shipping_total": "0.00",
        "shipping_tax": "0.00",
        "cart_tax": "0.00",
        "total": "10.00",
        "total_tax": "0.00",
        "billing": {
          "first_name": "Pietro",
          "last_name": "Rossi",
          "company": "",
          "address_1": "via rossi 55",
          "address_2": "",
          "city": "Sesto F.no",
          "state": "FI",
          "postcode": "50019",
          "country": "IT",
          "email": "pietroleoni1994@gmail.com",
          "phone": "3333333"
        },
        "shipping": {
          "first_name": "Pietro",
          "last_name": "Rossi",
          "company": "",
          "address_1": "via rossi 55",
          "address_2": "",
          "city": "Sesto F.no",
          "state": "FI",
          "postcode": "50019",
          "country": "IT"
        },
        "payment_method": "bacs",
        "payment_method_title": "Bonifico bancario",
        "transaction_id": "",
        "customer_ip_address": "31.193.30.210",
        "customer_user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:51.0) Gecko/20100101 Firefox/51.0",
        "created_via": "checkout",
        "customer_note": "",
        "date_completed": "2017-02-09T11:05:14",
        "date_paid": "",
        "cart_hash": "b74d0f6231907493a5c17a453bc57f02",
        "line_items": [
          {
            "id": 7,
            "name": "Test abbonamento 2",
            "sku": "",
            "product_id": 39,
            "variation_id": 0,
            "quantity": 1,
            "tax_class": "",
            "price": "10.00",
            "subtotal": "10.00",
            "subtotal_tax": "0.00",
            "total": "10.00",
            "total_tax": "0.00",
            "taxes": [],
            "meta": []
          }
        ],
        "tax_lines": [],
        "shipping_lines": [],
        "fee_lines": [],
        "coupon_lines": [],
        "refunds": [],
        "billing_period": "day",
        "billing_interval": "1",
        "start_date": "2017-02-07T17:11:25",
        "trial_end_date": null,
        "next_payment_date": null,
        "end_date": "2017-02-09T10:05:14",
        "_links": {
          "self": [
            {
              "href": "http://www.commercialista-on-line.it/demo/wp-json/wc/v1/subscriptions/41"
            }
          ],
          "collection": [
            {
              "href": "http://www.commercialista-on-line.it/demo/wp-json/wc/v1/subscriptions"
            }
          ],
          "customer": [
            {
              "href": "http://www.commercialista-on-line.it/demo/wp-json/wc/v1/customers/7"
            }
          ],
          "up": [
            {
              "href": "http://www.commercialista-on-line.it/demo/wp-json/wc/v1/orders/40"
            }
          ]
        }
      },
      {
        "id": 35,
        "parent_id": 34,
        "status": "active",
        "order_key": "wc_order_5899f3dc44a24",
        "number": 35,
        "currency": "EUR",
        "version": "2.6.14",
        "prices_include_tax": false,
        "date_created": "2017-02-07T16:20:44",
        "date_modified": "2017-02-07T16:21:35",
        "customer_id": 5,
        "discount_total": "0.00",
        "discount_tax": "0.00",
        "shipping_total": "0.00",
        "shipping_tax": "0.00",
        "cart_tax": "0.00",
        "total": "50.00",
        "total_tax": "0.00",
        "billing": {
          "first_name": "Pippo",
          "last_name": "rossi",
          "company": "",
          "address_1": "via rossi2",
          "address_2": "",
          "city": "Prato",
          "state": "PO",
          "postcode": "59100",
          "country": "IT",
          "email": "pietro@bencini-informatica.it",
          "phone": "3333333"
        },
        "shipping": {
          "first_name": "Pippo",
          "last_name": "rossi",
          "company": "",
          "address_1": "via rossi2",
          "address_2": "",
          "city": "Prato",
          "state": "PO",
          "postcode": "59100",
          "country": "IT"
        },
        "payment_method": "bacs",
        "payment_method_title": "Bonifico bancario",
        "transaction_id": "",
        "customer_ip_address": "31.193.30.210",
        "customer_user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:51.0) Gecko/20100101 Firefox/51.0",
        "created_via": "checkout",
        "customer_note": "",
        "date_completed": "2017-02-07T17:21:35",
        "date_paid": "",
        "cart_hash": "986763f9a1df3e503ad80ee33cbacff3",
        "line_items": [
          {
            "id": 5,
            "name": "Test abbonamento",
            "sku": "",
            "product_id": 22,
            "variation_id": 0,
            "quantity": 1,
            "tax_class": "",
            "price": "50.00",
            "subtotal": "50.00",
            "subtotal_tax": "0.00",
            "total": "50.00",
            "total_tax": "0.00",
            "taxes": [],
            "meta": []
          }
        ],
        "tax_lines": [],
        "shipping_lines": [],
        "fee_lines": [],
        "coupon_lines": [],
        "refunds": [],
        "billing_period": "month",
        "billing_interval": "1",
        "start_date": "2017-02-07T16:20:44",
        "trial_end_date": null,
        "next_payment_date": "2017-03-07T16:20:44",
        "end_date": "2017-05-07T16:20:44",
        "_links": {
          "self": [
            {
              "href": "http://www.commercialista-on-line.it/demo/wp-json/wc/v1/subscriptions/35"
            }
          ],
          "collection": [
            {
              "href": "http://www.commercialista-on-line.it/demo/wp-json/wc/v1/subscriptions"
            }
          ],
          "customer": [
            {
              "href": "http://www.commercialista-on-line.it/demo/wp-json/wc/v1/customers/5"
            }
          ],
          "up": [
            {
              "href": "http://www.commercialista-on-line.it/demo/wp-json/wc/v1/orders/34"
            }
          ]
        }
      }
    ]
'''
listUser = json.loads(rawListUser)
listSubscription = json.loads(rawListSubscription)
