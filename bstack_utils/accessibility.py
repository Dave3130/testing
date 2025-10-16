# coding: UTF-8
import sys
bstack1llllll_opy_ = sys.version_info [0] == 2
bstack11l1l1l_opy_ = 2048
bstack1111ll_opy_ = 7
def bstack1lllll1_opy_ (bstack1l1_opy_):
    global bstack111ll11_opy_
    bstackl_opy_ = ord (bstack1l1_opy_ [-1])
    bstack1l1l_opy_ = bstack1l1_opy_ [:-1]
    bstack111ll_opy_ = bstackl_opy_ % len (bstack1l1l_opy_)
    bstack111l_opy_ = bstack1l1l_opy_ [:bstack111ll_opy_] + bstack1l1l_opy_ [bstack111ll_opy_:]
    if bstack1llllll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
import os
import json
import requests
import logging
import threading
import bstack_utils.constants as bstack1lllll111111_opy_
from urllib.parse import urlparse
from bstack_utils.constants import bstack11l1l1111l1_opy_ as bstack1lllll111lll_opy_, EVENTS
from bstack_utils.bstack1llll11l11_opy_ import bstack1llll11l11_opy_
from bstack_utils.helper import bstack1llll11l_opy_, bstack1l1ll1l1_opy_, bstack11ll11111_opy_, bstack111l1111l1l_opy_, \
  bstack1111ll1ll11_opy_, bstack1ll111111l_opy_, get_host_info, bstack111l1llll1l_opy_, bstack1l1111111_opy_, error_handler, bstack111l1l1l1ll_opy_, bstack1111l1ll11l_opy_, bstack1lll1l11_opy_
from browserstack_sdk._version import __version__
from bstack_utils.bstack1ll11111l1_opy_ import get_logger
from bstack_utils.bstack11l11l1111_opy_ import bstack1lllllllll1_opy_
from selenium.webdriver.chrome.options import Options as ChromeOptions
from browserstack_sdk.sdk_cli.cli import cli
from bstack_utils.constants import *
logger = get_logger(__name__)
bstack11l11l1111_opy_ = bstack1lllllllll1_opy_()
@error_handler(class_method=False)
def _1lllll11l1l1_opy_(driver, bstack111llll1_opy_):
  response = {}
  try:
    caps = driver.capabilities
    response = {
        bstack1lllll1_opy_ (u"ࠨࡱࡶࡣࡳࡧ࡭ࡦࠩῇ"): caps.get(bstack1lllll1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡒࡦࡳࡥࠨῈ"), None),
        bstack1lllll1_opy_ (u"ࠪࡳࡸࡥࡶࡦࡴࡶ࡭ࡴࡴࠧΈ"): bstack111llll1_opy_.get(bstack1lllll1_opy_ (u"ࠫࡴࡹࡖࡦࡴࡶ࡭ࡴࡴࠧῊ"), None),
        bstack1lllll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡥ࡮ࡢ࡯ࡨࠫΉ"): caps.get(bstack1lllll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫῌ"), None),
        bstack1lllll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡸࡨࡶࡸ࡯࡯࡯ࠩ῍"): caps.get(bstack1lllll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩ῎"), None)
    }
  except Exception as error:
    logger.debug(bstack1lllll1_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡨࡨࡸࡨ࡮ࡩ࡯ࡩࠣࡴࡱࡧࡴࡧࡱࡵࡱࠥࡪࡥࡵࡣ࡬ࡰࡸࠦࡷࡪࡶ࡫ࠤࡪࡸࡲࡰࡴࠣ࠾ࠥ࠭῏") + str(error))
  return response
def on():
    if os.environ.get(bstack1lllll1_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨῐ"), None) is None or os.environ[bstack1lllll1_opy_ (u"ࠫࡇ࡙࡟ࡂ࠳࠴࡝ࡤࡐࡗࡕࠩῑ")] == bstack1lllll1_opy_ (u"ࠧࡴࡵ࡭࡮ࠥῒ"):
        return False
    return True
def bstack1l1lllll1_opy_(config):
  return config.get(bstack1lllll1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ΐ"), False) or any([p.get(bstack1lllll1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ῔"), False) == True for p in config.get(bstack1lllll1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ῕"), [])])
def bstack1l111lll1_opy_(config, bstack1l11l111l_opy_):
  try:
    bstack1lllll1111ll_opy_ = config.get(bstack1lllll1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩῖ"), False)
    if int(bstack1l11l111l_opy_) < len(config.get(bstack1lllll1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ῗ"), [])) and config[bstack1lllll1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧῘ")][bstack1l11l111l_opy_]:
      bstack1llll1ll1l1l_opy_ = config[bstack1lllll1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨῙ")][bstack1l11l111l_opy_].get(bstack1lllll1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭Ὶ"), None)
    else:
      bstack1llll1ll1l1l_opy_ = config.get(bstack1lllll1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧΊ"), None)
    if bstack1llll1ll1l1l_opy_ != None:
      bstack1lllll1111ll_opy_ = bstack1llll1ll1l1l_opy_
    bstack1llll1ll1ll1_opy_ = os.getenv(bstack1lllll1_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭῜")) is not None and len(os.getenv(bstack1lllll1_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧ῝"))) > 0 and os.getenv(bstack1lllll1_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨ῞")) != bstack1lllll1_opy_ (u"ࠫࡳࡻ࡬࡭ࠩ῟")
    return bstack1lllll1111ll_opy_ and bstack1llll1ll1ll1_opy_
  except Exception as error:
    logger.debug(bstack1lllll1_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡻ࡫ࡲࡪࡨࡼ࡭ࡳ࡭ࠠࡵࡪࡨࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡽࡩࡵࡪࠣࡩࡷࡸ࡯ࡳࠢ࠽ࠤࠬῠ") + str(error))
  return False
def bstack11l1ll1lll_opy_(test_tags):
  bstack1l111ll1111_opy_ = os.getenv(bstack1lllll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡢࡅࡈࡉࡅࡔࡕࡌࡆࡎࡒࡉࡕ࡛ࡢࡇࡔࡔࡆࡊࡉࡘࡖࡆ࡚ࡉࡐࡐࡢ࡝ࡒࡒࠧῡ"))
  if bstack1l111ll1111_opy_ is None:
    return True
  bstack1l111ll1111_opy_ = json.loads(bstack1l111ll1111_opy_)
  try:
    include_tags = bstack1l111ll1111_opy_[bstack1lllll1_opy_ (u"ࠧࡪࡰࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩࠬῢ")] if bstack1lllll1_opy_ (u"ࠨ࡫ࡱࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ࠭ΰ") in bstack1l111ll1111_opy_ and isinstance(bstack1l111ll1111_opy_[bstack1lllll1_opy_ (u"ࠩ࡬ࡲࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧῤ")], list) else []
    exclude_tags = bstack1l111ll1111_opy_[bstack1lllll1_opy_ (u"ࠪࡩࡽࡩ࡬ࡶࡦࡨࡘࡦ࡭ࡳࡊࡰࡗࡩࡸࡺࡩ࡯ࡩࡖࡧࡴࡶࡥࠨῥ")] if bstack1lllll1_opy_ (u"ࠫࡪࡾࡣ࡭ࡷࡧࡩ࡙ࡧࡧࡴࡋࡱࡘࡪࡹࡴࡪࡰࡪࡗࡨࡵࡰࡦࠩῦ") in bstack1l111ll1111_opy_ and isinstance(bstack1l111ll1111_opy_[bstack1lllll1_opy_ (u"ࠬ࡫ࡸࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪῧ")], list) else []
    excluded = any(tag in exclude_tags for tag in test_tags)
    included = len(include_tags) == 0 or any(tag in include_tags for tag in test_tags)
    return not excluded and included
  except Exception as error:
    logger.debug(bstack1lllll1_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡽࡨࡪ࡮ࡨࠤࡻࡧ࡬ࡪࡦࡤࡸ࡮ࡴࡧࠡࡶࡨࡷࡹࠦࡣࡢࡵࡨࠤ࡫ࡵࡲࠡࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡤࡨࡪࡴࡸࡥࠡࡵࡦࡥࡳࡴࡩ࡯ࡩ࠱ࠤࡊࡸࡲࡰࡴࠣ࠾ࠥࠨῨ") + str(error))
  return False
def bstack1llll1ll1lll_opy_(config, frameworkName, bstack1lllll11l11l_opy_, bstack1lllll11ll1l_opy_):
  bstack1lllll11l1ll_opy_ = bstack111l1111l1l_opy_(config)
  bstack1lllll11111l_opy_ = bstack1111ll1ll11_opy_(config)
  if bstack1lllll11l1ll_opy_ is None or bstack1lllll11111l_opy_ is None:
    logger.error(bstack1lllll1_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡻ࡭࡯࡬ࡦࠢࡦࡶࡪࡧࡴࡪࡰࡪࠤࡹ࡫ࡳࡵࠢࡵࡹࡳࠦࡦࡰࡴࠣࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡀࠠࡎ࡫ࡶࡷ࡮ࡴࡧࠡࡣࡸࡸ࡭࡫࡮ࡵ࡫ࡦࡥࡹ࡯࡯࡯ࠢࡷࡳࡰ࡫࡮ࠨῩ"))
    return [None, None]
  try:
    settings = json.loads(os.getenv(bstack1lllll1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡤࡇࡃࡄࡇࡖࡗࡎࡈࡉࡍࡋࡗ࡝ࡤࡉࡏࡏࡈࡌࡋ࡚ࡘࡁࡕࡋࡒࡒࡤ࡟ࡍࡍࠩῪ"), bstack1lllll1_opy_ (u"ࠩࡾࢁࠬΎ")))
    data = {
        bstack1lllll1_opy_ (u"ࠪࡴࡷࡵࡪࡦࡥࡷࡒࡦࡳࡥࠨῬ"): config[bstack1lllll1_opy_ (u"ࠫࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠩ῭")],
        bstack1lllll1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ΅"): config.get(bstack1lllll1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩ`"), os.path.basename(os.getcwd())),
        bstack1lllll1_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡚ࡩ࡮ࡧࠪ῰"): bstack1llll11l_opy_(),
        bstack1lllll1_opy_ (u"ࠨࡦࡨࡷࡨࡸࡩࡱࡶ࡬ࡳࡳ࠭῱"): config.get(bstack1lllll1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡅࡧࡶࡧࡷ࡯ࡰࡵ࡫ࡲࡲࠬῲ"), bstack1lllll1_opy_ (u"ࠪࠫῳ")),
        bstack1lllll1_opy_ (u"ࠫࡸࡵࡵࡳࡥࡨࠫῴ"): {
            bstack1lllll1_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡏࡣࡰࡩࠬ῵"): frameworkName,
            bstack1lllll1_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡘࡨࡶࡸ࡯࡯࡯ࠩῶ"): bstack1lllll11l11l_opy_,
            bstack1lllll1_opy_ (u"ࠧࡴࡦ࡮࡚ࡪࡸࡳࡪࡱࡱࠫῷ"): __version__,
            bstack1lllll1_opy_ (u"ࠨ࡮ࡤࡲ࡬ࡻࡡࡨࡧࠪῸ"): bstack1lllll1_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩΌ"),
            bstack1lllll1_opy_ (u"ࠪࡸࡪࡹࡴࡇࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪῺ"): bstack1lllll1_opy_ (u"ࠫࡸ࡫࡬ࡦࡰ࡬ࡹࡲ࠭Ώ"),
            bstack1lllll1_opy_ (u"ࠬࡺࡥࡴࡶࡉࡶࡦࡳࡥࡸࡱࡵ࡯࡛࡫ࡲࡴ࡫ࡲࡲࠬῼ"): bstack1lllll11ll1l_opy_
        },
        bstack1lllll1_opy_ (u"࠭ࡳࡦࡶࡷ࡭ࡳ࡭ࡳࠨ´"): settings,
        bstack1lllll1_opy_ (u"ࠧࡷࡧࡵࡷ࡮ࡵ࡮ࡄࡱࡱࡸࡷࡵ࡬ࠨ῾"): bstack111l1llll1l_opy_(),
        bstack1lllll1_opy_ (u"ࠨࡥ࡬ࡍࡳ࡬࡯ࠨ῿"): bstack1ll111111l_opy_(),
        bstack1lllll1_opy_ (u"ࠩ࡫ࡳࡸࡺࡉ࡯ࡨࡲࠫ "): get_host_info(),
        bstack1lllll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬ "): bstack11ll11111_opy_(config)
    }
    headers = {
        bstack1lllll1_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲࡚ࡹࡱࡧࠪ "): bstack1lllll1_opy_ (u"ࠬࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲࡮ࡸࡵ࡮ࠨ "),
    }
    config = {
        bstack1lllll1_opy_ (u"࠭ࡡࡶࡶ࡫ࠫ "): (bstack1lllll11l1ll_opy_, bstack1lllll11111l_opy_),
        bstack1lllll1_opy_ (u"ࠧࡩࡧࡤࡨࡪࡸࡳࠨ "): headers
    }
    response = bstack1l1111111_opy_(bstack1lllll1_opy_ (u"ࠨࡒࡒࡗ࡙࠭ "), bstack1lllll111lll_opy_ + bstack1lllll1_opy_ (u"ࠩ࠲ࡺ࠷࠵ࡴࡦࡵࡷࡣࡷࡻ࡮ࡴࠩ "), data, config)
    bstack1llll1ll1l11_opy_ = response.json()
    if bstack1llll1ll1l11_opy_[bstack1lllll1_opy_ (u"ࠪࡷࡺࡩࡣࡦࡵࡶࠫ ")]:
      parsed = json.loads(os.getenv(bstack1lllll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡠࡃࡆࡇࡊ࡙ࡓࡊࡄࡌࡐࡎ࡚࡙ࡠࡅࡒࡒࡋࡏࡇࡖࡔࡄࡘࡎࡕࡎࡠ࡛ࡐࡐࠬ "), bstack1lllll1_opy_ (u"ࠬࢁࡽࠨ ")))
      parsed[bstack1lllll1_opy_ (u"࠭ࡳࡤࡣࡱࡲࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧ​")] = bstack1llll1ll1l11_opy_[bstack1lllll1_opy_ (u"ࠧࡥࡣࡷࡥࠬ‌")][bstack1lllll1_opy_ (u"ࠨࡵࡦࡥࡳࡴࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩ‍")]
      os.environ[bstack1lllll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡥࡁࡄࡅࡈࡗࡘࡏࡂࡊࡎࡌࡘ࡞ࡥࡃࡐࡐࡉࡍࡌ࡛ࡒࡂࡖࡌࡓࡓࡥ࡙ࡎࡎࠪ‎")] = json.dumps(parsed)
      bstack1llll11l11_opy_.bstack1111l1111_opy_(bstack1llll1ll1l11_opy_[bstack1lllll1_opy_ (u"ࠪࡨࡦࡺࡡࠨ‏")][bstack1lllll1_opy_ (u"ࠫࡸࡩࡲࡪࡲࡷࡷࠬ‐")])
      bstack1llll11l11_opy_.bstack1lllll1l11ll_opy_(bstack1llll1ll1l11_opy_[bstack1lllll1_opy_ (u"ࠬࡪࡡࡵࡣࠪ‑")][bstack1lllll1_opy_ (u"࠭ࡣࡰ࡯ࡰࡥࡳࡪࡳࠨ‒")])
      bstack1llll11l11_opy_.store()
      return bstack1llll1ll1l11_opy_[bstack1lllll1_opy_ (u"ࠧࡥࡣࡷࡥࠬ–")][bstack1lllll1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡕࡱ࡮ࡩࡳ࠭—")], bstack1llll1ll1l11_opy_[bstack1lllll1_opy_ (u"ࠩࡧࡥࡹࡧࠧ―")][bstack1lllll1_opy_ (u"ࠪ࡭ࡩ࠭‖")]
    else:
      logger.error(bstack1lllll1_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡸࡪ࡬ࡰࡪࠦࡲࡶࡰࡱ࡭ࡳ࡭ࠠࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰ࠽ࠤࠬ‗") + bstack1llll1ll1l11_opy_[bstack1lllll1_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭‘")])
      if bstack1llll1ll1l11_opy_[bstack1lllll1_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ’")] == bstack1lllll1_opy_ (u"ࠧࡊࡰࡹࡥࡱ࡯ࡤࠡࡥࡲࡲ࡫࡯ࡧࡶࡴࡤࡸ࡮ࡵ࡮ࠡࡲࡤࡷࡸ࡫ࡤ࠯ࠩ‚"):
        for bstack1llll1lllll1_opy_ in bstack1llll1ll1l11_opy_[bstack1lllll1_opy_ (u"ࠨࡧࡵࡶࡴࡸࡳࠨ‛")]:
          logger.error(bstack1llll1lllll1_opy_[bstack1lllll1_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ“")])
      return None, None
  except Exception as error:
    logger.error(bstack1lllll1_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡷࡩ࡫࡯ࡩࠥࡩࡲࡦࡣࡷ࡭ࡳ࡭ࠠࡵࡧࡶࡸࠥࡸࡵ࡯ࠢࡩࡳࡷࠦࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯࠼ࠣࠦ”") +  str(error))
    return None, None
def bstack1llll1llll1l_opy_():
  if os.getenv(bstack1lllll1_opy_ (u"ࠫࡇ࡙࡟ࡂ࠳࠴࡝ࡤࡐࡗࡕࠩ„")) is None:
    return {
        bstack1lllll1_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬ‟"): bstack1lllll1_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬ†"),
        bstack1lllll1_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ‡"): bstack1lllll1_opy_ (u"ࠨࡄࡸ࡭ࡱࡪࠠࡤࡴࡨࡥࡹ࡯࡯࡯ࠢ࡫ࡥࡩࠦࡦࡢ࡫࡯ࡩࡩ࠴ࠧ•")
    }
  data = {bstack1lllll1_opy_ (u"ࠩࡨࡲࡩ࡚ࡩ࡮ࡧࠪ‣"): bstack1llll11l_opy_()}
  headers = {
      bstack1lllll1_opy_ (u"ࠪࡅࡺࡺࡨࡰࡴ࡬ࡾࡦࡺࡩࡰࡰࠪ․"): bstack1lllll1_opy_ (u"ࠫࡇ࡫ࡡࡳࡧࡵࠤࠬ‥") + os.getenv(bstack1lllll1_opy_ (u"ࠧࡈࡓࡠࡃ࠴࠵࡞ࡥࡊࡘࡖࠥ…")),
      bstack1lllll1_opy_ (u"࠭ࡃࡰࡰࡷࡩࡳࡺ࠭ࡕࡻࡳࡩࠬ‧"): bstack1lllll1_opy_ (u"ࠧࡢࡲࡳࡰ࡮ࡩࡡࡵ࡫ࡲࡲ࠴ࡰࡳࡰࡰࠪ ")
  }
  response = bstack1l1111111_opy_(bstack1lllll1_opy_ (u"ࠨࡒࡘࡘࠬ "), bstack1lllll111lll_opy_ + bstack1lllll1_opy_ (u"ࠩ࠲ࡸࡪࡹࡴࡠࡴࡸࡲࡸ࠵ࡳࡵࡱࡳࠫ‪"), data, { bstack1lllll1_opy_ (u"ࠪ࡬ࡪࡧࡤࡦࡴࡶࠫ‫"): headers })
  try:
    if response.status_code == 200:
      logger.info(bstack1lllll1_opy_ (u"ࠦࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡕࡧࡶࡸࠥࡘࡵ࡯ࠢࡰࡥࡷࡱࡥࡥࠢࡤࡷࠥࡩ࡯࡮ࡲ࡯ࡩࡹ࡫ࡤࠡࡣࡷࠤࠧ‬") + bstack1l1ll1l1_opy_().isoformat() + bstack1lllll1_opy_ (u"ࠬࡠࠧ‭"))
      return {bstack1lllll1_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭‮"): bstack1lllll1_opy_ (u"ࠧࡴࡷࡦࡧࡪࡹࡳࠨ "), bstack1lllll1_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ‰"): bstack1lllll1_opy_ (u"ࠩࠪ‱")}
    else:
      response.raise_for_status()
  except requests.RequestException as error:
    logger.error(bstack1lllll1_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡷࡩ࡫࡯ࡩࠥࡳࡡࡳ࡭࡬ࡲ࡬ࠦࡣࡰ࡯ࡳࡰࡪࡺࡩࡰࡰࠣࡳ࡫ࠦࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡗࡩࡸࡺࠠࡓࡷࡱ࠾ࠥࠨ′") + str(error))
    return {
        bstack1lllll1_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫ″"): bstack1lllll1_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫ‴"),
        bstack1lllll1_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ‵"): str(error)
    }
def bstack1llll1lll111_opy_(bstack1llll1lll1ll_opy_):
    return re.match(bstack1lllll1_opy_ (u"ࡲࠨࡠ࡟ࡨ࠰࠮࡜࠯࡞ࡧ࠯࠮ࡅࠤࠨ‶"), bstack1llll1lll1ll_opy_.strip()) is not None
def bstack111lllll1_opy_(caps, options, desired_capabilities={}, config=None):
    try:
        if options:
          bstack1lllll111ll1_opy_ = options.to_capabilities()
        elif desired_capabilities:
          bstack1lllll111ll1_opy_ = desired_capabilities
        else:
          bstack1lllll111ll1_opy_ = {}
        bstack1l111l1l1ll_opy_ = (bstack1lllll111ll1_opy_.get(bstack1lllll1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡑࡥࡲ࡫ࠧ‷"), bstack1lllll1_opy_ (u"ࠩࠪ‸")).lower() or caps.get(bstack1lllll1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡓࡧ࡭ࡦࠩ‹"), bstack1lllll1_opy_ (u"ࠫࠬ›")).lower())
        if bstack1l111l1l1ll_opy_ == bstack1lllll1_opy_ (u"ࠬ࡯࡯ࡴࠩ※"):
            return True
        if bstack1l111l1l1ll_opy_ == bstack1lllll1_opy_ (u"࠭ࡡ࡯ࡦࡵࡳ࡮ࡪࠧ‼"):
            bstack1l111l1ll11_opy_ = str(float(caps.get(bstack1lllll1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠩ‽")) or bstack1lllll111ll1_opy_.get(bstack1lllll1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩ‾"), {}).get(bstack1lllll1_opy_ (u"ࠩࡲࡷ࡛࡫ࡲࡴ࡫ࡲࡲࠬ‿"),bstack1lllll1_opy_ (u"ࠪࠫ⁀"))))
            if bstack1l111l1l1ll_opy_ == bstack1lllll1_opy_ (u"ࠫࡦࡴࡤࡳࡱ࡬ࡨࠬ⁁") and int(bstack1l111l1ll11_opy_.split(bstack1lllll1_opy_ (u"ࠬ࠴ࠧ⁂"))[0]) < float(bstack11l1l1l1l11_opy_):
                logger.warning(str(bstack11l1l1ll111_opy_))
                return False
            return True
        bstack1l111lll1l1_opy_ = caps.get(bstack1lllll1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧ⁃"), {}).get(bstack1lllll1_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࡎࡢ࡯ࡨࠫ⁄"), caps.get(bstack1lllll1_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࠨ⁅"), bstack1lllll1_opy_ (u"ࠩࠪ⁆")))
        if bstack1l111lll1l1_opy_:
            logger.warning(bstack1lllll1_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡸ࡫࡯ࡰࠥࡸࡵ࡯ࠢࡲࡲࡱࡿࠠࡰࡰࠣࡈࡪࡹ࡫ࡵࡱࡳࠤࡧࡸ࡯ࡸࡵࡨࡶࡸ࠴ࠢ⁇"))
            return False
        browser = caps.get(bstack1lllll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩ⁈"), bstack1lllll1_opy_ (u"ࠬ࠭⁉")).lower() or bstack1lllll111ll1_opy_.get(bstack1lllll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫ⁊"), bstack1lllll1_opy_ (u"ࠧࠨ⁋")).lower()
        if browser != bstack1lllll1_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࠨ⁌"):
            logger.warning(bstack1lllll1_opy_ (u"ࠤࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡷࡪ࡮࡯ࠤࡷࡻ࡮ࠡࡱࡱࡰࡾࠦ࡯࡯ࠢࡆ࡬ࡷࡵ࡭ࡦࠢࡥࡶࡴࡽࡳࡦࡴࡶ࠲ࠧ⁍"))
            return False
        browser_version = caps.get(bstack1lllll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫ⁎")) or caps.get(bstack1lllll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭⁏")) or bstack1lllll111ll1_opy_.get(bstack1lllll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭⁐")) or bstack1lllll111ll1_opy_.get(bstack1lllll1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧ⁑"), {}).get(bstack1lllll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨ⁒")) or bstack1lllll111ll1_opy_.get(bstack1lllll1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩ⁓"), {}).get(bstack1lllll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡺࡪࡸࡳࡪࡱࡱࠫ⁔"))
        bstack1l111lll111_opy_ = bstack1lllll111111_opy_.bstack1l111l111ll_opy_
        bstack1lllll11ll11_opy_ = False
        if config is not None:
          bstack1lllll11ll11_opy_ = bstack1lllll1_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧ⁕") in config and str(config[bstack1lllll1_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨ⁖")]).lower() != bstack1lllll1_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫ⁗")
        if os.environ.get(bstack1lllll1_opy_ (u"࠭ࡉࡔࡡࡑࡓࡓࡥࡂࡔࡖࡄࡇࡐࡥࡉࡏࡈࡕࡅࡤࡇ࠱࠲࡛ࡢࡗࡊ࡙ࡓࡊࡑࡑࠫ⁘"), bstack1lllll1_opy_ (u"ࠧࠨ⁙")).lower() == bstack1lllll1_opy_ (u"ࠨࡶࡵࡹࡪ࠭⁚") or bstack1lllll11ll11_opy_:
          bstack1l111lll111_opy_ = bstack1lllll111111_opy_.bstack1l111l1l11l_opy_
        if browser_version and browser_version != bstack1lllll1_opy_ (u"ࠩ࡯ࡥࡹ࡫ࡳࡵࠩ⁛") and int(browser_version.split(bstack1lllll1_opy_ (u"ࠪ࠲ࠬ⁜"))[0]) <= bstack1l111lll111_opy_:
          logger.warning(bstack1lll1lll11l_opy_ (u"ࠫࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡹ࡬ࡰࡱࠦࡲࡶࡰࠣࡳࡳࡲࡹࠡࡱࡱࠤࡈ࡮ࡲࡰ࡯ࡨࠤࡧࡸ࡯ࡸࡵࡨࡶࠥࡼࡥࡳࡵ࡬ࡳࡳࠦࡧࡳࡧࡤࡸࡪࡸࠠࡵࡪࡤࡲࠥࢁ࡭ࡪࡰࡢࡥ࠶࠷ࡹࡠࡵࡸࡴࡵࡵࡲࡵࡧࡧࡣࡨ࡮ࡲࡰ࡯ࡨࡣࡻ࡫ࡲࡴ࡫ࡲࡲࢂ࠴ࠧ⁝"))
          return False
        if not options:
          bstack1l111l1ll1l_opy_ = caps.get(bstack1lllll1_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ⁞")) or bstack1lllll111ll1_opy_.get(bstack1lllll1_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫ "), {})
          if bstack1lllll1_opy_ (u"ࠧ࠮࠯࡫ࡩࡦࡪ࡬ࡦࡵࡶࠫ⁠") in bstack1l111l1ll1l_opy_.get(bstack1lllll1_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭⁡"), []):
              logger.warning(bstack1lllll1_opy_ (u"ࠤࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡷࡪ࡮࡯ࠤࡳࡵࡴࠡࡴࡸࡲࠥࡵ࡮ࠡ࡮ࡨ࡫ࡦࡩࡹࠡࡪࡨࡥࡩࡲࡥࡴࡵࠣࡱࡴࡪࡥ࠯ࠢࡖࡻ࡮ࡺࡣࡩࠢࡷࡳࠥࡴࡥࡸࠢ࡫ࡩࡦࡪ࡬ࡦࡵࡶࠤࡲࡵࡤࡦࠢࡲࡶࠥࡧࡶࡰ࡫ࡧࠤࡺࡹࡩ࡯ࡩࠣ࡬ࡪࡧࡤ࡭ࡧࡶࡷࠥࡳ࡯ࡥࡧ࠱ࠦ⁢"))
              return False
        return True
    except Exception as error:
        logger.debug(bstack1lllll1_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡹࡥࡱ࡯ࡤࡢࡶࡨࠤࡦ࠷࠱ࡺࠢࡶࡹࡵࡶ࡯ࡳࡶࠣ࠾ࠧ⁣") + str(error))
        return False
def set_capabilities(caps, config):
  try:
    bstack1l1l1ll1l1l_opy_ = config.get(bstack1lllll1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫ⁤"), {})
    bstack1l1l1ll1l1l_opy_[bstack1lllll1_opy_ (u"ࠬࡧࡵࡵࡪࡗࡳࡰ࡫࡮ࠨ⁥")] = os.getenv(bstack1lllll1_opy_ (u"࠭ࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗࠫ⁦"))
    bstack111l1l1l111_opy_ = json.loads(os.getenv(bstack1lllll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡣࡆࡉࡃࡆࡕࡖࡍࡇࡏࡌࡊࡖ࡜ࡣࡈࡕࡎࡇࡋࡊ࡙ࡗࡇࡔࡊࡑࡑࡣ࡞ࡓࡌࠨ⁧"), bstack1lllll1_opy_ (u"ࠨࡽࢀࠫ⁨"))).get(bstack1lllll1_opy_ (u"ࠩࡶࡧࡦࡴ࡮ࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪ⁩"))
    if not config[bstack1lllll1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡒࡵࡳࡩࡻࡣࡵࡏࡤࡴࠬ⁪")].get(bstack1lllll1_opy_ (u"ࠦࡦࡶࡰࡠࡣࡸࡸࡴࡳࡡࡵࡧࠥ⁫")):
      if bstack1lllll1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭⁬") in caps:
        caps[bstack1lllll1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧ⁭")][bstack1lllll1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧ⁮")] = bstack1l1l1ll1l1l_opy_
        caps[bstack1lllll1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩ⁯")][bstack1lllll1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩ⁰")][bstack1lllll1_opy_ (u"ࠪࡷࡨࡧ࡮࡯ࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫⁱ")] = bstack111l1l1l111_opy_
      else:
        caps[bstack1lllll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪ⁲")] = bstack1l1l1ll1l1l_opy_
        caps[bstack1lllll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫ⁳")][bstack1lllll1_opy_ (u"࠭ࡳࡤࡣࡱࡲࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧ⁴")] = bstack111l1l1l111_opy_
  except Exception as error:
    logger.debug(bstack1lllll1_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡻ࡭࡯࡬ࡦࠢࡶࡩࡹࡺࡩ࡯ࡩࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠴ࠠࡆࡴࡵࡳࡷࡀࠠࠣ⁵") +  str(error))
def bstack1111lll1l_opy_(driver, bstack1llll1llll11_opy_):
  try:
    setattr(driver, bstack1lllll1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡂ࠳࠴ࡽࡘ࡮࡯ࡶ࡮ࡧࡗࡨࡧ࡮ࠨ⁶"), True)
    session = driver.session_id
    if session:
      bstack1llll1lll1l1_opy_ = True
      current_url = driver.current_url
      try:
        url = urlparse(current_url)
      except Exception as e:
        bstack1llll1lll1l1_opy_ = False
      bstack1llll1lll1l1_opy_ = url.scheme in [bstack1lllll1_opy_ (u"ࠤ࡫ࡸࡹࡶࠢ⁷"), bstack1lllll1_opy_ (u"ࠥ࡬ࡹࡺࡰࡴࠤ⁸")]
      if bstack1llll1lll1l1_opy_:
        if bstack1llll1llll11_opy_:
          logger.info(bstack1lllll1_opy_ (u"ࠦࡘ࡫ࡴࡶࡲࠣࡪࡴࡸࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡵࡧࡶࡸ࡮ࡴࡧࠡࡪࡤࡷࠥࡹࡴࡢࡴࡷࡩࡩ࠴ࠠࡂࡷࡷࡳࡲࡧࡴࡦࠢࡷࡩࡸࡺࠠࡤࡣࡶࡩࠥ࡫ࡸࡦࡥࡸࡸ࡮ࡵ࡮ࠡࡹ࡬ࡰࡱࠦࡢࡦࡩ࡬ࡲࠥࡳ࡯࡮ࡧࡱࡸࡦࡸࡩ࡭ࡻ࠱ࠦ⁹"))
      return bstack1llll1llll11_opy_
  except Exception as e:
    logger.error(bstack1lllll1_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡸࡺࡡࡳࡶ࡬ࡲ࡬ࠦࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡷࡨࡧ࡮ࠡࡨࡲࡶࠥࡺࡨࡪࡵࠣࡸࡪࡹࡴࠡࡥࡤࡷࡪࡀࠠࠣ⁺") + str(e))
    return False
def bstack1111l1ll_opy_(driver, name, path):
  try:
    bstack1l111ll1l11_opy_ = {
        bstack1lllll1_opy_ (u"࠭ࡴࡩࡖࡨࡷࡹࡘࡵ࡯ࡗࡸ࡭ࡩ࠭⁻"): threading.current_thread().current_test_uuid,
        bstack1lllll1_opy_ (u"ࠧࡵࡪࡅࡹ࡮ࡲࡤࡖࡷ࡬ࡨࠬ⁼"): os.environ.get(bstack1lllll1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭⁽"), bstack1lllll1_opy_ (u"ࠩࠪ⁾")),
        bstack1lllll1_opy_ (u"ࠪࡸ࡭ࡐࡷࡵࡖࡲ࡯ࡪࡴࠧⁿ"): os.environ.get(bstack1lllll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨ₀"), bstack1lllll1_opy_ (u"ࠬ࠭₁"))
    }
    bstack1ll1l1l1111_opy_ = bstack11l11l1111_opy_.bstack1ll11111ll1_opy_(EVENTS.bstack1l1l1l1ll_opy_.value)
    logger.debug(bstack1lllll1_opy_ (u"࠭ࡐࡦࡴࡩࡳࡷࡳࡩ࡯ࡩࠣࡷࡨࡧ࡮ࠡࡤࡨࡪࡴࡸࡥࠡࡵࡤࡺ࡮ࡴࡧࠡࡴࡨࡷࡺࡲࡴࡴࠩ₂"))
    try:
      if (bstack1lll1l11_opy_(threading.current_thread(), bstack1lllll1_opy_ (u"ࠧࡪࡵࡄࡴࡵࡇ࠱࠲ࡻࡗࡩࡸࡺࠧ₃"), None) and bstack1lll1l11_opy_(threading.current_thread(), bstack1lllll1_opy_ (u"ࠨࡣࡳࡴࡆ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪ₄"), None)):
        scripts = {bstack1lllll1_opy_ (u"ࠩࡶࡧࡦࡴࠧ₅"): bstack1llll11l11_opy_.perform_scan}
        bstack1lllll1111l1_opy_ = json.loads(scripts[bstack1lllll1_opy_ (u"ࠥࡷࡨࡧ࡮ࠣ₆")].replace(bstack1lllll1_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࠢ₇"), bstack1lllll1_opy_ (u"ࠧࠨ₈")))
        bstack1lllll1111l1_opy_[bstack1lllll1_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩ₉")][bstack1lllll1_opy_ (u"ࠧ࡮ࡧࡷ࡬ࡴࡪࠧ₊")] = None
        scripts[bstack1lllll1_opy_ (u"ࠣࡵࡦࡥࡳࠨ₋")] = bstack1lllll1_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࠧ₌") + json.dumps(bstack1lllll1111l1_opy_)
        bstack1llll11l11_opy_.bstack1111l1111_opy_(scripts)
        bstack1llll11l11_opy_.store()
        logger.debug(driver.execute_script(bstack1llll11l11_opy_.perform_scan))
      else:
        logger.debug(driver.execute_async_script(bstack1llll11l11_opy_.perform_scan, {bstack1lllll1_opy_ (u"ࠥࡱࡪࡺࡨࡰࡦࠥ₍"): name}))
      bstack11l11l1111_opy_.end(EVENTS.bstack1l1l1l1ll_opy_.value, bstack1ll1l1l1111_opy_ + bstack1lllll1_opy_ (u"ࠦ࠿ࡹࡴࡢࡴࡷࠦ₎"), bstack1ll1l1l1111_opy_ + bstack1lllll1_opy_ (u"ࠧࡀࡥ࡯ࡦࠥ₏"), True, None)
    except Exception as error:
      bstack11l11l1111_opy_.end(EVENTS.bstack1l1l1l1ll_opy_.value, bstack1ll1l1l1111_opy_ + bstack1lllll1_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨₐ"), bstack1ll1l1l1111_opy_ + bstack1lllll1_opy_ (u"ࠢ࠻ࡧࡱࡨࠧₑ"), False, str(error))
    bstack1ll1l1l1111_opy_ = bstack11l11l1111_opy_.bstack11ll1ll11ll_opy_(EVENTS.bstack1l111lll1ll_opy_.value)
    bstack11l11l1111_opy_.mark(bstack1ll1l1l1111_opy_ + bstack1lllll1_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣₒ"))
    try:
      if (bstack1lll1l11_opy_(threading.current_thread(), bstack1lllll1_opy_ (u"ࠩ࡬ࡷࡆࡶࡰࡂ࠳࠴ࡽ࡙࡫ࡳࡵࠩₓ"), None) and bstack1lll1l11_opy_(threading.current_thread(), bstack1lllll1_opy_ (u"ࠪࡥࡵࡶࡁ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬₔ"), None)):
        scripts = {bstack1lllll1_opy_ (u"ࠫࡸࡩࡡ࡯ࠩₕ"): bstack1llll11l11_opy_.perform_scan}
        bstack1lllll1111l1_opy_ = json.loads(scripts[bstack1lllll1_opy_ (u"ࠧࡹࡣࡢࡰࠥₖ")].replace(bstack1lllll1_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࠤₗ"), bstack1lllll1_opy_ (u"ࠢࠣₘ")))
        bstack1lllll1111l1_opy_[bstack1lllll1_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫₙ")][bstack1lllll1_opy_ (u"ࠩࡰࡩࡹ࡮࡯ࡥࠩₚ")] = None
        scripts[bstack1lllll1_opy_ (u"ࠥࡷࡨࡧ࡮ࠣₛ")] = bstack1lllll1_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࠢₜ") + json.dumps(bstack1lllll1111l1_opy_)
        bstack1llll11l11_opy_.bstack1111l1111_opy_(scripts)
        bstack1llll11l11_opy_.store()
        logger.debug(driver.execute_script(bstack1llll11l11_opy_.perform_scan))
      else:
        logger.debug(driver.execute_async_script(bstack1llll11l11_opy_.bstack1lllll1l111l_opy_, bstack1l111ll1l11_opy_))
      bstack11l11l1111_opy_.end(bstack1ll1l1l1111_opy_, bstack1ll1l1l1111_opy_ + bstack1lllll1_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧ₝"), bstack1ll1l1l1111_opy_ + bstack1lllll1_opy_ (u"ࠨ࠺ࡦࡰࡧࠦ₞"),True, None)
    except Exception as error:
      bstack11l11l1111_opy_.end(bstack1ll1l1l1111_opy_, bstack1ll1l1l1111_opy_ + bstack1lllll1_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢ₟"), bstack1ll1l1l1111_opy_ + bstack1lllll1_opy_ (u"ࠣ࠼ࡨࡲࡩࠨ₠"),False, str(error))
    logger.info(bstack1lllll1_opy_ (u"ࠤࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡷࡩࡸࡺࡩ࡯ࡩࠣࡪࡴࡸࠠࡵࡪ࡬ࡷࠥࡺࡥࡴࡶࠣࡧࡦࡹࡥࠡࡪࡤࡷࠥ࡫࡮ࡥࡧࡧ࠲ࠧ₡"))
  except Exception as bstack1l1111ll11l_opy_:
    logger.error(bstack1lllll1_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡶࡪࡹࡵ࡭ࡶࡶࠤࡨࡵࡵ࡭ࡦࠣࡲࡴࡺࠠࡣࡧࠣࡴࡷࡵࡣࡦࡵࡶࡩࡩࠦࡦࡰࡴࠣࡸ࡭࡫ࠠࡵࡧࡶࡸࠥࡩࡡࡴࡧ࠽ࠤࠧ₢") + str(path) + bstack1lllll1_opy_ (u"ࠦࠥࡋࡲࡳࡱࡵࠤ࠿ࠨ₣") + str(bstack1l1111ll11l_opy_))
def bstack1lllll11l111_opy_(driver):
    caps = driver.capabilities
    if caps.get(bstack1lllll1_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࡎࡢ࡯ࡨࠦ₤")) and str(caps.get(bstack1lllll1_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡏࡣࡰࡩࠧ₥"))).lower() == bstack1lllll1_opy_ (u"ࠢࡢࡰࡧࡶࡴ࡯ࡤࠣ₦"):
        bstack1l111l1ll11_opy_ = caps.get(bstack1lllll1_opy_ (u"ࠣࡣࡳࡴ࡮ࡻ࡭࠻ࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࡙ࡩࡷࡹࡩࡰࡰࠥ₧")) or caps.get(bstack1lllll1_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰ࡚ࡪࡸࡳࡪࡱࡱࠦ₨"))
        if bstack1l111l1ll11_opy_ and int(str(bstack1l111l1ll11_opy_)) < bstack11l1l1l1l11_opy_:
            return False
    return True
def bstack111ll111l1_opy_(config):
  if bstack1lllll1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ₩") in config:
        return config[bstack1lllll1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ₪")]
  for platform in config.get(bstack1lllll1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ₫"), []):
      if bstack1lllll1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭€") in platform:
          return platform[bstack1lllll1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ₭")]
  return None
def bstack11lll1111l_opy_(bstack11llll1l1_opy_):
  try:
    browser_name = bstack11llll1l1_opy_[bstack1lllll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡱࡥࡲ࡫ࠧ₮")]
    browser_version = bstack11llll1l1_opy_[bstack1lllll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡺࡪࡸࡳࡪࡱࡱࠫ₯")]
    chrome_options = bstack11llll1l1_opy_[bstack1lllll1_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧࡢࡳࡵࡺࡩࡰࡰࡶࠫ₰")]
    try:
        bstack1lllll11lll1_opy_ = int(browser_version.split(bstack1lllll1_opy_ (u"ࠫ࠳࠭₱"))[0])
    except ValueError as e:
        logger.error(bstack1lllll1_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡧࡴࡴࡶࡦࡴࡷ࡭ࡳ࡭ࠠࡣࡴࡲࡻࡸ࡫ࡲࠡࡸࡨࡶࡸ࡯࡯࡯ࠤ₲") + str(e))
        return False
    if not (browser_name and browser_name.lower() == bstack1lllll1_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪ࠭₳")):
        logger.warning(bstack1lllll1_opy_ (u"ࠢࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡼ࡯࡬࡭ࠢࡵࡹࡳࠦ࡯࡯࡮ࡼࠤࡴࡴࠠࡄࡪࡵࡳࡲ࡫ࠠࡣࡴࡲࡻࡸ࡫ࡲࡴ࠰ࠥ₴"))
        return False
    if bstack1lllll11lll1_opy_ < bstack1lllll111111_opy_.bstack1l111l1l11l_opy_:
        logger.warning(bstack1lll1lll11l_opy_ (u"ࠨࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡸࡥࡲࡷ࡬ࡶࡪࡹࠠࡄࡪࡵࡳࡲ࡫ࠠࡷࡧࡵࡷ࡮ࡵ࡮ࠡࡽࡆࡓࡓ࡙ࡔࡂࡐࡗࡗ࠳ࡓࡉࡏࡋࡐ࡙ࡒࡥࡎࡐࡐࡢࡆࡘ࡚ࡁࡄࡍࡢࡍࡓࡌࡒࡂࡡࡄ࠵࠶࡟࡟ࡔࡗࡓࡔࡔࡘࡔࡆࡆࡢࡇࡍࡘࡏࡎࡇࡢ࡚ࡊࡘࡓࡊࡑࡑࢁࠥࡵࡲࠡࡪ࡬࡫࡭࡫ࡲ࠯ࠩ₵"))
        return False
    if chrome_options and any(bstack1lllll1_opy_ (u"ࠩ࠰࠱࡭࡫ࡡࡥ࡮ࡨࡷࡸ࠭₶") in value for value in chrome_options.values() if isinstance(value, str)):
        logger.warning(bstack1lllll1_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡸ࡫࡯ࡰࠥࡴ࡯ࡵࠢࡵࡹࡳࠦ࡯࡯ࠢ࡯ࡩ࡬ࡧࡣࡺࠢ࡫ࡩࡦࡪ࡬ࡦࡵࡶࠤࡲࡵࡤࡦ࠰ࠣࡗࡼ࡯ࡴࡤࡪࠣࡸࡴࠦ࡮ࡦࡹࠣ࡬ࡪࡧࡤ࡭ࡧࡶࡷࠥࡳ࡯ࡥࡧࠣࡳࡷࠦࡡࡷࡱ࡬ࡨࠥࡻࡳࡪࡰࡪࠤ࡭࡫ࡡࡥ࡮ࡨࡷࡸࠦ࡭ࡰࡦࡨ࠲ࠧ₷"))
        return False
    return True
  except Exception as e:
    logger.error(bstack1lllll1_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡣࡩࡧࡦ࡯࡮ࡴࡧࠡࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࠣࡷࡺࡶࡰࡰࡴࡷࠤ࡫ࡵࡲࠡ࡮ࡲࡧࡦࡲࠠࡄࡪࡵࡳࡲ࡫࠺ࠡࠤ₸") + str(e))
    return False
def bstack1l1l1lll1_opy_(bstack1ll1l1l111_opy_, config):
    try:
      bstack1l111l1111l_opy_ = bstack1lllll1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ₹") in config and config[bstack1lllll1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭₺")] == True
      bstack1lllll11ll11_opy_ = bstack1lllll1_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫ₻") in config and str(config[bstack1lllll1_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬ₼")]).lower() != bstack1lllll1_opy_ (u"ࠩࡩࡥࡱࡹࡥࠨ₽")
      if not (bstack1l111l1111l_opy_ and (not bstack11ll11111_opy_(config) or bstack1lllll11ll11_opy_)):
        return bstack1ll1l1l111_opy_
      bstack1llll1ll11ll_opy_ = bstack1llll11l11_opy_.bstack1lllll1l1l1l_opy_
      if bstack1llll1ll11ll_opy_ is None:
        logger.debug(bstack1lllll1_opy_ (u"ࠥࡋࡴࡵࡧ࡭ࡧࠣࡧ࡭ࡸ࡯࡮ࡧࠣࡳࡵࡺࡩࡰࡰࡶࠤࡦࡸࡥࠡࡐࡲࡲࡪࠨ₾"))
        return bstack1ll1l1l111_opy_
      bstack1lllll111l1l_opy_ = int(str(bstack1111l1ll11l_opy_()).split(bstack1lllll1_opy_ (u"ࠫ࠳࠭₿"))[0])
      logger.debug(bstack1lllll1_opy_ (u"࡙ࠧࡥ࡭ࡧࡱ࡭ࡺࡳࠠࡷࡧࡵࡷ࡮ࡵ࡮ࠡࡦࡨࡸࡪࡩࡴࡦࡦ࠽ࠤࠧ⃀") + str(bstack1lllll111l1l_opy_) + bstack1lllll1_opy_ (u"ࠨࠢ⃁"))
      if bstack1lllll111l1l_opy_ == 3 and isinstance(bstack1ll1l1l111_opy_, dict) and bstack1lllll1_opy_ (u"ࠧࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠧ⃂") in bstack1ll1l1l111_opy_ and bstack1llll1ll11ll_opy_ is not None:
        if bstack1lllll1_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭⃃") not in bstack1ll1l1l111_opy_[bstack1lllll1_opy_ (u"ࠩࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩ⃄")]:
          bstack1ll1l1l111_opy_[bstack1lllll1_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪ⃅")][bstack1lllll1_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩ⃆")] = {}
        if bstack1lllll1_opy_ (u"ࠬࡧࡲࡨࡵࠪ⃇") in bstack1llll1ll11ll_opy_:
          if bstack1lllll1_opy_ (u"࠭ࡡࡳࡩࡶࠫ⃈") not in bstack1ll1l1l111_opy_[bstack1lllll1_opy_ (u"ࠧࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠧ⃉")][bstack1lllll1_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭⃊")]:
            bstack1ll1l1l111_opy_[bstack1lllll1_opy_ (u"ࠩࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩ⃋")][bstack1lllll1_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨ⃌")][bstack1lllll1_opy_ (u"ࠫࡦࡸࡧࡴࠩ⃍")] = []
          for arg in bstack1llll1ll11ll_opy_[bstack1lllll1_opy_ (u"ࠬࡧࡲࡨࡵࠪ⃎")]:
            if arg not in bstack1ll1l1l111_opy_[bstack1lllll1_opy_ (u"࠭ࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠭⃏")][bstack1lllll1_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬ⃐")][bstack1lllll1_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭⃑")]:
              bstack1ll1l1l111_opy_[bstack1lllll1_opy_ (u"ࠩࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴ⃒ࠩ")][bstack1lllll1_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨ⃓")][bstack1lllll1_opy_ (u"ࠫࡦࡸࡧࡴࠩ⃔")].append(arg)
        if bstack1lllll1_opy_ (u"ࠬ࡫ࡸࡵࡧࡱࡷ࡮ࡵ࡮ࡴࠩ⃕") in bstack1llll1ll11ll_opy_:
          if bstack1lllll1_opy_ (u"࠭ࡥࡹࡶࡨࡲࡸ࡯࡯࡯ࡵࠪ⃖") not in bstack1ll1l1l111_opy_[bstack1lllll1_opy_ (u"ࠧࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠧ⃗")][bstack1lllll1_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ⃘࠭")]:
            bstack1ll1l1l111_opy_[bstack1lllll1_opy_ (u"ࠩࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴ⃙ࠩ")][bstack1lllll1_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨ⃚")][bstack1lllll1_opy_ (u"ࠫࡪࡾࡴࡦࡰࡶ࡭ࡴࡴࡳࠨ⃛")] = []
          for ext in bstack1llll1ll11ll_opy_[bstack1lllll1_opy_ (u"ࠬ࡫ࡸࡵࡧࡱࡷ࡮ࡵ࡮ࡴࠩ⃜")]:
            if ext not in bstack1ll1l1l111_opy_[bstack1lllll1_opy_ (u"࠭ࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠭⃝")][bstack1lllll1_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬ⃞")][bstack1lllll1_opy_ (u"ࠨࡧࡻࡸࡪࡴࡳࡪࡱࡱࡷࠬ⃟")]:
              bstack1ll1l1l111_opy_[bstack1lllll1_opy_ (u"ࠩࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩ⃠")][bstack1lllll1_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨ⃡")][bstack1lllll1_opy_ (u"ࠫࡪࡾࡴࡦࡰࡶ࡭ࡴࡴࡳࠨ⃢")].append(ext)
        if bstack1lllll1_opy_ (u"ࠬࡶࡲࡦࡨࡶࠫ⃣") in bstack1llll1ll11ll_opy_:
          if bstack1lllll1_opy_ (u"࠭ࡰࡳࡧࡩࡷࠬ⃤") not in bstack1ll1l1l111_opy_[bstack1lllll1_opy_ (u"ࠧࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹ⃥ࠧ")][bstack1lllll1_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ⃦࠭")]:
            bstack1ll1l1l111_opy_[bstack1lllll1_opy_ (u"ࠩࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩ⃧")][bstack1lllll1_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨ⃨")][bstack1lllll1_opy_ (u"ࠫࡵࡸࡥࡧࡵࠪ⃩")] = {}
          bstack111l1l1l1ll_opy_(bstack1ll1l1l111_opy_[bstack1lllll1_opy_ (u"ࠬࡪࡥࡴ࡫ࡵࡩࡩࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷ⃪ࠬ")][bstack1lllll1_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶ⃫ࠫ")][bstack1lllll1_opy_ (u"ࠧࡱࡴࡨࡪࡸ⃬࠭")],
                    bstack1llll1ll11ll_opy_[bstack1lllll1_opy_ (u"ࠨࡲࡵࡩ࡫ࡹ⃭ࠧ")])
        os.environ[bstack1lllll1_opy_ (u"ࠩࡌࡗࡤࡔࡏࡏࡡࡅࡗ࡙ࡇࡃࡌࡡࡌࡒࡋࡘࡁࡠࡃ࠴࠵࡞ࡥࡓࡆࡕࡖࡍࡔࡔ⃮ࠧ")] = bstack1lllll1_opy_ (u"ࠪࡸࡷࡻࡥࠨ⃯")
        return bstack1ll1l1l111_opy_
      else:
        chrome_options = None
        if isinstance(bstack1ll1l1l111_opy_, ChromeOptions):
          chrome_options = bstack1ll1l1l111_opy_
        elif isinstance(bstack1ll1l1l111_opy_, dict):
          for value in bstack1ll1l1l111_opy_.values():
            if isinstance(value, ChromeOptions):
              chrome_options = value
              break
        if chrome_options is None:
          chrome_options = ChromeOptions()
          if isinstance(bstack1ll1l1l111_opy_, dict):
            bstack1ll1l1l111_opy_[bstack1lllll1_opy_ (u"ࠫࡴࡶࡴࡪࡱࡱࡷࠬ⃰")] = chrome_options
          else:
            bstack1ll1l1l111_opy_ = chrome_options
        if bstack1llll1ll11ll_opy_ is not None:
          if bstack1lllll1_opy_ (u"ࠬࡧࡲࡨࡵࠪ⃱") in bstack1llll1ll11ll_opy_:
                bstack1llll1lll11l_opy_ = chrome_options.arguments or []
                new_args = bstack1llll1ll11ll_opy_[bstack1lllll1_opy_ (u"࠭ࡡࡳࡩࡶࠫ⃲")]
                for arg in new_args:
                    if arg not in bstack1llll1lll11l_opy_:
                        chrome_options.add_argument(arg)
          if bstack1lllll1_opy_ (u"ࠧࡦࡺࡷࡩࡳࡹࡩࡰࡰࡶࠫ⃳") in bstack1llll1ll11ll_opy_:
                existing_extensions = chrome_options.experimental_options.get(bstack1lllll1_opy_ (u"ࠨࡧࡻࡸࡪࡴࡳࡪࡱࡱࡷࠬ⃴"), [])
                bstack1lllll11llll_opy_ = bstack1llll1ll11ll_opy_[bstack1lllll1_opy_ (u"ࠩࡨࡼࡹ࡫࡮ࡴ࡫ࡲࡲࡸ࠭⃵")]
                for extension in bstack1lllll11llll_opy_:
                    if extension not in existing_extensions:
                        chrome_options.add_encoded_extension(extension)
          if bstack1lllll1_opy_ (u"ࠪࡴࡷ࡫ࡦࡴࠩ⃶") in bstack1llll1ll11ll_opy_:
                bstack1llll1llllll_opy_ = chrome_options.experimental_options.get(bstack1lllll1_opy_ (u"ࠫࡵࡸࡥࡧࡵࠪ⃷"), {})
                bstack1lllll111l11_opy_ = bstack1llll1ll11ll_opy_[bstack1lllll1_opy_ (u"ࠬࡶࡲࡦࡨࡶࠫ⃸")]
                bstack111l1l1l1ll_opy_(bstack1llll1llllll_opy_, bstack1lllll111l11_opy_)
                chrome_options.add_experimental_option(bstack1lllll1_opy_ (u"࠭ࡰࡳࡧࡩࡷࠬ⃹"), bstack1llll1llllll_opy_)
        os.environ[bstack1lllll1_opy_ (u"ࠧࡊࡕࡢࡒࡔࡔ࡟ࡃࡕࡗࡅࡈࡑ࡟ࡊࡐࡉࡖࡆࡥࡁ࠲࠳࡜ࡣࡘࡋࡓࡔࡋࡒࡒࠬ⃺")] = bstack1lllll1_opy_ (u"ࠨࡶࡵࡹࡪ࠭⃻")
        return bstack1ll1l1l111_opy_
    except Exception as e:
      logger.error(bstack1lllll1_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡹ࡫࡭ࡱ࡫ࠠࡢࡦࡧ࡭ࡳ࡭ࠠ࡯ࡱࡱ࠱ࡇ࡙ࠠࡪࡰࡩࡶࡦࠦࡡ࠲࠳ࡼࠤࡨ࡮ࡲࡰ࡯ࡨࠤࡴࡶࡴࡪࡱࡱࡷ࠿ࠦࠢ⃼") + str(e))
      return bstack1ll1l1l111_opy_