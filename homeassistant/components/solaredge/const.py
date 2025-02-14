"""Constants for the SolarEdge Monitoring API."""
from datetime import timedelta
import logging

from homeassistant.components.sensor import (
    STATE_CLASS_MEASUREMENT,
    STATE_CLASS_TOTAL,
    STATE_CLASS_TOTAL_INCREASING,
)
from homeassistant.const import (
    DEVICE_CLASS_ENERGY,
    DEVICE_CLASS_POWER,
    ENERGY_WATT_HOUR,
    PERCENTAGE,
    POWER_WATT,
)

from .models import SolarEdgeSensorEntityDescription

DOMAIN = "solaredge"

LOGGER = logging.getLogger(__package__)

DATA_API_CLIENT = "api_client"

# Config for solaredge monitoring api requests.
CONF_SITE_ID = "site_id"
DEFAULT_NAME = "SolarEdge"

OVERVIEW_UPDATE_DELAY = timedelta(minutes=15)
DETAILS_UPDATE_DELAY = timedelta(hours=12)
INVENTORY_UPDATE_DELAY = timedelta(hours=12)
POWER_FLOW_UPDATE_DELAY = timedelta(minutes=15)
ENERGY_DETAILS_DELAY = timedelta(minutes=15)

SCAN_INTERVAL = timedelta(minutes=15)


# Supported overview sensors
SENSOR_TYPES = [
    SolarEdgeSensorEntityDescription(
        key="lifetime_energy",
        json_key="lifeTimeData",
        name="Lifetime energy",
        icon="mdi:solar-power",
        state_class=STATE_CLASS_TOTAL,
        native_unit_of_measurement=ENERGY_WATT_HOUR,
        device_class=DEVICE_CLASS_ENERGY,
    ),
    SolarEdgeSensorEntityDescription(
        key="energy_this_year",
        json_key="lastYearData",
        name="Energy this year",
        entity_registry_enabled_default=False,
        icon="mdi:solar-power",
        native_unit_of_measurement=ENERGY_WATT_HOUR,
        device_class=DEVICE_CLASS_ENERGY,
    ),
    SolarEdgeSensorEntityDescription(
        key="energy_this_month",
        json_key="lastMonthData",
        name="Energy this month",
        entity_registry_enabled_default=False,
        icon="mdi:solar-power",
        native_unit_of_measurement=ENERGY_WATT_HOUR,
        device_class=DEVICE_CLASS_ENERGY,
    ),
    SolarEdgeSensorEntityDescription(
        key="energy_today",
        json_key="lastDayData",
        name="Energy today",
        entity_registry_enabled_default=False,
        icon="mdi:solar-power",
        native_unit_of_measurement=ENERGY_WATT_HOUR,
        device_class=DEVICE_CLASS_ENERGY,
    ),
    SolarEdgeSensorEntityDescription(
        key="current_power",
        json_key="currentPower",
        name="Current Power",
        icon="mdi:solar-power",
        state_class=STATE_CLASS_MEASUREMENT,
        native_unit_of_measurement=POWER_WATT,
        device_class=DEVICE_CLASS_POWER,
    ),
    SolarEdgeSensorEntityDescription(
        key="site_details",
        name="Site details",
        entity_registry_enabled_default=False,
    ),
    SolarEdgeSensorEntityDescription(
        key="meters",
        json_key="meters",
        name="Meters",
        entity_registry_enabled_default=False,
    ),
    SolarEdgeSensorEntityDescription(
        key="sensors",
        json_key="sensors",
        name="Sensors",
        entity_registry_enabled_default=False,
    ),
    SolarEdgeSensorEntityDescription(
        key="gateways",
        json_key="gateways",
        name="Gateways",
        entity_registry_enabled_default=False,
    ),
    SolarEdgeSensorEntityDescription(
        key="batteries",
        json_key="batteries",
        name="Batteries",
        entity_registry_enabled_default=False,
    ),
    SolarEdgeSensorEntityDescription(
        key="inverters",
        json_key="inverters",
        name="Inverters",
        entity_registry_enabled_default=False,
    ),
    SolarEdgeSensorEntityDescription(
        key="power_consumption",
        json_key="LOAD",
        name="Power Consumption",
        entity_registry_enabled_default=False,
        icon="mdi:flash",
    ),
    SolarEdgeSensorEntityDescription(
        key="solar_power",
        json_key="PV",
        name="Solar Power",
        entity_registry_enabled_default=False,
        icon="mdi:solar-power",
    ),
    SolarEdgeSensorEntityDescription(
        key="grid_power",
        json_key="GRID",
        name="Grid Power",
        entity_registry_enabled_default=False,
        icon="mdi:power-plug",
    ),
    SolarEdgeSensorEntityDescription(
        key="storage_power",
        json_key="STORAGE",
        name="Storage Power",
        entity_registry_enabled_default=False,
        icon="mdi:car-battery",
    ),
    SolarEdgeSensorEntityDescription(
        key="purchased_power",
        json_key="Purchased",
        name="Imported Power",
        entity_registry_enabled_default=False,
        state_class=STATE_CLASS_TOTAL_INCREASING,
        native_unit_of_measurement=ENERGY_WATT_HOUR,
        device_class=DEVICE_CLASS_ENERGY,
    ),
    SolarEdgeSensorEntityDescription(
        key="production_power",
        json_key="Production",
        name="Production Power",
        entity_registry_enabled_default=False,
        state_class=STATE_CLASS_TOTAL_INCREASING,
        native_unit_of_measurement=ENERGY_WATT_HOUR,
        device_class=DEVICE_CLASS_ENERGY,
    ),
    SolarEdgeSensorEntityDescription(
        key="consumption_power",
        json_key="Consumption",
        name="Consumption Power",
        entity_registry_enabled_default=False,
        state_class=STATE_CLASS_TOTAL_INCREASING,
        native_unit_of_measurement=ENERGY_WATT_HOUR,
        device_class=DEVICE_CLASS_ENERGY,
    ),
    SolarEdgeSensorEntityDescription(
        key="selfconsumption_power",
        json_key="SelfConsumption",
        name="SelfConsumption Power",
        entity_registry_enabled_default=False,
        state_class=STATE_CLASS_TOTAL_INCREASING,
        native_unit_of_measurement=ENERGY_WATT_HOUR,
        device_class=DEVICE_CLASS_ENERGY,
    ),
    SolarEdgeSensorEntityDescription(
        key="feedin_power",
        json_key="FeedIn",
        name="Exported Power",
        entity_registry_enabled_default=False,
        state_class=STATE_CLASS_TOTAL_INCREASING,
        native_unit_of_measurement=ENERGY_WATT_HOUR,
        device_class=DEVICE_CLASS_ENERGY,
    ),
    SolarEdgeSensorEntityDescription(
        key="storage_level",
        json_key="STORAGE",
        name="Storage Level",
        entity_registry_enabled_default=False,
        state_class=STATE_CLASS_MEASUREMENT,
        native_unit_of_measurement=PERCENTAGE,
    ),
]
