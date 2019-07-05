import json
import boto3

ec2 = boto3.client('ec2', region_name='eu-west-1')

snapshots = ec2.describe_snapshots(
    OwnerIds=[
        '007388104365'
    ], 
    Filters=[
        {
            'Name': 'tag:Expired', 
            'Values': [
                'yes'
            ]
        }
    ]
)['Snapshots']

to_delete = [snapshot['SnapshotId'] for snapshot in snapshots]
for snap in to_delete:
    response = ec2.delete_snapshot(
        SnapshotId = snap
    )
    print(response)

print(snapshots)