import json

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda! From GitHub Actions..fix test again!!!!???')
    }

if __name__ == "__main__":
    print (lambda_handler({},{}))
