# Encoding: utf-8

# --
# Copyright (c) 2008-2024 Net-ng.
# All rights reserved.
#
# This software is licensed under the BSD License, as described in
# the file LICENSE.txt, which you should have received as part of
# this distribution.
# --

"""Provides classes to interact with AWS."""

import boto3

from nagare.services import plugin


class AWS(plugin.Plugin):
    CONFIG_SPEC = dict(
        plugin.Plugin.CONFIG_SPEC,
        endpoint_url='string(default=None)',
        access_key_id='string(default=None)',
        secret_access_key='string(default=None)',
        session_token='string(default=None)',
        region='string(default=None)',
        ssl='boolean(default=True)',
        verify='boolean(default=True)',
    )

    @staticmethod
    def _create_resource(service, access_key_id, secret_access_key, session_token, region, ssl, activated, **config):
        return boto3.resource(
            service,
            aws_access_key_id=access_key_id,
            aws_secret_access_key=secret_access_key,
            aws_session_token=session_token,
            region_name=region,
            use_ssl=ssl,
            **config,
        )

    def create_resource(self, service):
        return self._create_resource(service, **self.plugin_config)
