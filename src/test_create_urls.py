import pytest

import json

import jsonschema

import create_urls

def assert_dicts_equal(a, b):
    assert json.dumps(a, sort_keys=True) == json.dumps(b, sort_keys=True)

get_request = lambda: {
    "resource": "/urls",
    "path": "/urls",
    "httpMethod": "POST",
    "headers": {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "cache-control": "no-cache",
        "CloudFront-Forwarded-Proto": "https",
        "CloudFront-Is-Desktop-Viewer": "true",
        "CloudFront-Is-Mobile-Viewer": "false",
        "CloudFront-Is-SmartTV-Viewer": "false",
        "CloudFront-Is-Tablet-Viewer": "false",
        "CloudFront-Viewer-Country": "US",
        "Content-Type": "application/json",
        "headerName": "headerValue",
        "Host": "gy415nuibc.execute-api.us-east-1.amazonaws.com",
        "Postman-Token": "9f583ef0-ed83-4a38-aef3-eb9ce3f7a57f",
        "User-Agent": "PostmanRuntime/2.4.5",
        "Via": "1.1 d98420743a69852491bbdea73f7680bd.cloudfront.net (CloudFront)",
        "X-Amz-Cf-Id": "pn-PWIJc6thYnZm5P0NMgOUglL1DYtl0gdeJky8tqsg8iS_sgsKD1A==",
        "X-Forwarded-For": "54.240.196.186, 54.182.214.83",
        "X-Forwarded-Port": "443",
        "X-Forwarded-Proto": "https"
    },
    "multiValueHeaders":{
        'Accept':[
        "*/*"
        ],
        'Accept-Encoding':[
        "gzip, deflate"
        ],
        'cache-control':[
        "no-cache"
        ],
        'CloudFront-Forwarded-Proto':[
        "https"
        ],
        'CloudFront-Is-Desktop-Viewer':[
        "true"
        ],
        'CloudFront-Is-Mobile-Viewer':[
        "false"
        ],
        'CloudFront-Is-SmartTV-Viewer':[
        "false"
        ],
        'CloudFront-Is-Tablet-Viewer':[
        "false"
        ],
        'CloudFront-Viewer-Country':[
        "US"
        ],
        '':[
        ""
        ],
        'Content-Type':[
        "application/json"
        ],
        'headerName':[
        "headerValue"
        ],
        'Host':[
        "gy415nuibc.execute-api.us-east-1.amazonaws.com"
        ],
        'Postman-Token':[
        "9f583ef0-ed83-4a38-aef3-eb9ce3f7a57f"
        ],
        'User-Agent':[
        "PostmanRuntime/2.4.5"
        ],
        'Via':[
        "1.1 d98420743a69852491bbdea73f7680bd.cloudfront.net (CloudFront)"
        ],
        'X-Amz-Cf-Id':[
        "pn-PWIJc6thYnZm5P0NMgOUglL1DYtl0gdeJky8tqsg8iS_sgsKD1A=="
        ],
        'X-Forwarded-For':[
        "54.240.196.186, 54.182.214.83"
        ],
        'X-Forwarded-Port':[
        "443"
        ],
        'X-Forwarded-Proto':[
        "https"
        ]
    },
    "queryStringParameters": {
    },
    "multiValueQueryStringParameters":{
        
    },
    "pathParameters": {
    },
    "stageVariables": {
    },
    "requestContext": {
        "accountId": "12345678912",
        "resourceId": "roq9wj",
        "stage": "testStage",
        "requestId": "deef4878-7910-11e6-8f14-25afc3e9ae33",
        "identity": {
            "cognitoIdentityPoolId": None,
            "accountId": None,
            "cognitoIdentityId": None,
            "caller": None,
            "apiKey": None,
            "sourceIp": "192.168.196.186",
            "cognitoAuthenticationType": None,
            "cognitoAuthenticationProvider": None,
            "userArn": None,
            "userAgent": "PostmanRuntime/2.4.5",
            "user": None
        },
        "resourcePath": "/{proxy+}",
        "httpMethod": "POST",
        "apiId": "gy415nuibc"
    },
    "body": "",
    "isBase64Encoded": False
}

get_success = lambda output: {
    'type': 'success',
    'output': output,
}

def get_failure(error=None, reason=None):
    action = {
        'type': 'failure'
    }
    if error:
        action['error'] = error
    if reason:
        action['reason'] = reason
    return action

get_heartbeat = lambda: { 'type': 'heartbeat' }

def get_event(actions,
        expiration=None,
        enable_output_parameters=None,
        api=None):
    event = {
        'token': 'asdf',
        'actions': actions,
    }

    if expiration is not None:
        event['expiration'] = expiration

    if enable_output_parameters is not None:
        event['enable_output_parameters'] = enable_output_parameters
    
    if api is not None:
        event['api'] = api
    
    return event

def test_action_schema():
    def assert_good(obj):
        jsonschema.validate(obj, create_urls.ACTION_SCHEMA)
    
    def assert_bad(obj):
        with pytest.raises(jsonschema.ValidationError):
            jsonschema.validate(obj, create_urls.ACTION_SCHEMA)

    assert_bad({})

    assert_bad({
        'type': 'foo'
    })

    assert_bad({
        'type': 'success'
    })

    assert_bad({
        'type': 'success',
        'output': 'foo'
    })

    assert_good({
        'type': 'success',
        'output': {}
    })
    
    assert_good({
        'type': 'failure'
    })

    assert_bad({
        'type': 'failure',
        'error': {}
    })
    
    assert_good({
        'type': 'failure',
        'error': 'foo'
    })

    assert_bad({
        'type': 'failure',
        'reason': {}
    })
    
    assert_good({
        'type': 'failure',
        'reason': 'foo'
    })

    assert_good({
        'type': 'heartbeat'
    })

def test_event_schema():
    def assert_good(obj):
        jsonschema.validate(obj, create_urls.CREATE_URL_EVENT_SCHEMA)
    
    def assert_bad(obj):
        with pytest.raises(jsonschema.ValidationError):
            jsonschema.validate(obj, create_urls.CREATE_URL_EVENT_SCHEMA)
    
    assert_bad({})

    assert_bad({
        'token': 'foo'
    })

    assert_bad({
        'token': 'foo',
        'actions': {},
    })

    assert_good({
        'token': 'foo',
        'actions': {
            'foo': {
                'type': 'heartbeat'
            },
            'f': {
                'type': 'success',
                'output': {}
            }
        }
    })

    assert_bad({
        'token': 1,
        'actions': {
            'foo': {
                'type': 'heartbeat'
            }
        }
    })

    assert_bad({
        'token': 'foo',
        'actions': {
            '': {
                'type': 'heartbeat'
            }
        }
    })

    assert_bad({
        'token': 'foo',
        'actions': {
            '$foo': {
                'type': 'heartbeat'
            }
        }
    })

def test_wrong_method():
    req = get_request()
    req['httpMethod'] = 'GET'

    resp = create_urls.handler(req, None)

    assert resp['statusCode'] == 405

def test_wrong_content_type():
    req = get_request()
    req['headers']['Content-Type'] = 'text/plain'

    resp = create_urls.handler(req, None)

    assert resp['statusCode'] == 415

def test_empty_body():
    req = get_request()
    
    resp = create_urls.handler(req, None)

    assert resp['statusCode'] == 400

def test_invalid_json():
    req = get_request()

    req['body'] = '{"foo"'

    resp = create_urls.handler(req, None)

    assert resp['statusCode'] == 400
    
    body = json.loads(resp['body'])
    assert body['error'] == 'InvalidJSON'

def test_invalid_event():
    req = get_request()

    req['body'] = json.dumps({
        'token': 1
    })

    resp = create_urls.handler(req, None)

    assert resp['statusCode'] == 400
    
    body = json.loads(resp['body'])
    assert body['error'] == 'InvalidJSON'

def test_basic():
    req = get_request()

    req['body'] = json.dumps(
        get_event(actions={
            'foo': get_success({'spam': 'eggs'}),
            'bar': get_failure(),
            'baz': get_heartbeat()
        })
    )

    resp = create_urls.handler(req, None)
    assert resp['statusCode'] == 200

    body = json.loads(resp['body'])

    assert len(body['urls']) == 3