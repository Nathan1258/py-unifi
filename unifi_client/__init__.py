# coding: utf-8

# flake8: noqa

"""
    Unifi API
    Unifi Controller API
    The version of the OpenAPI document: 8.0.26
    Generated by OpenAPI Generator (https://openapi-generator.tech)
    Do not edit the class manually.
"""  # noqa: E501


__version__ = "0.1.0"

# import apis into sdk package
from .api.account_api import AccountApi
from .api.broadcast_group_api import BroadcastGroupApi
from .api.channel_plan_api import ChannelPlanApi
from .api.dhcp_option_api import DHCPOptionApi
from .api.dashboard_api import DashboardApi
from .api.device_api import DeviceApi
from .api.dpi_app_api import DpiAppApi
from .api.dpi_group_api import DpiGroupApi
from .api.dynamic_dns_api import DynamicDNSApi
from .api.firewall_group_api import FirewallGroupApi
from .api.firewall_rule_api import FirewallRuleApi
from .api.heat_map_api import HeatMapApi
from .api.heat_map_point_api import HeatMapPointApi
from .api.hotspot2_conf_api import Hotspot2ConfApi
from .api.hotspot_op_api import HotspotOpApi
from .api.hotspot_package_api import HotspotPackageApi
from .api.map_api import MapApi
from .api.media_file_api import MediaFileApi
from .api.network_api import NetworkApi
from .api.port_forward_api import PortForwardApi
from .api.port_profile_api import PortProfileApi
from .api.radius_profile_api import RADIUSProfileApi
from .api.routing_api import RoutingApi
from .api.schedule_task_api import ScheduleTaskApi
from .api.setting_auto_speedtest_api import SettingAutoSpeedtestApi
from .api.setting_baresip_api import SettingBaresipApi
from .api.setting_broadcast_api import SettingBroadcastApi
from .api.setting_connectivity_api import SettingConnectivityApi
from .api.setting_country_api import SettingCountryApi
from .api.setting_doh_api import SettingDohApi
from .api.setting_dpi_api import SettingDpiApi
from .api.setting_element_adopt_api import SettingElementAdoptApi
from .api.setting_ether_lighting_api import SettingEtherLightingApi
from .api.setting_global_ap_api import SettingGlobalApApi
from .api.setting_global_switch_api import SettingGlobalSwitchApi
from .api.setting_guest_access_api import SettingGuestAccessApi
from .api.setting_ips_api import SettingIpsApi
from .api.setting_lcm_api import SettingLcmApi
from .api.setting_locale_api import SettingLocaleApi
from .api.setting_magic_site_to_site_vpn_api import SettingMagicSiteToSiteVpnApi
from .api.setting_mgmt_api import SettingMgmtApi
from .api.setting_network_optimization_api import SettingNetworkOptimizationApi
from .api.setting_ntp_api import SettingNtpApi
from .api.setting_porta_api import SettingPortaApi
from .api.setting_radio_ai_api import SettingRadioAiApi
from .api.setting_radius_api import SettingRadiusApi
from .api.setting_rsyslogd_api import SettingRsyslogdApi
from .api.setting_snmp_api import SettingSnmpApi
from .api.setting_super_cloudaccess_api import SettingSuperCloudaccessApi
from .api.setting_super_events_api import SettingSuperEventsApi
from .api.setting_super_fwupdate_api import SettingSuperFwupdateApi
from .api.setting_super_identity_api import SettingSuperIdentityApi
from .api.setting_super_mail_api import SettingSuperMailApi
from .api.setting_super_mgmt_api import SettingSuperMgmtApi
from .api.setting_super_sdn_api import SettingSuperSdnApi
from .api.setting_super_smtp_api import SettingSuperSmtpApi
from .api.setting_teleport_api import SettingTeleportApi
from .api.setting_usg_api import SettingUsgApi
from .api.setting_usw_api import SettingUswApi
from .api.spatial_record_api import SpatialRecordApi
from .api.tag_api import TagApi
from .api.user_api import UserApi
from .api.user_group_api import UserGroupApi
from .api.virtual_device_api import VirtualDeviceApi
from .api.wlan_api import WLANApi
from .api.wlan_group_api import WLANGroupApi

# import ApiClient
from .api_response import ApiResponse
from .api_client import ApiClient
from .configuration import Configuration
from .exceptions import OpenApiException
from .exceptions import ApiTypeError
from .exceptions import ApiValueError
from .exceptions import ApiKeyError
from .exceptions import ApiAttributeError
from .exceptions import ApiException

# import models into sdk package
from .models.account import Account
from .models.account_response import AccountResponse
from .models.account_update_request import AccountUpdateRequest
from .models.broadcast_group import BroadcastGroup
from .models.broadcast_group_response import BroadcastGroupResponse
from .models.broadcast_group_update_request import BroadcastGroupUpdateRequest
from .models.channel_plan import ChannelPlan
from .models.channel_plan_ap_blacklisted_channels import ChannelPlanApBlacklistedChannels
from .models.channel_plan_coupling import ChannelPlanCoupling
from .models.channel_plan_radio_table import ChannelPlanRadioTable
from .models.channel_plan_response import ChannelPlanResponse
from .models.channel_plan_satisfaction_table import ChannelPlanSatisfactionTable
from .models.channel_plan_site_blacklisted_channels import ChannelPlanSiteBlacklistedChannels
from .models.channel_plan_update_request import ChannelPlanUpdateRequest
from .models.dhcp_option import DHCPOption
from .models.dhcp_option_response import DHCPOptionResponse
from .models.dhcp_option_update_request import DHCPOptionUpdateRequest
from .models.dashboard import Dashboard
from .models.dashboard_modules import DashboardModules
from .models.dashboard_response import DashboardResponse
from .models.dashboard_update_request import DashboardUpdateRequest
from .models.device import Device
from .models.device_config_network import DeviceConfigNetwork
from .models.device_connected_battery_overrides import DeviceConnectedBatteryOverrides
from .models.device_ether_lighting import DeviceEtherLighting
from .models.device_ethernet_overrides import DeviceEthernetOverrides
from .models.device_outlet_overrides import DeviceOutletOverrides
from .models.device_port_overrides import DevicePortOverrides
from .models.device_radio_i_dentifiers import DeviceRadioIDentifiers
from .models.device_radio_table import DeviceRadioTable
from .models.device_response import DeviceResponse
from .models.device_rps_override import DeviceRpsOverride
from .models.device_rps_port_table import DeviceRpsPortTable
from .models.device_update_request import DeviceUpdateRequest
from .models.dpi_app import DpiApp
from .models.dpi_app_response import DpiAppResponse
from .models.dpi_app_update_request import DpiAppUpdateRequest
from .models.dpi_group import DpiGroup
from .models.dpi_group_response import DpiGroupResponse
from .models.dpi_group_update_request import DpiGroupUpdateRequest
from .models.dynamic_dns import DynamicDNS
from .models.dynamic_dns_response import DynamicDNSResponse
from .models.dynamic_dns_update_request import DynamicDNSUpdateRequest
from .models.firewall_group import FirewallGroup
from .models.firewall_group_response import FirewallGroupResponse
from .models.firewall_group_update_request import FirewallGroupUpdateRequest
from .models.firewall_rule import FirewallRule
from .models.firewall_rule_response import FirewallRuleResponse
from .models.firewall_rule_update_request import FirewallRuleUpdateRequest
from .models.get_setting_auto_speedtest_default_response import GetSettingAutoSpeedtestDefaultResponse
from .models.get_setting_auto_speedtest_default_response_data_inner import GetSettingAutoSpeedtestDefaultResponseDataInner
from .models.heat_map import HeatMap
from .models.heat_map_point import HeatMapPoint
from .models.heat_map_point_response import HeatMapPointResponse
from .models.heat_map_point_update_request import HeatMapPointUpdateRequest
from .models.heat_map_response import HeatMapResponse
from .models.heat_map_update_request import HeatMapUpdateRequest
from .models.hotspot2_conf import Hotspot2Conf
from .models.hotspot2_conf_capab import Hotspot2ConfCapab
from .models.hotspot2_conf_cellular_network_list import Hotspot2ConfCellularNetworkList
from .models.hotspot2_conf_description import Hotspot2ConfDescription
from .models.hotspot2_conf_friendly_name import Hotspot2ConfFriendlyName
from .models.hotspot2_conf_icon import Hotspot2ConfIcon
from .models.hotspot2_conf_icons import Hotspot2ConfIcons
from .models.hotspot2_conf_nai_realm_list import Hotspot2ConfNaiRealmList
from .models.hotspot2_conf_osu import Hotspot2ConfOsu
from .models.hotspot2_conf_qos_map_dcsp import Hotspot2ConfQOSMapDcsp
from .models.hotspot2_conf_qos_map_exceptions import Hotspot2ConfQOSMapExceptions
from .models.hotspot2_conf_response import Hotspot2ConfResponse
from .models.hotspot2_conf_roaming_consortium_list import Hotspot2ConfRoamingConsortiumList
from .models.hotspot2_conf_update_request import Hotspot2ConfUpdateRequest
from .models.hotspot2_conf_venue_name import Hotspot2ConfVenueName
from .models.hotspot_op import HotspotOp
from .models.hotspot_op_response import HotspotOpResponse
from .models.hotspot_op_update_request import HotspotOpUpdateRequest
from .models.hotspot_package import HotspotPackage
from .models.hotspot_package_response import HotspotPackageResponse
from .models.hotspot_package_update_request import HotspotPackageUpdateRequest
from .models.map import Map
from .models.map_response import MapResponse
from .models.map_update_request import MapUpdateRequest
from .models.media_file import MediaFile
from .models.media_file_response import MediaFileResponse
from .models.media_file_update_request import MediaFileUpdateRequest
from .models.meta import Meta
from .models.network import Network
from .models.network_nat_outbound_ip_addresses import NetworkNATOutboundIPAddresses
from .models.network_response import NetworkResponse
from .models.network_update_request import NetworkUpdateRequest
from .models.network_wandhcp_options import NetworkWANDHCPOptions
from .models.network_wan_provider_capabilities import NetworkWANProviderCapabilities
from .models.port_forward import PortForward
from .models.port_forward_response import PortForwardResponse
from .models.port_forward_update_request import PortForwardUpdateRequest
from .models.port_profile import PortProfile
from .models.port_profile_response import PortProfileResponse
from .models.port_profile_update_request import PortProfileUpdateRequest
from .models.radius_profile import RADIUSProfile
from .models.radius_profile_acct_servers import RADIUSProfileAcctServers
from .models.radius_profile_auth_servers import RADIUSProfileAuthServers
from .models.radius_profile_response import RADIUSProfileResponse
from .models.radius_profile_update_request import RADIUSProfileUpdateRequest
from .models.routing import Routing
from .models.routing_response import RoutingResponse
from .models.routing_update_request import RoutingUpdateRequest
from .models.schedule_task import ScheduleTask
from .models.schedule_task_response import ScheduleTaskResponse
from .models.schedule_task_update_request import ScheduleTaskUpdateRequest
from .models.schedule_task_upgrade_targets import ScheduleTaskUpgradeTargets
from .models.setting_auto_speedtest import SettingAutoSpeedtest
from .models.setting_auto_speedtest_response import SettingAutoSpeedtestResponse
from .models.setting_baresip import SettingBaresip
from .models.setting_baresip_response import SettingBaresipResponse
from .models.setting_broadcast import SettingBroadcast
from .models.setting_broadcast_response import SettingBroadcastResponse
from .models.setting_connectivity import SettingConnectivity
from .models.setting_connectivity_response import SettingConnectivityResponse
from .models.setting_country import SettingCountry
from .models.setting_country_response import SettingCountryResponse
from .models.setting_doh import SettingDoh
from .models.setting_doh_response import SettingDohResponse
from .models.setting_dpi import SettingDpi
from .models.setting_dpi_response import SettingDpiResponse
from .models.setting_element_adopt import SettingElementAdopt
from .models.setting_element_adopt_response import SettingElementAdoptResponse
from .models.setting_ether_lighting import SettingEtherLighting
from .models.setting_ether_lighting_network_overrides import SettingEtherLightingNetworkOverrides
from .models.setting_ether_lighting_response import SettingEtherLightingResponse
from .models.setting_ether_lighting_speed_overrides import SettingEtherLightingSpeedOverrides
from .models.setting_global_ap import SettingGlobalAp
from .models.setting_global_ap_response import SettingGlobalApResponse
from .models.setting_global_switch import SettingGlobalSwitch
from .models.setting_global_switch_response import SettingGlobalSwitchResponse
from .models.setting_guest_access import SettingGuestAccess
from .models.setting_guest_access_response import SettingGuestAccessResponse
from .models.setting_ips import SettingIps
from .models.setting_ips_ad_blocking_configurations import SettingIpsAdBlockingConfigurations
from .models.setting_ips_alerts import SettingIpsAlerts
from .models.setting_ips_dns_filters import SettingIpsDNSFilters
from .models.setting_ips_honeypot import SettingIpsHoneypot
from .models.setting_ips_response import SettingIpsResponse
from .models.setting_ips_suppression import SettingIpsSuppression
from .models.setting_ips_tracking import SettingIpsTracking
from .models.setting_ips_whitelist import SettingIpsWhitelist
from .models.setting_lcm import SettingLcm
from .models.setting_lcm_response import SettingLcmResponse
from .models.setting_locale import SettingLocale
from .models.setting_locale_response import SettingLocaleResponse
from .models.setting_magic_site_to_site_vpn import SettingMagicSiteToSiteVpn
from .models.setting_magic_site_to_site_vpn_response import SettingMagicSiteToSiteVpnResponse
from .models.setting_mgmt import SettingMgmt
from .models.setting_mgmt_response import SettingMgmtResponse
from .models.setting_mgmt_x_ssh_keys import SettingMgmtXSshKeys
from .models.setting_network_optimization import SettingNetworkOptimization
from .models.setting_network_optimization_response import SettingNetworkOptimizationResponse
from .models.setting_ntp import SettingNtp
from .models.setting_ntp_response import SettingNtpResponse
from .models.setting_porta import SettingPorta
from .models.setting_porta_response import SettingPortaResponse
from .models.setting_radio_ai import SettingRadioAi
from .models.setting_radio_ai_response import SettingRadioAiResponse
from .models.setting_radius import SettingRadius
from .models.setting_radius_response import SettingRadiusResponse
from .models.setting_rsyslogd import SettingRsyslogd
from .models.setting_rsyslogd_response import SettingRsyslogdResponse
from .models.setting_snmp import SettingSnmp
from .models.setting_snmp_response import SettingSnmpResponse
from .models.setting_super_cloudaccess import SettingSuperCloudaccess
from .models.setting_super_cloudaccess_response import SettingSuperCloudaccessResponse
from .models.setting_super_events import SettingSuperEvents
from .models.setting_super_events_response import SettingSuperEventsResponse
from .models.setting_super_fwupdate import SettingSuperFwupdate
from .models.setting_super_fwupdate_response import SettingSuperFwupdateResponse
from .models.setting_super_identity import SettingSuperIdentity
from .models.setting_super_identity_response import SettingSuperIdentityResponse
from .models.setting_super_mail import SettingSuperMail
from .models.setting_super_mail_response import SettingSuperMailResponse
from .models.setting_super_mgmt import SettingSuperMgmt
from .models.setting_super_mgmt_response import SettingSuperMgmtResponse
from .models.setting_super_sdn import SettingSuperSdn
from .models.setting_super_sdn_response import SettingSuperSdnResponse
from .models.setting_super_smtp import SettingSuperSmtp
from .models.setting_super_smtp_response import SettingSuperSmtpResponse
from .models.setting_teleport import SettingTeleport
from .models.setting_teleport_response import SettingTeleportResponse
from .models.setting_usg import SettingUsg
from .models.setting_usg_response import SettingUsgResponse
from .models.setting_usw import SettingUsw
from .models.setting_usw_response import SettingUswResponse
from .models.spatial_record import SpatialRecord
from .models.spatial_record_devices import SpatialRecordDevices
from .models.spatial_record_position import SpatialRecordPosition
from .models.spatial_record_response import SpatialRecordResponse
from .models.spatial_record_update_request import SpatialRecordUpdateRequest
from .models.tag import Tag
from .models.tag_response import TagResponse
from .models.tag_update_request import TagUpdateRequest
from .models.user import User
from .models.user_group import UserGroup
from .models.user_group_response import UserGroupResponse
from .models.user_group_update_request import UserGroupUpdateRequest
from .models.user_response import UserResponse
from .models.user_update_request import UserUpdateRequest
from .models.virtual_device import VirtualDevice
from .models.virtual_device_response import VirtualDeviceResponse
from .models.virtual_device_update_request import VirtualDeviceUpdateRequest
from .models.wlan import WLAN
from .models.wlan_group import WLANGroup
from .models.wlan_group_response import WLANGroupResponse
from .models.wlan_group_update_request import WLANGroupUpdateRequest
from .models.wlan_private_preshared_keys import WLANPrivatePresharedKeys
from .models.wlan_response import WLANResponse
from .models.wlan_sae_psk import WLANSaePsk
from .models.wlan_schedule_with_duration import WLANScheduleWithDuration
from .models.wlan_update_request import WLANUpdateRequest
