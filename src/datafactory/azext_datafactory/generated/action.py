# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


# pylint: disable=protected-access

# pylint: disable=no-self-use


import argparse
from collections import defaultdict
from knack.util import CLIError


class AddFactoryVstsConfiguration(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.factory_vsts_configuration = action

    def get_action(self, values, option_string):
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]

            if kl == 'project-name':
                d['project_name'] = v[0]

            elif kl == 'tenant-id':
                d['tenant_id'] = v[0]

            elif kl == 'account-name':
                d['account_name'] = v[0]

            elif kl == 'repository-name':
                d['repository_name'] = v[0]

            elif kl == 'collaboration-branch':
                d['collaboration_branch'] = v[0]

            elif kl == 'root-folder':
                d['root_folder'] = v[0]

            elif kl == 'last-commit-id':
                d['last_commit_id'] = v[0]

            else:
                raise CLIError(
                    'Unsupported Key {} is provided for parameter factory-vsts-configuration. All possible keys are:'
                    ' project-name, tenant-id, account-name, repository-name, collaboration-branch, root-folder,'
                    ' last-commit-id'.format(k)
                )

        d['type'] = 'FactoryVSTSConfiguration'

        return d


class AddFactoryGitHubConfiguration(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.factory_git_hub_configuration = action

    def get_action(self, values, option_string):
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]

            if kl == 'host-name':
                d['host_name'] = v[0]

            elif kl == 'account-name':
                d['account_name'] = v[0]

            elif kl == 'repository-name':
                d['repository_name'] = v[0]

            elif kl == 'collaboration-branch':
                d['collaboration_branch'] = v[0]

            elif kl == 'root-folder':
                d['root_folder'] = v[0]

            elif kl == 'last-commit-id':
                d['last_commit_id'] = v[0]

            else:
                raise CLIError(
                    'Unsupported Key {} is provided for parameter factory-git-hub-configuration. All possible keys are:'
                    ' host-name, account-name, repository-name, collaboration-branch, root-folder, last-commit-id'
                    .format(k)
                )

        d['type'] = 'FactoryGitHubConfiguration'

        return d


class AddFolder(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.folder = action

    def get_action(self, values, option_string):
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]

            if kl == 'name':
                d['name'] = v[0]

            else:
                raise CLIError(
                    'Unsupported Key {} is provided for parameter folder. All possible keys are: name'.format(k)
                )

        return d


class AddFilters(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddFilters, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]

            if kl == 'operand':
                d['operand'] = v[0]

            elif kl == 'operator':
                d['operator'] = v[0]

            elif kl == 'values':
                d['values'] = v

            else:
                raise CLIError(
                    'Unsupported Key {} is provided for parameter filters. All possible keys are: operand, operator,'
                    ' values'.format(k)
                )

        return d


class AddOrderBy(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddOrderBy, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]

            if kl == 'order-by':
                d['order_by'] = v[0]

            elif kl == 'order':
                d['order'] = v[0]

            else:
                raise CLIError(
                    'Unsupported Key {} is provided for parameter order-by. All possible keys are: order-by, order'
                    .format(k)
                )

        return d
