from rest_framework import serializers
from .models import GenericFileUpload, Message, MessageAttachment


class GenericFileUploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = GenericFileUpload
        fields = "__all__"


class MessageAttachmentSerializer(serializers.ModelSerializer):
    attachment = GenericFileUploadSerializer()

    class Meta:
        model = MessageAttachment
        fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.SerializerMethodField("get_sender_data")
    sender_id = serializers.IntegerField(write_only=True)
    receiver = serializers.SerializerMethodField("get_receiver_data")
    receiver_id = serializers.IntegerField(write_only=True)
    message_attachments = MessageAttachmentSerializer(
        read_only=True, many=True)
    

    class Meta:
        model = Message
        fields = "__all__"

    def get_receiver_data(self, obj):
        from user_control.serializers import UserProfileSerializer
        x = UserProfileSerializer(obj.receiver.user_profile).data
        # print("Receiver Data : ",x)
        return x

    def get_sender_data(self, obj):
        from user_control.serializers import UserProfileSerializer
        x = UserProfileSerializer(obj.sender.user_profile).data
        # print("Sender Data : ",x)
        return x
