# coding: UTF-8
import sys
bstack111lll1_opy_ = sys.version_info [0] == 2
bstack11l1l1_opy_ = 2048
bstack11lllll_opy_ = 7
def bstack11lll1_opy_ (bstack111lll_opy_):
    global bstack11ll1l_opy_
    bstack11l11l1_opy_ = ord (bstack111lll_opy_ [-1])
    bstack1l1l_opy_ = bstack111lll_opy_ [:-1]
    bstack1l11l1_opy_ = bstack11l11l1_opy_ % len (bstack1l1l_opy_)
    bstack1lll1l_opy_ = bstack1l1l_opy_ [:bstack1l11l1_opy_] + bstack1l1l_opy_ [bstack1l11l1_opy_:]
    if bstack111lll1_opy_:
        bstack1111lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1_opy_ - (bstack1ll1ll1_opy_ + bstack11l11l1_opy_) % bstack11lllll_opy_) for bstack1ll1ll1_opy_, char in enumerate (bstack1lll1l_opy_)])
    else:
        bstack1111lll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1_opy_ - (bstack1ll1ll1_opy_ + bstack11l11l1_opy_) % bstack11lllll_opy_) for bstack1ll1ll1_opy_, char in enumerate (bstack1lll1l_opy_)])
    return eval (bstack1111lll_opy_)
import os
import json
import requests
import logging
import threading
import bstack_utils.constants as bstack1llll1llll11_opy_
from urllib.parse import urlparse
from bstack_utils.constants import bstack11l1l11ll11_opy_ as bstack1llll1l1l111_opy_, EVENTS
from bstack_utils.bstack11ll1111l_opy_ import bstack11ll1111l_opy_
from bstack_utils.helper import bstack1l1111l1_opy_, bstack11lll1l1_opy_, bstack11l1l1ll1l_opy_, bstack111l1111l11_opy_, \
  bstack111l1ll11l1_opy_, bstack111llllll1_opy_, get_host_info, bstack1111l1l1l11_opy_, bstack1lll111l1l_opy_, error_handler, bstack1111ll1ll11_opy_, bstack111l1ll1l1l_opy_, bstack1lll111l_opy_
from browserstack_sdk._version import __version__
from bstack_utils.bstack1l1l1llll1_opy_ import get_logger
from bstack_utils.bstack1111l111l1_opy_ import bstack1lllllll111_opy_
from selenium.webdriver.chrome.options import Options as ChromeOptions
from browserstack_sdk.sdk_cli.cli import cli
from bstack_utils.constants import *
logger = get_logger(__name__)
bstack1111l111l1_opy_ = bstack1lllllll111_opy_()
@error_handler(class_method=False)
def _1lllll1111l1_opy_(driver, bstack1llll1l1l_opy_):
  response = {}
  try:
    caps = driver.capabilities
    response = {
        bstack11lll1_opy_ (u"ࠨࡱࡶࡣࡳࡧ࡭ࡦࠩΰ"): caps.get(bstack11lll1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡒࡦࡳࡥࠨῤ"), None),
        bstack11lll1_opy_ (u"ࠪࡳࡸࡥࡶࡦࡴࡶ࡭ࡴࡴࠧῥ"): bstack1llll1l1l_opy_.get(bstack11lll1_opy_ (u"ࠫࡴࡹࡖࡦࡴࡶ࡭ࡴࡴࠧῦ"), None),
        bstack11lll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡥ࡮ࡢ࡯ࡨࠫῧ"): caps.get(bstack11lll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫῨ"), None),
        bstack11lll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡸࡨࡶࡸ࡯࡯࡯ࠩῩ"): caps.get(bstack11lll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩῪ"), None)
    }
  except Exception as error:
    logger.debug(bstack11lll1_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡨࡨࡸࡨ࡮ࡩ࡯ࡩࠣࡴࡱࡧࡴࡧࡱࡵࡱࠥࡪࡥࡵࡣ࡬ࡰࡸࠦࡷࡪࡶ࡫ࠤࡪࡸࡲࡰࡴࠣ࠾ࠥ࠭Ύ") + str(error))
  return response
def on():
    if os.environ.get(bstack11lll1_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨῬ"), None) is None or os.environ[bstack11lll1_opy_ (u"ࠫࡇ࡙࡟ࡂ࠳࠴࡝ࡤࡐࡗࡕࠩ῭")] == bstack11lll1_opy_ (u"ࠧࡴࡵ࡭࡮ࠥ΅"):
        return False
    return True
def bstack1111lll11l_opy_(config):
  return config.get(bstack11lll1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭`"), False) or any([p.get(bstack11lll1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ῰"), False) == True for p in config.get(bstack11lll1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ῱"), [])])
def bstack1111l11lll_opy_(config, bstack1lll11ll11_opy_):
  try:
    bstack1llll1l1ll1l_opy_ = config.get(bstack11lll1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩῲ"), False)
    if int(bstack1lll11ll11_opy_) < len(config.get(bstack11lll1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ῳ"), [])) and config[bstack11lll1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧῴ")][bstack1lll11ll11_opy_]:
      bstack1llll1ll11l1_opy_ = config[bstack11lll1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ῵")][bstack1lll11ll11_opy_].get(bstack11lll1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ῶ"), None)
    else:
      bstack1llll1ll11l1_opy_ = config.get(bstack11lll1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧῷ"), None)
    if bstack1llll1ll11l1_opy_ != None:
      bstack1llll1l1ll1l_opy_ = bstack1llll1ll11l1_opy_
    bstack1llll1l1l1l1_opy_ = os.getenv(bstack11lll1_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭Ὸ")) is not None and len(os.getenv(bstack11lll1_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧΌ"))) > 0 and os.getenv(bstack11lll1_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨῺ")) != bstack11lll1_opy_ (u"ࠫࡳࡻ࡬࡭ࠩΏ")
    return bstack1llll1l1ll1l_opy_ and bstack1llll1l1l1l1_opy_
  except Exception as error:
    logger.debug(bstack11lll1_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡻ࡫ࡲࡪࡨࡼ࡭ࡳ࡭ࠠࡵࡪࡨࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡽࡩࡵࡪࠣࡩࡷࡸ࡯ࡳࠢ࠽ࠤࠬῼ") + str(error))
  return False
def bstack11111l1ll_opy_(test_tags):
  bstack1l1111ll11l_opy_ = os.getenv(bstack11lll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡢࡅࡈࡉࡅࡔࡕࡌࡆࡎࡒࡉࡕ࡛ࡢࡇࡔࡔࡆࡊࡉࡘࡖࡆ࡚ࡉࡐࡐࡢ࡝ࡒࡒࠧ´"))
  if bstack1l1111ll11l_opy_ is None:
    return True
  bstack1l1111ll11l_opy_ = json.loads(bstack1l1111ll11l_opy_)
  try:
    include_tags = bstack1l1111ll11l_opy_[bstack11lll1_opy_ (u"ࠧࡪࡰࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩࠬ῾")] if bstack11lll1_opy_ (u"ࠨ࡫ࡱࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ࠭῿") in bstack1l1111ll11l_opy_ and isinstance(bstack1l1111ll11l_opy_[bstack11lll1_opy_ (u"ࠩ࡬ࡲࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧ ")], list) else []
    exclude_tags = bstack1l1111ll11l_opy_[bstack11lll1_opy_ (u"ࠪࡩࡽࡩ࡬ࡶࡦࡨࡘࡦ࡭ࡳࡊࡰࡗࡩࡸࡺࡩ࡯ࡩࡖࡧࡴࡶࡥࠨ ")] if bstack11lll1_opy_ (u"ࠫࡪࡾࡣ࡭ࡷࡧࡩ࡙ࡧࡧࡴࡋࡱࡘࡪࡹࡴࡪࡰࡪࡗࡨࡵࡰࡦࠩ ") in bstack1l1111ll11l_opy_ and isinstance(bstack1l1111ll11l_opy_[bstack11lll1_opy_ (u"ࠬ࡫ࡸࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪ ")], list) else []
    excluded = any(tag in exclude_tags for tag in test_tags)
    included = len(include_tags) == 0 or any(tag in include_tags for tag in test_tags)
    return not excluded and included
  except Exception as error:
    logger.debug(bstack11lll1_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡽࡨࡪ࡮ࡨࠤࡻࡧ࡬ࡪࡦࡤࡸ࡮ࡴࡧࠡࡶࡨࡷࡹࠦࡣࡢࡵࡨࠤ࡫ࡵࡲࠡࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡤࡨࡪࡴࡸࡥࠡࡵࡦࡥࡳࡴࡩ࡯ࡩ࠱ࠤࡊࡸࡲࡰࡴࠣ࠾ࠥࠨ ") + str(error))
  return False
def bstack1llll1lllll1_opy_(config, frameworkName, bstack1llll1llll1l_opy_, bstack1llll1l1l11l_opy_):
  bstack1llll1l1llll_opy_ = bstack111l1111l11_opy_(config)
  bstack1llll1lll1l1_opy_ = bstack111l1ll11l1_opy_(config)
  if bstack1llll1l1llll_opy_ is None or bstack1llll1lll1l1_opy_ is None:
    logger.error(bstack11lll1_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡻ࡭࡯࡬ࡦࠢࡦࡶࡪࡧࡴࡪࡰࡪࠤࡹ࡫ࡳࡵࠢࡵࡹࡳࠦࡦࡰࡴࠣࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡀࠠࡎ࡫ࡶࡷ࡮ࡴࡧࠡࡣࡸࡸ࡭࡫࡮ࡵ࡫ࡦࡥࡹ࡯࡯࡯ࠢࡷࡳࡰ࡫࡮ࠨ "))
    return [None, None]
  try:
    settings = json.loads(os.getenv(bstack11lll1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡤࡇࡃࡄࡇࡖࡗࡎࡈࡉࡍࡋࡗ࡝ࡤࡉࡏࡏࡈࡌࡋ࡚ࡘࡁࡕࡋࡒࡒࡤ࡟ࡍࡍࠩ "), bstack11lll1_opy_ (u"ࠩࡾࢁࠬ ")))
    data = {
        bstack11lll1_opy_ (u"ࠪࡴࡷࡵࡪࡦࡥࡷࡒࡦࡳࡥࠨ "): config[bstack11lll1_opy_ (u"ࠫࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠩ ")],
        bstack11lll1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ "): config.get(bstack11lll1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩ​"), os.path.basename(os.getcwd())),
        bstack11lll1_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡚ࡩ࡮ࡧࠪ‌"): bstack1l1111l1_opy_(),
        bstack11lll1_opy_ (u"ࠨࡦࡨࡷࡨࡸࡩࡱࡶ࡬ࡳࡳ࠭‍"): config.get(bstack11lll1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡅࡧࡶࡧࡷ࡯ࡰࡵ࡫ࡲࡲࠬ‎"), bstack11lll1_opy_ (u"ࠪࠫ‏")),
        bstack11lll1_opy_ (u"ࠫࡸࡵࡵࡳࡥࡨࠫ‐"): {
            bstack11lll1_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡏࡣࡰࡩࠬ‑"): frameworkName,
            bstack11lll1_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡘࡨࡶࡸ࡯࡯࡯ࠩ‒"): bstack1llll1llll1l_opy_,
            bstack11lll1_opy_ (u"ࠧࡴࡦ࡮࡚ࡪࡸࡳࡪࡱࡱࠫ–"): __version__,
            bstack11lll1_opy_ (u"ࠨ࡮ࡤࡲ࡬ࡻࡡࡨࡧࠪ—"): bstack11lll1_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩ―"),
            bstack11lll1_opy_ (u"ࠪࡸࡪࡹࡴࡇࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪ‖"): bstack11lll1_opy_ (u"ࠫࡸ࡫࡬ࡦࡰ࡬ࡹࡲ࠭‗"),
            bstack11lll1_opy_ (u"ࠬࡺࡥࡴࡶࡉࡶࡦࡳࡥࡸࡱࡵ࡯࡛࡫ࡲࡴ࡫ࡲࡲࠬ‘"): bstack1llll1l1l11l_opy_
        },
        bstack11lll1_opy_ (u"࠭ࡳࡦࡶࡷ࡭ࡳ࡭ࡳࠨ’"): settings,
        bstack11lll1_opy_ (u"ࠧࡷࡧࡵࡷ࡮ࡵ࡮ࡄࡱࡱࡸࡷࡵ࡬ࠨ‚"): bstack1111l1l1l11_opy_(),
        bstack11lll1_opy_ (u"ࠨࡥ࡬ࡍࡳ࡬࡯ࠨ‛"): bstack111llllll1_opy_(),
        bstack11lll1_opy_ (u"ࠩ࡫ࡳࡸࡺࡉ࡯ࡨࡲࠫ“"): get_host_info(),
        bstack11lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬ”"): bstack11l1l1ll1l_opy_(config)
    }
    headers = {
        bstack11lll1_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲࡚ࡹࡱࡧࠪ„"): bstack11lll1_opy_ (u"ࠬࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲࡮ࡸࡵ࡮ࠨ‟"),
    }
    config = {
        bstack11lll1_opy_ (u"࠭ࡡࡶࡶ࡫ࠫ†"): (bstack1llll1l1llll_opy_, bstack1llll1lll1l1_opy_),
        bstack11lll1_opy_ (u"ࠧࡩࡧࡤࡨࡪࡸࡳࠨ‡"): headers
    }
    response = bstack1lll111l1l_opy_(bstack11lll1_opy_ (u"ࠨࡒࡒࡗ࡙࠭•"), bstack1llll1l1l111_opy_ + bstack11lll1_opy_ (u"ࠩ࠲ࡺ࠷࠵ࡴࡦࡵࡷࡣࡷࡻ࡮ࡴࠩ‣"), data, config)
    bstack1llll1ll1l11_opy_ = response.json()
    if bstack1llll1ll1l11_opy_[bstack11lll1_opy_ (u"ࠪࡷࡺࡩࡣࡦࡵࡶࠫ․")]:
      parsed = json.loads(os.getenv(bstack11lll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡠࡃࡆࡇࡊ࡙ࡓࡊࡄࡌࡐࡎ࡚࡙ࡠࡅࡒࡒࡋࡏࡇࡖࡔࡄࡘࡎࡕࡎࡠ࡛ࡐࡐࠬ‥"), bstack11lll1_opy_ (u"ࠬࢁࡽࠨ…")))
      parsed[bstack11lll1_opy_ (u"࠭ࡳࡤࡣࡱࡲࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧ‧")] = bstack1llll1ll1l11_opy_[bstack11lll1_opy_ (u"ࠧࡥࡣࡷࡥࠬ ")][bstack11lll1_opy_ (u"ࠨࡵࡦࡥࡳࡴࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩ ")]
      os.environ[bstack11lll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡥࡁࡄࡅࡈࡗࡘࡏࡂࡊࡎࡌࡘ࡞ࡥࡃࡐࡐࡉࡍࡌ࡛ࡒࡂࡖࡌࡓࡓࡥ࡙ࡎࡎࠪ‪")] = json.dumps(parsed)
      bstack11ll1111l_opy_.bstack11ll111111_opy_(bstack1llll1ll1l11_opy_[bstack11lll1_opy_ (u"ࠪࡨࡦࡺࡡࠨ‫")][bstack11lll1_opy_ (u"ࠫࡸࡩࡲࡪࡲࡷࡷࠬ‬")])
      bstack11ll1111l_opy_.bstack1lllll111l11_opy_(bstack1llll1ll1l11_opy_[bstack11lll1_opy_ (u"ࠬࡪࡡࡵࡣࠪ‭")][bstack11lll1_opy_ (u"࠭ࡣࡰ࡯ࡰࡥࡳࡪࡳࠨ‮")])
      bstack11ll1111l_opy_.store()
      return bstack1llll1ll1l11_opy_[bstack11lll1_opy_ (u"ࠧࡥࡣࡷࡥࠬ ")][bstack11lll1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡕࡱ࡮ࡩࡳ࠭‰")], bstack1llll1ll1l11_opy_[bstack11lll1_opy_ (u"ࠩࡧࡥࡹࡧࠧ‱")][bstack11lll1_opy_ (u"ࠪ࡭ࡩ࠭′")]
    else:
      logger.error(bstack11lll1_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡸࡪ࡬ࡰࡪࠦࡲࡶࡰࡱ࡭ࡳ࡭ࠠࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰ࠽ࠤࠬ″") + bstack1llll1ll1l11_opy_[bstack11lll1_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭‴")])
      if bstack1llll1ll1l11_opy_[bstack11lll1_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ‵")] == bstack11lll1_opy_ (u"ࠧࡊࡰࡹࡥࡱ࡯ࡤࠡࡥࡲࡲ࡫࡯ࡧࡶࡴࡤࡸ࡮ࡵ࡮ࠡࡲࡤࡷࡸ࡫ࡤ࠯ࠩ‶"):
        for bstack1llll1ll1lll_opy_ in bstack1llll1ll1l11_opy_[bstack11lll1_opy_ (u"ࠨࡧࡵࡶࡴࡸࡳࠨ‷")]:
          logger.error(bstack1llll1ll1lll_opy_[bstack11lll1_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ‸")])
      return None, None
  except Exception as error:
    logger.error(bstack11lll1_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡷࡩ࡫࡯ࡩࠥࡩࡲࡦࡣࡷ࡭ࡳ࡭ࠠࡵࡧࡶࡸࠥࡸࡵ࡯ࠢࡩࡳࡷࠦࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯࠼ࠣࠦ‹") +  str(error))
    return None, None
def bstack1llll1llllll_opy_():
  if os.getenv(bstack11lll1_opy_ (u"ࠫࡇ࡙࡟ࡂ࠳࠴࡝ࡤࡐࡗࡕࠩ›")) is None:
    return {
        bstack11lll1_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬ※"): bstack11lll1_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬ‼"),
        bstack11lll1_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ‽"): bstack11lll1_opy_ (u"ࠨࡄࡸ࡭ࡱࡪࠠࡤࡴࡨࡥࡹ࡯࡯࡯ࠢ࡫ࡥࡩࠦࡦࡢ࡫࡯ࡩࡩ࠴ࠧ‾")
    }
  data = {bstack11lll1_opy_ (u"ࠩࡨࡲࡩ࡚ࡩ࡮ࡧࠪ‿"): bstack1l1111l1_opy_()}
  headers = {
      bstack11lll1_opy_ (u"ࠪࡅࡺࡺࡨࡰࡴ࡬ࡾࡦࡺࡩࡰࡰࠪ⁀"): bstack11lll1_opy_ (u"ࠫࡇ࡫ࡡࡳࡧࡵࠤࠬ⁁") + os.getenv(bstack11lll1_opy_ (u"ࠧࡈࡓࡠࡃ࠴࠵࡞ࡥࡊࡘࡖࠥ⁂")),
      bstack11lll1_opy_ (u"࠭ࡃࡰࡰࡷࡩࡳࡺ࠭ࡕࡻࡳࡩࠬ⁃"): bstack11lll1_opy_ (u"ࠧࡢࡲࡳࡰ࡮ࡩࡡࡵ࡫ࡲࡲ࠴ࡰࡳࡰࡰࠪ⁄")
  }
  response = bstack1lll111l1l_opy_(bstack11lll1_opy_ (u"ࠨࡒࡘࡘࠬ⁅"), bstack1llll1l1l111_opy_ + bstack11lll1_opy_ (u"ࠩ࠲ࡸࡪࡹࡴࡠࡴࡸࡲࡸ࠵ࡳࡵࡱࡳࠫ⁆"), data, { bstack11lll1_opy_ (u"ࠪ࡬ࡪࡧࡤࡦࡴࡶࠫ⁇"): headers })
  try:
    if response.status_code == 200:
      logger.info(bstack11lll1_opy_ (u"ࠦࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡕࡧࡶࡸࠥࡘࡵ࡯ࠢࡰࡥࡷࡱࡥࡥࠢࡤࡷࠥࡩ࡯࡮ࡲ࡯ࡩࡹ࡫ࡤࠡࡣࡷࠤࠧ⁈") + bstack11lll1l1_opy_().isoformat() + bstack11lll1_opy_ (u"ࠬࡠࠧ⁉"))
      return {bstack11lll1_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭⁊"): bstack11lll1_opy_ (u"ࠧࡴࡷࡦࡧࡪࡹࡳࠨ⁋"), bstack11lll1_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ⁌"): bstack11lll1_opy_ (u"ࠩࠪ⁍")}
    else:
      response.raise_for_status()
  except requests.RequestException as error:
    logger.error(bstack11lll1_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡷࡩ࡫࡯ࡩࠥࡳࡡࡳ࡭࡬ࡲ࡬ࠦࡣࡰ࡯ࡳࡰࡪࡺࡩࡰࡰࠣࡳ࡫ࠦࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡗࡩࡸࡺࠠࡓࡷࡱ࠾ࠥࠨ⁎") + str(error))
    return {
        bstack11lll1_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫ⁏"): bstack11lll1_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫ⁐"),
        bstack11lll1_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ⁑"): str(error)
    }
def bstack1llll1ll1ll1_opy_(bstack1llll1lll11l_opy_):
    return re.match(bstack11lll1_opy_ (u"ࡲࠨࡠ࡟ࡨ࠰࠮࡜࠯࡞ࡧ࠯࠮ࡅࠤࠨ⁒"), bstack1llll1lll11l_opy_.strip()) is not None
def bstack1l11l1111_opy_(caps, options, desired_capabilities={}, config=None):
    try:
        if options:
          bstack1llll1l1lll1_opy_ = options.to_capabilities()
        elif desired_capabilities:
          bstack1llll1l1lll1_opy_ = desired_capabilities
        else:
          bstack1llll1l1lll1_opy_ = {}
        bstack1l111ll11l1_opy_ = (bstack1llll1l1lll1_opy_.get(bstack11lll1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡑࡥࡲ࡫ࠧ⁓"), bstack11lll1_opy_ (u"ࠩࠪ⁔")).lower() or caps.get(bstack11lll1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡓࡧ࡭ࡦࠩ⁕"), bstack11lll1_opy_ (u"ࠫࠬ⁖")).lower())
        if bstack1l111ll11l1_opy_ == bstack11lll1_opy_ (u"ࠬ࡯࡯ࡴࠩ⁗"):
            return True
        if bstack1l111ll11l1_opy_ == bstack11lll1_opy_ (u"࠭ࡡ࡯ࡦࡵࡳ࡮ࡪࠧ⁘"):
            bstack1l11111lll1_opy_ = str(float(caps.get(bstack11lll1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠩ⁙")) or bstack1llll1l1lll1_opy_.get(bstack11lll1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩ⁚"), {}).get(bstack11lll1_opy_ (u"ࠩࡲࡷ࡛࡫ࡲࡴ࡫ࡲࡲࠬ⁛"),bstack11lll1_opy_ (u"ࠪࠫ⁜"))))
            if bstack1l111ll11l1_opy_ == bstack11lll1_opy_ (u"ࠫࡦࡴࡤࡳࡱ࡬ࡨࠬ⁝") and int(bstack1l11111lll1_opy_.split(bstack11lll1_opy_ (u"ࠬ࠴ࠧ⁞"))[0]) < float(bstack11l11lll11l_opy_):
                logger.warning(str(bstack11l11l1llll_opy_))
                return False
            return True
        bstack1l111ll1111_opy_ = caps.get(bstack11lll1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧ "), {}).get(bstack11lll1_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࡎࡢ࡯ࡨࠫ⁠"), caps.get(bstack11lll1_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࠨ⁡"), bstack11lll1_opy_ (u"ࠩࠪ⁢")))
        if bstack1l111ll1111_opy_:
            logger.warning(bstack11lll1_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡸ࡫࡯ࡰࠥࡸࡵ࡯ࠢࡲࡲࡱࡿࠠࡰࡰࠣࡈࡪࡹ࡫ࡵࡱࡳࠤࡧࡸ࡯ࡸࡵࡨࡶࡸ࠴ࠢ⁣"))
            return False
        browser = caps.get(bstack11lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩ⁤"), bstack11lll1_opy_ (u"ࠬ࠭⁥")).lower() or bstack1llll1l1lll1_opy_.get(bstack11lll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫ⁦"), bstack11lll1_opy_ (u"ࠧࠨ⁧")).lower()
        if browser != bstack11lll1_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࠨ⁨"):
            logger.warning(bstack11lll1_opy_ (u"ࠤࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡷࡪ࡮࡯ࠤࡷࡻ࡮ࠡࡱࡱࡰࡾࠦ࡯࡯ࠢࡆ࡬ࡷࡵ࡭ࡦࠢࡥࡶࡴࡽࡳࡦࡴࡶ࠲ࠧ⁩"))
            return False
        browser_version = caps.get(bstack11lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫ⁪")) or caps.get(bstack11lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭⁫")) or bstack1llll1l1lll1_opy_.get(bstack11lll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭⁬")) or bstack1llll1l1lll1_opy_.get(bstack11lll1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧ⁭"), {}).get(bstack11lll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨ⁮")) or bstack1llll1l1lll1_opy_.get(bstack11lll1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩ⁯"), {}).get(bstack11lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡺࡪࡸࡳࡪࡱࡱࠫ⁰"))
        bstack1l111l1ll11_opy_ = bstack1llll1llll11_opy_.bstack1l111l111ll_opy_
        bstack1llll1ll1111_opy_ = False
        if config is not None:
          bstack1llll1ll1111_opy_ = bstack11lll1_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧⁱ") in config and str(config[bstack11lll1_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨ⁲")]).lower() != bstack11lll1_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫ⁳")
        if os.environ.get(bstack11lll1_opy_ (u"࠭ࡉࡔࡡࡑࡓࡓࡥࡂࡔࡖࡄࡇࡐࡥࡉࡏࡈࡕࡅࡤࡇ࠱࠲࡛ࡢࡗࡊ࡙ࡓࡊࡑࡑࠫ⁴"), bstack11lll1_opy_ (u"ࠧࠨ⁵")).lower() == bstack11lll1_opy_ (u"ࠨࡶࡵࡹࡪ࠭⁶") or bstack1llll1ll1111_opy_:
          bstack1l111l1ll11_opy_ = bstack1llll1llll11_opy_.bstack1l11111ll11_opy_
        if browser_version and browser_version != bstack11lll1_opy_ (u"ࠩ࡯ࡥࡹ࡫ࡳࡵࠩ⁷") and int(browser_version.split(bstack11lll1_opy_ (u"ࠪ࠲ࠬ⁸"))[0]) <= bstack1l111l1ll11_opy_:
          logger.warning(bstack1lll1ll1111_opy_ (u"ࠫࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡹ࡬ࡰࡱࠦࡲࡶࡰࠣࡳࡳࡲࡹࠡࡱࡱࠤࡈ࡮ࡲࡰ࡯ࡨࠤࡧࡸ࡯ࡸࡵࡨࡶࠥࡼࡥࡳࡵ࡬ࡳࡳࠦࡧࡳࡧࡤࡸࡪࡸࠠࡵࡪࡤࡲࠥࢁ࡭ࡪࡰࡢࡥ࠶࠷ࡹࡠࡵࡸࡴࡵࡵࡲࡵࡧࡧࡣࡨ࡮ࡲࡰ࡯ࡨࡣࡻ࡫ࡲࡴ࡫ࡲࡲࢂ࠴ࠧ⁹"))
          return False
        if not options:
          bstack1l111l1l1l1_opy_ = caps.get(bstack11lll1_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ⁺")) or bstack1llll1l1lll1_opy_.get(bstack11lll1_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫ⁻"), {})
          if bstack11lll1_opy_ (u"ࠧ࠮࠯࡫ࡩࡦࡪ࡬ࡦࡵࡶࠫ⁼") in bstack1l111l1l1l1_opy_.get(bstack11lll1_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭⁽"), []):
              logger.warning(bstack11lll1_opy_ (u"ࠤࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡷࡪ࡮࡯ࠤࡳࡵࡴࠡࡴࡸࡲࠥࡵ࡮ࠡ࡮ࡨ࡫ࡦࡩࡹࠡࡪࡨࡥࡩࡲࡥࡴࡵࠣࡱࡴࡪࡥ࠯ࠢࡖࡻ࡮ࡺࡣࡩࠢࡷࡳࠥࡴࡥࡸࠢ࡫ࡩࡦࡪ࡬ࡦࡵࡶࠤࡲࡵࡤࡦࠢࡲࡶࠥࡧࡶࡰ࡫ࡧࠤࡺࡹࡩ࡯ࡩࠣ࡬ࡪࡧࡤ࡭ࡧࡶࡷࠥࡳ࡯ࡥࡧ࠱ࠦ⁾"))
              return False
        return True
    except Exception as error:
        logger.debug(bstack11lll1_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡹࡥࡱ࡯ࡤࡢࡶࡨࠤࡦ࠷࠱ࡺࠢࡶࡹࡵࡶ࡯ࡳࡶࠣ࠾ࠧⁿ") + str(error))
        return False
def set_capabilities(caps, config):
  try:
    bstack1l1l1lllll1_opy_ = config.get(bstack11lll1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫ₀"), {})
    bstack1l1l1lllll1_opy_[bstack11lll1_opy_ (u"ࠬࡧࡵࡵࡪࡗࡳࡰ࡫࡮ࠨ₁")] = os.getenv(bstack11lll1_opy_ (u"࠭ࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗࠫ₂"))
    bstack1111l1l11l1_opy_ = json.loads(os.getenv(bstack11lll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡣࡆࡉࡃࡆࡕࡖࡍࡇࡏࡌࡊࡖ࡜ࡣࡈࡕࡎࡇࡋࡊ࡙ࡗࡇࡔࡊࡑࡑࡣ࡞ࡓࡌࠨ₃"), bstack11lll1_opy_ (u"ࠨࡽࢀࠫ₄"))).get(bstack11lll1_opy_ (u"ࠩࡶࡧࡦࡴ࡮ࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪ₅"))
    if not config[bstack11lll1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡒࡵࡳࡩࡻࡣࡵࡏࡤࡴࠬ₆")].get(bstack11lll1_opy_ (u"ࠦࡦࡶࡰࡠࡣࡸࡸࡴࡳࡡࡵࡧࠥ₇")):
      if bstack11lll1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭₈") in caps:
        caps[bstack11lll1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧ₉")][bstack11lll1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧ₊")] = bstack1l1l1lllll1_opy_
        caps[bstack11lll1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩ₋")][bstack11lll1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩ₌")][bstack11lll1_opy_ (u"ࠪࡷࡨࡧ࡮࡯ࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫ₍")] = bstack1111l1l11l1_opy_
      else:
        caps[bstack11lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪ₎")] = bstack1l1l1lllll1_opy_
        caps[bstack11lll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫ₏")][bstack11lll1_opy_ (u"࠭ࡳࡤࡣࡱࡲࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧₐ")] = bstack1111l1l11l1_opy_
  except Exception as error:
    logger.debug(bstack11lll1_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡻ࡭࡯࡬ࡦࠢࡶࡩࡹࡺࡩ࡯ࡩࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠴ࠠࡆࡴࡵࡳࡷࡀࠠࠣₑ") +  str(error))
def bstack1l11ll1l1_opy_(driver, bstack1llll1lll111_opy_):
  try:
    setattr(driver, bstack11lll1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡂ࠳࠴ࡽࡘ࡮࡯ࡶ࡮ࡧࡗࡨࡧ࡮ࠨₒ"), True)
    session = driver.session_id
    if session:
      bstack1llll1l1l1ll_opy_ = True
      current_url = driver.current_url
      try:
        url = urlparse(current_url)
      except Exception as e:
        bstack1llll1l1l1ll_opy_ = False
      bstack1llll1l1l1ll_opy_ = url.scheme in [bstack11lll1_opy_ (u"ࠤ࡫ࡸࡹࡶࠢₓ"), bstack11lll1_opy_ (u"ࠥ࡬ࡹࡺࡰࡴࠤₔ")]
      if bstack1llll1l1l1ll_opy_:
        if bstack1llll1lll111_opy_:
          logger.info(bstack11lll1_opy_ (u"ࠦࡘ࡫ࡴࡶࡲࠣࡪࡴࡸࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡵࡧࡶࡸ࡮ࡴࡧࠡࡪࡤࡷࠥࡹࡴࡢࡴࡷࡩࡩ࠴ࠠࡂࡷࡷࡳࡲࡧࡴࡦࠢࡷࡩࡸࡺࠠࡤࡣࡶࡩࠥ࡫ࡸࡦࡥࡸࡸ࡮ࡵ࡮ࠡࡹ࡬ࡰࡱࠦࡢࡦࡩ࡬ࡲࠥࡳ࡯࡮ࡧࡱࡸࡦࡸࡩ࡭ࡻ࠱ࠦₕ"))
      return bstack1llll1lll111_opy_
  except Exception as e:
    logger.error(bstack11lll1_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡸࡺࡡࡳࡶ࡬ࡲ࡬ࠦࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡷࡨࡧ࡮ࠡࡨࡲࡶࠥࡺࡨࡪࡵࠣࡸࡪࡹࡴࠡࡥࡤࡷࡪࡀࠠࠣₖ") + str(e))
    return False
def bstack1lll1lll1_opy_(driver, name, path):
  try:
    bstack1l111ll11ll_opy_ = {
        bstack11lll1_opy_ (u"࠭ࡴࡩࡖࡨࡷࡹࡘࡵ࡯ࡗࡸ࡭ࡩ࠭ₗ"): threading.current_thread().current_test_uuid,
        bstack11lll1_opy_ (u"ࠧࡵࡪࡅࡹ࡮ࡲࡤࡖࡷ࡬ࡨࠬₘ"): os.environ.get(bstack11lll1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭ₙ"), bstack11lll1_opy_ (u"ࠩࠪₚ")),
        bstack11lll1_opy_ (u"ࠪࡸ࡭ࡐࡷࡵࡖࡲ࡯ࡪࡴࠧₛ"): os.environ.get(bstack11lll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨₜ"), bstack11lll1_opy_ (u"ࠬ࠭₝"))
    }
    bstack1ll1l1111ll_opy_ = bstack1111l111l1_opy_.bstack1ll11111l1l_opy_(EVENTS.bstack111ll1l111_opy_.value)
    logger.debug(bstack11lll1_opy_ (u"࠭ࡐࡦࡴࡩࡳࡷࡳࡩ࡯ࡩࠣࡷࡨࡧ࡮ࠡࡤࡨࡪࡴࡸࡥࠡࡵࡤࡺ࡮ࡴࡧࠡࡴࡨࡷࡺࡲࡴࡴࠩ₞"))
    try:
      if (bstack1lll111l_opy_(threading.current_thread(), bstack11lll1_opy_ (u"ࠧࡪࡵࡄࡴࡵࡇ࠱࠲ࡻࡗࡩࡸࡺࠧ₟"), None) and bstack1lll111l_opy_(threading.current_thread(), bstack11lll1_opy_ (u"ࠨࡣࡳࡴࡆ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪ₠"), None)):
        scripts = {bstack11lll1_opy_ (u"ࠩࡶࡧࡦࡴࠧ₡"): bstack11ll1111l_opy_.perform_scan}
        bstack1llll1lll1ll_opy_ = json.loads(scripts[bstack11lll1_opy_ (u"ࠥࡷࡨࡧ࡮ࠣ₢")].replace(bstack11lll1_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࠢ₣"), bstack11lll1_opy_ (u"ࠧࠨ₤")))
        bstack1llll1lll1ll_opy_[bstack11lll1_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩ₥")][bstack11lll1_opy_ (u"ࠧ࡮ࡧࡷ࡬ࡴࡪࠧ₦")] = None
        scripts[bstack11lll1_opy_ (u"ࠣࡵࡦࡥࡳࠨ₧")] = bstack11lll1_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࠧ₨") + json.dumps(bstack1llll1lll1ll_opy_)
        bstack11ll1111l_opy_.bstack11ll111111_opy_(scripts)
        bstack11ll1111l_opy_.store()
        logger.debug(driver.execute_script(bstack11ll1111l_opy_.perform_scan))
      else:
        logger.debug(driver.execute_async_script(bstack11ll1111l_opy_.perform_scan, {bstack11lll1_opy_ (u"ࠥࡱࡪࡺࡨࡰࡦࠥ₩"): name}))
      bstack1111l111l1_opy_.end(EVENTS.bstack111ll1l111_opy_.value, bstack1ll1l1111ll_opy_ + bstack11lll1_opy_ (u"ࠦ࠿ࡹࡴࡢࡴࡷࠦ₪"), bstack1ll1l1111ll_opy_ + bstack11lll1_opy_ (u"ࠧࡀࡥ࡯ࡦࠥ₫"), True, None)
    except Exception as error:
      bstack1111l111l1_opy_.end(EVENTS.bstack111ll1l111_opy_.value, bstack1ll1l1111ll_opy_ + bstack11lll1_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨ€"), bstack1ll1l1111ll_opy_ + bstack11lll1_opy_ (u"ࠢ࠻ࡧࡱࡨࠧ₭"), False, str(error))
    bstack1ll1l1111ll_opy_ = bstack1111l111l1_opy_.bstack11ll1l11lll_opy_(EVENTS.bstack1l1111l1l11_opy_.value)
    bstack1111l111l1_opy_.mark(bstack1ll1l1111ll_opy_ + bstack11lll1_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣ₮"))
    try:
      if (bstack1lll111l_opy_(threading.current_thread(), bstack11lll1_opy_ (u"ࠩ࡬ࡷࡆࡶࡰࡂ࠳࠴ࡽ࡙࡫ࡳࡵࠩ₯"), None) and bstack1lll111l_opy_(threading.current_thread(), bstack11lll1_opy_ (u"ࠪࡥࡵࡶࡁ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬ₰"), None)):
        scripts = {bstack11lll1_opy_ (u"ࠫࡸࡩࡡ࡯ࠩ₱"): bstack11ll1111l_opy_.perform_scan}
        bstack1llll1lll1ll_opy_ = json.loads(scripts[bstack11lll1_opy_ (u"ࠧࡹࡣࡢࡰࠥ₲")].replace(bstack11lll1_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࠤ₳"), bstack11lll1_opy_ (u"ࠢࠣ₴")))
        bstack1llll1lll1ll_opy_[bstack11lll1_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫ₵")][bstack11lll1_opy_ (u"ࠩࡰࡩࡹ࡮࡯ࡥࠩ₶")] = None
        scripts[bstack11lll1_opy_ (u"ࠥࡷࡨࡧ࡮ࠣ₷")] = bstack11lll1_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࠢ₸") + json.dumps(bstack1llll1lll1ll_opy_)
        bstack11ll1111l_opy_.bstack11ll111111_opy_(scripts)
        bstack11ll1111l_opy_.store()
        logger.debug(driver.execute_script(bstack11ll1111l_opy_.perform_scan))
      else:
        logger.debug(driver.execute_async_script(bstack11ll1111l_opy_.bstack1lllll111ll1_opy_, bstack1l111ll11ll_opy_))
      bstack1111l111l1_opy_.end(bstack1ll1l1111ll_opy_, bstack1ll1l1111ll_opy_ + bstack11lll1_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧ₹"), bstack1ll1l1111ll_opy_ + bstack11lll1_opy_ (u"ࠨ࠺ࡦࡰࡧࠦ₺"),True, None)
    except Exception as error:
      bstack1111l111l1_opy_.end(bstack1ll1l1111ll_opy_, bstack1ll1l1111ll_opy_ + bstack11lll1_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢ₻"), bstack1ll1l1111ll_opy_ + bstack11lll1_opy_ (u"ࠣ࠼ࡨࡲࡩࠨ₼"),False, str(error))
    logger.info(bstack11lll1_opy_ (u"ࠤࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡷࡩࡸࡺࡩ࡯ࡩࠣࡪࡴࡸࠠࡵࡪ࡬ࡷࠥࡺࡥࡴࡶࠣࡧࡦࡹࡥࠡࡪࡤࡷࠥ࡫࡮ࡥࡧࡧ࠲ࠧ₽"))
  except Exception as bstack1l111l1l111_opy_:
    logger.error(bstack11lll1_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡶࡪࡹࡵ࡭ࡶࡶࠤࡨࡵࡵ࡭ࡦࠣࡲࡴࡺࠠࡣࡧࠣࡴࡷࡵࡣࡦࡵࡶࡩࡩࠦࡦࡰࡴࠣࡸ࡭࡫ࠠࡵࡧࡶࡸࠥࡩࡡࡴࡧ࠽ࠤࠧ₾") + str(path) + bstack11lll1_opy_ (u"ࠦࠥࡋࡲࡳࡱࡵࠤ࠿ࠨ₿") + str(bstack1l111l1l111_opy_))
def bstack1lllll111111_opy_(driver):
    caps = driver.capabilities
    if caps.get(bstack11lll1_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࡎࡢ࡯ࡨࠦ⃀")) and str(caps.get(bstack11lll1_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡏࡣࡰࡩࠧ⃁"))).lower() == bstack11lll1_opy_ (u"ࠢࡢࡰࡧࡶࡴ࡯ࡤࠣ⃂"):
        bstack1l11111lll1_opy_ = caps.get(bstack11lll1_opy_ (u"ࠣࡣࡳࡴ࡮ࡻ࡭࠻ࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࡙ࡩࡷࡹࡩࡰࡰࠥ⃃")) or caps.get(bstack11lll1_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰ࡚ࡪࡸࡳࡪࡱࡱࠦ⃄"))
        if bstack1l11111lll1_opy_ and int(str(bstack1l11111lll1_opy_)) < bstack11l11lll11l_opy_:
            return False
    return True
def bstack11lll1lll_opy_(config):
  if bstack11lll1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ⃅") in config:
        return config[bstack11lll1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ⃆")]
  for platform in config.get(bstack11lll1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ⃇"), []):
      if bstack11lll1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭⃈") in platform:
          return platform[bstack11lll1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ⃉")]
  return None
def bstack11l1ll11l_opy_(bstack1ll1ll1l1l_opy_):
  try:
    browser_name = bstack1ll1ll1l1l_opy_[bstack11lll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡱࡥࡲ࡫ࠧ⃊")]
    browser_version = bstack1ll1ll1l1l_opy_[bstack11lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡺࡪࡸࡳࡪࡱࡱࠫ⃋")]
    chrome_options = bstack1ll1ll1l1l_opy_[bstack11lll1_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧࡢࡳࡵࡺࡩࡰࡰࡶࠫ⃌")]
    try:
        bstack1llll1l1ll11_opy_ = int(browser_version.split(bstack11lll1_opy_ (u"ࠫ࠳࠭⃍"))[0])
    except ValueError as e:
        logger.error(bstack11lll1_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡧࡴࡴࡶࡦࡴࡷ࡭ࡳ࡭ࠠࡣࡴࡲࡻࡸ࡫ࡲࠡࡸࡨࡶࡸ࡯࡯࡯ࠤ⃎") + str(e))
        return False
    if not (browser_name and browser_name.lower() == bstack11lll1_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪ࠭⃏")):
        logger.warning(bstack11lll1_opy_ (u"ࠢࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡼ࡯࡬࡭ࠢࡵࡹࡳࠦ࡯࡯࡮ࡼࠤࡴࡴࠠࡄࡪࡵࡳࡲ࡫ࠠࡣࡴࡲࡻࡸ࡫ࡲࡴ࠰ࠥ⃐"))
        return False
    if bstack1llll1l1ll11_opy_ < bstack1llll1llll11_opy_.bstack1l11111ll11_opy_:
        logger.warning(bstack1lll1ll1111_opy_ (u"ࠨࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡸࡥࡲࡷ࡬ࡶࡪࡹࠠࡄࡪࡵࡳࡲ࡫ࠠࡷࡧࡵࡷ࡮ࡵ࡮ࠡࡽࡆࡓࡓ࡙ࡔࡂࡐࡗࡗ࠳ࡓࡉࡏࡋࡐ࡙ࡒࡥࡎࡐࡐࡢࡆࡘ࡚ࡁࡄࡍࡢࡍࡓࡌࡒࡂࡡࡄ࠵࠶࡟࡟ࡔࡗࡓࡔࡔࡘࡔࡆࡆࡢࡇࡍࡘࡏࡎࡇࡢ࡚ࡊࡘࡓࡊࡑࡑࢁࠥࡵࡲࠡࡪ࡬࡫࡭࡫ࡲ࠯ࠩ⃑"))
        return False
    if chrome_options and any(bstack11lll1_opy_ (u"ࠩ࠰࠱࡭࡫ࡡࡥ࡮ࡨࡷࡸ⃒࠭") in value for value in chrome_options.values() if isinstance(value, str)):
        logger.warning(bstack11lll1_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡸ࡫࡯ࡰࠥࡴ࡯ࡵࠢࡵࡹࡳࠦ࡯࡯ࠢ࡯ࡩ࡬ࡧࡣࡺࠢ࡫ࡩࡦࡪ࡬ࡦࡵࡶࠤࡲࡵࡤࡦ࠰ࠣࡗࡼ࡯ࡴࡤࡪࠣࡸࡴࠦ࡮ࡦࡹࠣ࡬ࡪࡧࡤ࡭ࡧࡶࡷࠥࡳ࡯ࡥࡧࠣࡳࡷࠦࡡࡷࡱ࡬ࡨࠥࡻࡳࡪࡰࡪࠤ࡭࡫ࡡࡥ࡮ࡨࡷࡸࠦ࡭ࡰࡦࡨ࠲⃓ࠧ"))
        return False
    return True
  except Exception as e:
    logger.error(bstack11lll1_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡣࡩࡧࡦ࡯࡮ࡴࡧࠡࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࠣࡷࡺࡶࡰࡰࡴࡷࠤ࡫ࡵࡲࠡ࡮ࡲࡧࡦࡲࠠࡄࡪࡵࡳࡲ࡫࠺ࠡࠤ⃔") + str(e))
    return False
def bstack111lll1ll_opy_(bstack11l1l111l1_opy_, config):
    try:
      bstack1l111l1l11l_opy_ = bstack11lll1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ⃕") in config and config[bstack11lll1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭⃖")] == True
      bstack1llll1ll1111_opy_ = bstack11lll1_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫ⃗") in config and str(config[bstack11lll1_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩ⃘ࠬ")]).lower() != bstack11lll1_opy_ (u"ࠩࡩࡥࡱࡹࡥࠨ⃙")
      if not (bstack1l111l1l11l_opy_ and (not bstack11l1l1ll1l_opy_(config) or bstack1llll1ll1111_opy_)):
        return bstack11l1l111l1_opy_
      bstack1lllll1111ll_opy_ = bstack11ll1111l_opy_.bstack1lllll11l1l1_opy_
      if bstack1lllll1111ll_opy_ is None:
        logger.debug(bstack11lll1_opy_ (u"ࠥࡋࡴࡵࡧ࡭ࡧࠣࡧ࡭ࡸ࡯࡮ࡧࠣࡳࡵࡺࡩࡰࡰࡶࠤࡦࡸࡥࠡࡐࡲࡲࡪࠨ⃚"))
        return bstack11l1l111l1_opy_
      bstack1lllll11111l_opy_ = int(str(bstack111l1ll1l1l_opy_()).split(bstack11lll1_opy_ (u"ࠫ࠳࠭⃛"))[0])
      logger.debug(bstack11lll1_opy_ (u"࡙ࠧࡥ࡭ࡧࡱ࡭ࡺࡳࠠࡷࡧࡵࡷ࡮ࡵ࡮ࠡࡦࡨࡸࡪࡩࡴࡦࡦ࠽ࠤࠧ⃜") + str(bstack1lllll11111l_opy_) + bstack11lll1_opy_ (u"ࠨࠢ⃝"))
      if bstack1lllll11111l_opy_ == 3 and isinstance(bstack11l1l111l1_opy_, dict) and bstack11lll1_opy_ (u"ࠧࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠧ⃞") in bstack11l1l111l1_opy_ and bstack1lllll1111ll_opy_ is not None:
        if bstack11lll1_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭⃟") not in bstack11l1l111l1_opy_[bstack11lll1_opy_ (u"ࠩࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩ⃠")]:
          bstack11l1l111l1_opy_[bstack11lll1_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪ⃡")][bstack11lll1_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩ⃢")] = {}
        if bstack11lll1_opy_ (u"ࠬࡧࡲࡨࡵࠪ⃣") in bstack1lllll1111ll_opy_:
          if bstack11lll1_opy_ (u"࠭ࡡࡳࡩࡶࠫ⃤") not in bstack11l1l111l1_opy_[bstack11lll1_opy_ (u"ࠧࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹ⃥ࠧ")][bstack11lll1_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ⃦࠭")]:
            bstack11l1l111l1_opy_[bstack11lll1_opy_ (u"ࠩࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩ⃧")][bstack11lll1_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨ⃨")][bstack11lll1_opy_ (u"ࠫࡦࡸࡧࡴࠩ⃩")] = []
          for arg in bstack1lllll1111ll_opy_[bstack11lll1_opy_ (u"ࠬࡧࡲࡨࡵ⃪ࠪ")]:
            if arg not in bstack11l1l111l1_opy_[bstack11lll1_opy_ (u"࠭ࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ⃫࠭")][bstack11lll1_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷ⃬ࠬ")][bstack11lll1_opy_ (u"ࠨࡣࡵ࡫ࡸ⃭࠭")]:
              bstack11l1l111l1_opy_[bstack11lll1_opy_ (u"ࠩࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴ⃮ࠩ")][bstack11lll1_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨ⃯")][bstack11lll1_opy_ (u"ࠫࡦࡸࡧࡴࠩ⃰")].append(arg)
        if bstack11lll1_opy_ (u"ࠬ࡫ࡸࡵࡧࡱࡷ࡮ࡵ࡮ࡴࠩ⃱") in bstack1lllll1111ll_opy_:
          if bstack11lll1_opy_ (u"࠭ࡥࡹࡶࡨࡲࡸ࡯࡯࡯ࡵࠪ⃲") not in bstack11l1l111l1_opy_[bstack11lll1_opy_ (u"ࠧࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠧ⃳")][bstack11lll1_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭⃴")]:
            bstack11l1l111l1_opy_[bstack11lll1_opy_ (u"ࠩࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩ⃵")][bstack11lll1_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨ⃶")][bstack11lll1_opy_ (u"ࠫࡪࡾࡴࡦࡰࡶ࡭ࡴࡴࡳࠨ⃷")] = []
          for ext in bstack1lllll1111ll_opy_[bstack11lll1_opy_ (u"ࠬ࡫ࡸࡵࡧࡱࡷ࡮ࡵ࡮ࡴࠩ⃸")]:
            if ext not in bstack11l1l111l1_opy_[bstack11lll1_opy_ (u"࠭ࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠭⃹")][bstack11lll1_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬ⃺")][bstack11lll1_opy_ (u"ࠨࡧࡻࡸࡪࡴࡳࡪࡱࡱࡷࠬ⃻")]:
              bstack11l1l111l1_opy_[bstack11lll1_opy_ (u"ࠩࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩ⃼")][bstack11lll1_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨ⃽")][bstack11lll1_opy_ (u"ࠫࡪࡾࡴࡦࡰࡶ࡭ࡴࡴࡳࠨ⃾")].append(ext)
        if bstack11lll1_opy_ (u"ࠬࡶࡲࡦࡨࡶࠫ⃿") in bstack1lllll1111ll_opy_:
          if bstack11lll1_opy_ (u"࠭ࡰࡳࡧࡩࡷࠬ℀") not in bstack11l1l111l1_opy_[bstack11lll1_opy_ (u"ࠧࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠧ℁")][bstack11lll1_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ℂ")]:
            bstack11l1l111l1_opy_[bstack11lll1_opy_ (u"ࠩࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩ℃")][bstack11lll1_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨ℄")][bstack11lll1_opy_ (u"ࠫࡵࡸࡥࡧࡵࠪ℅")] = {}
          bstack1111ll1ll11_opy_(bstack11l1l111l1_opy_[bstack11lll1_opy_ (u"ࠬࡪࡥࡴ࡫ࡵࡩࡩࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠬ℆")][bstack11lll1_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫℇ")][bstack11lll1_opy_ (u"ࠧࡱࡴࡨࡪࡸ࠭℈")],
                    bstack1lllll1111ll_opy_[bstack11lll1_opy_ (u"ࠨࡲࡵࡩ࡫ࡹࠧ℉")])
        os.environ[bstack11lll1_opy_ (u"ࠩࡌࡗࡤࡔࡏࡏࡡࡅࡗ࡙ࡇࡃࡌࡡࡌࡒࡋࡘࡁࡠࡃ࠴࠵࡞ࡥࡓࡆࡕࡖࡍࡔࡔࠧℊ")] = bstack11lll1_opy_ (u"ࠪࡸࡷࡻࡥࠨℋ")
        return bstack11l1l111l1_opy_
      else:
        chrome_options = None
        if isinstance(bstack11l1l111l1_opy_, ChromeOptions):
          chrome_options = bstack11l1l111l1_opy_
        elif isinstance(bstack11l1l111l1_opy_, dict):
          for value in bstack11l1l111l1_opy_.values():
            if isinstance(value, ChromeOptions):
              chrome_options = value
              break
        if chrome_options is None:
          chrome_options = ChromeOptions()
          if isinstance(bstack11l1l111l1_opy_, dict):
            bstack11l1l111l1_opy_[bstack11lll1_opy_ (u"ࠫࡴࡶࡴࡪࡱࡱࡷࠬℌ")] = chrome_options
          else:
            bstack11l1l111l1_opy_ = chrome_options
        if bstack1lllll1111ll_opy_ is not None:
          if bstack11lll1_opy_ (u"ࠬࡧࡲࡨࡵࠪℍ") in bstack1lllll1111ll_opy_:
                bstack1llll1ll111l_opy_ = chrome_options.arguments or []
                new_args = bstack1lllll1111ll_opy_[bstack11lll1_opy_ (u"࠭ࡡࡳࡩࡶࠫℎ")]
                for arg in new_args:
                    if arg not in bstack1llll1ll111l_opy_:
                        chrome_options.add_argument(arg)
          if bstack11lll1_opy_ (u"ࠧࡦࡺࡷࡩࡳࡹࡩࡰࡰࡶࠫℏ") in bstack1lllll1111ll_opy_:
                existing_extensions = chrome_options.experimental_options.get(bstack11lll1_opy_ (u"ࠨࡧࡻࡸࡪࡴࡳࡪࡱࡱࡷࠬℐ"), [])
                bstack1llll1l11lll_opy_ = bstack1lllll1111ll_opy_[bstack11lll1_opy_ (u"ࠩࡨࡼࡹ࡫࡮ࡴ࡫ࡲࡲࡸ࠭ℑ")]
                for extension in bstack1llll1l11lll_opy_:
                    if extension not in existing_extensions:
                        chrome_options.add_encoded_extension(extension)
          if bstack11lll1_opy_ (u"ࠪࡴࡷ࡫ࡦࡴࠩℒ") in bstack1lllll1111ll_opy_:
                bstack1llll1ll1l1l_opy_ = chrome_options.experimental_options.get(bstack11lll1_opy_ (u"ࠫࡵࡸࡥࡧࡵࠪℓ"), {})
                bstack1llll1ll11ll_opy_ = bstack1lllll1111ll_opy_[bstack11lll1_opy_ (u"ࠬࡶࡲࡦࡨࡶࠫ℔")]
                bstack1111ll1ll11_opy_(bstack1llll1ll1l1l_opy_, bstack1llll1ll11ll_opy_)
                chrome_options.add_experimental_option(bstack11lll1_opy_ (u"࠭ࡰࡳࡧࡩࡷࠬℕ"), bstack1llll1ll1l1l_opy_)
        os.environ[bstack11lll1_opy_ (u"ࠧࡊࡕࡢࡒࡔࡔ࡟ࡃࡕࡗࡅࡈࡑ࡟ࡊࡐࡉࡖࡆࡥࡁ࠲࠳࡜ࡣࡘࡋࡓࡔࡋࡒࡒࠬ№")] = bstack11lll1_opy_ (u"ࠨࡶࡵࡹࡪ࠭℗")
        return bstack11l1l111l1_opy_
    except Exception as e:
      logger.error(bstack11lll1_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡹ࡫࡭ࡱ࡫ࠠࡢࡦࡧ࡭ࡳ࡭ࠠ࡯ࡱࡱ࠱ࡇ࡙ࠠࡪࡰࡩࡶࡦࠦࡡ࠲࠳ࡼࠤࡨ࡮ࡲࡰ࡯ࡨࠤࡴࡶࡴࡪࡱࡱࡷ࠿ࠦࠢ℘") + str(e))
      return bstack11l1l111l1_opy_