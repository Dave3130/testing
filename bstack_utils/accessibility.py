# coding: UTF-8
import sys
bstack1_opy_ = sys.version_info [0] == 2
bstack11l1ll1_opy_ = 2048
bstack1l1l1ll_opy_ = 7
def bstack11l1l11_opy_ (bstack111l1ll_opy_):
    global bstack1l1lll1_opy_
    bstack1l1l11_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack111l1l1_opy_ = bstack111l1ll_opy_ [:-1]
    bstack111ll_opy_ = bstack1l1l11_opy_ % len (bstack111l1l1_opy_)
    bstack11l11l1_opy_ = bstack111l1l1_opy_ [:bstack111ll_opy_] + bstack111l1l1_opy_ [bstack111ll_opy_:]
    if bstack1_opy_:
        bstack1111l1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    else:
        bstack1111l1l_opy_ = str () .join ([chr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    return eval (bstack1111l1l_opy_)
import os
import json
import requests
import logging
import threading
import bstack_utils.constants as bstack1llll1lll1ll_opy_
from urllib.parse import urlparse
from bstack_utils.constants import bstack11l1l1l1ll1_opy_ as bstack1llll1llll11_opy_, EVENTS
from bstack_utils.bstack11l1ll11ll_opy_ import bstack11l1ll11ll_opy_
from bstack_utils.helper import bstack1ll1ll11_opy_, bstack1ll1l111_opy_, bstack1l1l11l1ll_opy_, bstack111l11lll1l_opy_, \
  bstack111l11ll111_opy_, bstack11l11l1111_opy_, get_host_info, bstack1111ll11l1l_opy_, bstack11lll1llll_opy_, error_handler, bstack1111l1lll1l_opy_, bstack1111ll1l11l_opy_, bstack11lll111_opy_
from browserstack_sdk._version import __version__
from bstack_utils.bstack1ll1111ll_opy_ import get_logger
from bstack_utils.bstack1l1l1111ll_opy_ import bstack111111111l_opy_
from selenium.webdriver.chrome.options import Options as ChromeOptions
from browserstack_sdk.sdk_cli.cli import cli
from bstack_utils.constants import *
logger = get_logger(__name__)
bstack1l1l1111ll_opy_ = bstack111111111l_opy_()
@error_handler(class_method=False)
def _1lllll11l1l1_opy_(driver, bstack111l1111_opy_):
  response = {}
  try:
    caps = driver.capabilities
    response = {
        bstack11l1l11_opy_ (u"ࠧࡰࡵࡢࡲࡦࡳࡥࠨ᾿"): caps.get(bstack11l1l11_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡑࡥࡲ࡫ࠧ῀"), None),
        bstack11l1l11_opy_ (u"ࠩࡲࡷࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭῁"): bstack111l1111_opy_.get(bstack11l1l11_opy_ (u"ࠪࡳࡸ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ῂ"), None),
        bstack11l1l11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡤࡴࡡ࡮ࡧࠪῃ"): caps.get(bstack11l1l11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪῄ"), None),
        bstack11l1l11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨ῅"): caps.get(bstack11l1l11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨῆ"), None)
    }
  except Exception as error:
    logger.debug(bstack11l1l11_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡧࡧࡷࡧ࡭࡯࡮ࡨࠢࡳࡰࡦࡺࡦࡰࡴࡰࠤࡩ࡫ࡴࡢ࡫࡯ࡷࠥࡽࡩࡵࡪࠣࡩࡷࡸ࡯ࡳࠢ࠽ࠤࠬῇ") + str(error))
  return response
def on():
    if os.environ.get(bstack11l1l11_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧῈ"), None) is None or os.environ[bstack11l1l11_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨΈ")] == bstack11l1l11_opy_ (u"ࠦࡳࡻ࡬࡭ࠤῊ"):
        return False
    return True
def bstack111l1111l_opy_(config):
  return config.get(bstack11l1l11_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬΉ"), False) or any([p.get(bstack11l1l11_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ῌ"), False) == True for p in config.get(bstack11l1l11_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ῍"), [])])
def bstack11l11ll1l_opy_(config, bstack11111l11l_opy_):
  try:
    bstack1lllll11111l_opy_ = config.get(bstack11l1l11_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ῎"), False)
    if int(bstack11111l11l_opy_) < len(config.get(bstack11l1l11_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ῏"), [])) and config[bstack11l1l11_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ῐ")][bstack11111l11l_opy_]:
      bstack1lllll11ll1l_opy_ = config[bstack11l1l11_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧῑ")][bstack11111l11l_opy_].get(bstack11l1l11_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬῒ"), None)
    else:
      bstack1lllll11ll1l_opy_ = config.get(bstack11l1l11_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ΐ"), None)
    if bstack1lllll11ll1l_opy_ != None:
      bstack1lllll11111l_opy_ = bstack1lllll11ll1l_opy_
    bstack1lllll11lll1_opy_ = os.getenv(bstack11l1l11_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠬ῔")) is not None and len(os.getenv(bstack11l1l11_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭῕"))) > 0 and os.getenv(bstack11l1l11_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧῖ")) != bstack11l1l11_opy_ (u"ࠪࡲࡺࡲ࡬ࠨῗ")
    return bstack1lllll11111l_opy_ and bstack1lllll11lll1_opy_
  except Exception as error:
    logger.debug(bstack11l1l11_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡺࡪࡸࡩࡧࡻ࡬ࡲ࡬ࠦࡴࡩࡧࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡷࡪࡹࡳࡪࡱࡱࠤࡼ࡯ࡴࡩࠢࡨࡶࡷࡵࡲࠡ࠼ࠣࠫῘ") + str(error))
  return False
def bstack111111l1l_opy_(test_tags):
  bstack1l1111l1lll_opy_ = os.getenv(bstack11l1l11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡡࡄࡇࡈࡋࡓࡔࡋࡅࡍࡑࡏࡔ࡚ࡡࡆࡓࡓࡌࡉࡈࡗࡕࡅ࡙ࡏࡏࡏࡡ࡜ࡑࡑ࠭Ῑ"))
  if bstack1l1111l1lll_opy_ is None:
    return True
  bstack1l1111l1lll_opy_ = json.loads(bstack1l1111l1lll_opy_)
  try:
    include_tags = bstack1l1111l1lll_opy_[bstack11l1l11_opy_ (u"࠭ࡩ࡯ࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫῚ")] if bstack11l1l11_opy_ (u"ࠧࡪࡰࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩࠬΊ") in bstack1l1111l1lll_opy_ and isinstance(bstack1l1111l1lll_opy_[bstack11l1l11_opy_ (u"ࠨ࡫ࡱࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ࠭῜")], list) else []
    exclude_tags = bstack1l1111l1lll_opy_[bstack11l1l11_opy_ (u"ࠩࡨࡼࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧ῝")] if bstack11l1l11_opy_ (u"ࠪࡩࡽࡩ࡬ࡶࡦࡨࡘࡦ࡭ࡳࡊࡰࡗࡩࡸࡺࡩ࡯ࡩࡖࡧࡴࡶࡥࠨ῞") in bstack1l1111l1lll_opy_ and isinstance(bstack1l1111l1lll_opy_[bstack11l1l11_opy_ (u"ࠫࡪࡾࡣ࡭ࡷࡧࡩ࡙ࡧࡧࡴࡋࡱࡘࡪࡹࡴࡪࡰࡪࡗࡨࡵࡰࡦࠩ῟")], list) else []
    excluded = any(tag in exclude_tags for tag in test_tags)
    included = len(include_tags) == 0 or any(tag in include_tags for tag in test_tags)
    return not excluded and included
  except Exception as error:
    logger.debug(bstack11l1l11_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡺࡦࡲࡩࡥࡣࡷ࡭ࡳ࡭ࠠࡵࡧࡶࡸࠥࡩࡡࡴࡧࠣࡪࡴࡸࠠࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡣࡧࡩࡳࡷ࡫ࠠࡴࡥࡤࡲࡳ࡯࡮ࡨ࠰ࠣࡉࡷࡸ࡯ࡳࠢ࠽ࠤࠧῠ") + str(error))
  return False
def bstack1lllll111l11_opy_(config, frameworkName, bstack1llll1ll11l1_opy_, bstack1llll1lll11l_opy_):
  bstack1lllll111lll_opy_ = bstack111l11lll1l_opy_(config)
  bstack1llll1ll11ll_opy_ = bstack111l11ll111_opy_(config)
  if bstack1lllll111lll_opy_ is None or bstack1llll1ll11ll_opy_ is None:
    logger.error(bstack11l1l11_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡺ࡬࡮ࡲࡥࠡࡥࡵࡩࡦࡺࡩ࡯ࡩࠣࡸࡪࡹࡴࠡࡴࡸࡲࠥ࡬࡯ࡳࠢࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲ࠿ࠦࡍࡪࡵࡶ࡭ࡳ࡭ࠠࡢࡷࡷ࡬ࡪࡴࡴࡪࡥࡤࡸ࡮ࡵ࡮ࠡࡶࡲ࡯ࡪࡴࠧῡ"))
    return [None, None]
  try:
    settings = json.loads(os.getenv(bstack11l1l11_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡣࡆࡉࡃࡆࡕࡖࡍࡇࡏࡌࡊࡖ࡜ࡣࡈࡕࡎࡇࡋࡊ࡙ࡗࡇࡔࡊࡑࡑࡣ࡞ࡓࡌࠨῢ"), bstack11l1l11_opy_ (u"ࠨࡽࢀࠫΰ")))
    data = {
        bstack11l1l11_opy_ (u"ࠩࡳࡶࡴࡰࡥࡤࡶࡑࡥࡲ࡫ࠧῤ"): config[bstack11l1l11_opy_ (u"ࠪࡴࡷࡵࡪࡦࡥࡷࡒࡦࡳࡥࠨῥ")],
        bstack11l1l11_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧῦ"): config.get(bstack11l1l11_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨῧ"), os.path.basename(os.getcwd())),
        bstack11l1l11_opy_ (u"࠭ࡳࡵࡣࡵࡸ࡙࡯࡭ࡦࠩῨ"): bstack1ll1ll11_opy_(),
        bstack11l1l11_opy_ (u"ࠧࡥࡧࡶࡧࡷ࡯ࡰࡵ࡫ࡲࡲࠬῩ"): config.get(bstack11l1l11_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡄࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࠫῪ"), bstack11l1l11_opy_ (u"ࠩࠪΎ")),
        bstack11l1l11_opy_ (u"ࠪࡷࡴࡻࡲࡤࡧࠪῬ"): {
            bstack11l1l11_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࡎࡢ࡯ࡨࠫ῭"): frameworkName,
            bstack11l1l11_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡗࡧࡵࡷ࡮ࡵ࡮ࠨ΅"): bstack1llll1ll11l1_opy_,
            bstack11l1l11_opy_ (u"࠭ࡳࡥ࡭࡙ࡩࡷࡹࡩࡰࡰࠪ`"): __version__,
            bstack11l1l11_opy_ (u"ࠧ࡭ࡣࡱ࡫ࡺࡧࡧࡦࠩ῰"): bstack11l1l11_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨ῱"),
            bstack11l1l11_opy_ (u"ࠩࡷࡩࡸࡺࡆࡳࡣࡰࡩࡼࡵࡲ࡬ࠩῲ"): bstack11l1l11_opy_ (u"ࠪࡷࡪࡲࡥ࡯࡫ࡸࡱࠬῳ"),
            bstack11l1l11_opy_ (u"ࠫࡹ࡫ࡳࡵࡈࡵࡥࡲ࡫ࡷࡰࡴ࡮࡚ࡪࡸࡳࡪࡱࡱࠫῴ"): bstack1llll1lll11l_opy_
        },
        bstack11l1l11_opy_ (u"ࠬࡹࡥࡵࡶ࡬ࡲ࡬ࡹࠧ῵"): settings,
        bstack11l1l11_opy_ (u"࠭ࡶࡦࡴࡶ࡭ࡴࡴࡃࡰࡰࡷࡶࡴࡲࠧῶ"): bstack1111ll11l1l_opy_(),
        bstack11l1l11_opy_ (u"ࠧࡤ࡫ࡌࡲ࡫ࡵࠧῷ"): bstack11l11l1111_opy_(),
        bstack11l1l11_opy_ (u"ࠨࡪࡲࡷࡹࡏ࡮ࡧࡱࠪῸ"): get_host_info(),
        bstack11l1l11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫΌ"): bstack1l1l11l1ll_opy_(config)
    }
    headers = {
        bstack11l1l11_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱࡙ࡿࡰࡦࠩῺ"): bstack11l1l11_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧΏ"),
    }
    config = {
        bstack11l1l11_opy_ (u"ࠬࡧࡵࡵࡪࠪῼ"): (bstack1lllll111lll_opy_, bstack1llll1ll11ll_opy_),
        bstack11l1l11_opy_ (u"࠭ࡨࡦࡣࡧࡩࡷࡹࠧ´"): headers
    }
    response = bstack11lll1llll_opy_(bstack11l1l11_opy_ (u"ࠧࡑࡑࡖࡘࠬ῾"), bstack1llll1llll11_opy_ + bstack11l1l11_opy_ (u"ࠨ࠱ࡹ࠶࠴ࡺࡥࡴࡶࡢࡶࡺࡴࡳࠨ῿"), data, config)
    bstack1llll1llllll_opy_ = response.json()
    if bstack1llll1llllll_opy_[bstack11l1l11_opy_ (u"ࠩࡶࡹࡨࡩࡥࡴࡵࠪ ")]:
      parsed = json.loads(os.getenv(bstack11l1l11_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚࡟ࡂࡅࡆࡉࡘ࡙ࡉࡃࡋࡏࡍ࡙࡟࡟ࡄࡑࡑࡊࡎࡍࡕࡓࡃࡗࡍࡔࡔ࡟࡚ࡏࡏࠫ "), bstack11l1l11_opy_ (u"ࠫࢀࢃࠧ ")))
      parsed[bstack11l1l11_opy_ (u"ࠬࡹࡣࡢࡰࡱࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ ")] = bstack1llll1llllll_opy_[bstack11l1l11_opy_ (u"࠭ࡤࡢࡶࡤࠫ ")][bstack11l1l11_opy_ (u"ࠧࡴࡥࡤࡲࡳ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨ ")]
      os.environ[bstack11l1l11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡤࡇࡃࡄࡇࡖࡗࡎࡈࡉࡍࡋࡗ࡝ࡤࡉࡏࡏࡈࡌࡋ࡚ࡘࡁࡕࡋࡒࡒࡤ࡟ࡍࡍࠩ ")] = json.dumps(parsed)
      bstack11l1ll11ll_opy_.bstack1ll11ll11l_opy_(bstack1llll1llllll_opy_[bstack11l1l11_opy_ (u"ࠩࡧࡥࡹࡧࠧ ")][bstack11l1l11_opy_ (u"ࠪࡷࡨࡸࡩࡱࡶࡶࠫ ")])
      bstack11l1ll11ll_opy_.bstack1lllll1l1111_opy_(bstack1llll1llllll_opy_[bstack11l1l11_opy_ (u"ࠫࡩࡧࡴࡢࠩ ")][bstack11l1l11_opy_ (u"ࠬࡩ࡯࡮࡯ࡤࡲࡩࡹࠧ ")])
      bstack11l1ll11ll_opy_.store()
      return bstack1llll1llllll_opy_[bstack11l1l11_opy_ (u"࠭ࡤࡢࡶࡤࠫ​")][bstack11l1l11_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡔࡰ࡭ࡨࡲࠬ‌")], bstack1llll1llllll_opy_[bstack11l1l11_opy_ (u"ࠨࡦࡤࡸࡦ࠭‍")][bstack11l1l11_opy_ (u"ࠩ࡬ࡨࠬ‎")]
    else:
      logger.error(bstack11l1l11_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡷࡩ࡫࡯ࡩࠥࡸࡵ࡯ࡰ࡬ࡲ࡬ࠦࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯࠼ࠣࠫ‏") + bstack1llll1llllll_opy_[bstack11l1l11_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ‐")])
      if bstack1llll1llllll_opy_[bstack11l1l11_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭‑")] == bstack11l1l11_opy_ (u"࠭ࡉ࡯ࡸࡤࡰ࡮ࡪࠠࡤࡱࡱࡪ࡮࡭ࡵࡳࡣࡷ࡭ࡴࡴࠠࡱࡣࡶࡷࡪࡪ࠮ࠨ‒"):
        for bstack1lllll1111ll_opy_ in bstack1llll1llllll_opy_[bstack11l1l11_opy_ (u"ࠧࡦࡴࡵࡳࡷࡹࠧ–")]:
          logger.error(bstack1lllll1111ll_opy_[bstack11l1l11_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ—")])
      return None, None
  except Exception as error:
    logger.error(bstack11l1l11_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡽࡨࡪ࡮ࡨࠤࡨࡸࡥࡢࡶ࡬ࡲ࡬ࠦࡴࡦࡵࡷࠤࡷࡻ࡮ࠡࡨࡲࡶࠥࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮࠻ࠢࠥ―") +  str(error))
    return None, None
def bstack1llll1lll111_opy_():
  if os.getenv(bstack11l1l11_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨ‖")) is None:
    return {
        bstack11l1l11_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫ‗"): bstack11l1l11_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫ‘"),
        bstack11l1l11_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ’"): bstack11l1l11_opy_ (u"ࠧࡃࡷ࡬ࡰࡩࠦࡣࡳࡧࡤࡸ࡮ࡵ࡮ࠡࡪࡤࡨࠥ࡬ࡡࡪ࡮ࡨࡨ࠳࠭‚")
    }
  data = {bstack11l1l11_opy_ (u"ࠨࡧࡱࡨ࡙࡯࡭ࡦࠩ‛"): bstack1ll1ll11_opy_()}
  headers = {
      bstack11l1l11_opy_ (u"ࠩࡄࡹࡹ࡮࡯ࡳ࡫ࡽࡥࡹ࡯࡯࡯ࠩ“"): bstack11l1l11_opy_ (u"ࠪࡆࡪࡧࡲࡦࡴࠣࠫ”") + os.getenv(bstack11l1l11_opy_ (u"ࠦࡇ࡙࡟ࡂ࠳࠴࡝ࡤࡐࡗࡕࠤ„")),
      bstack11l1l11_opy_ (u"ࠬࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡔࡺࡲࡨࠫ‟"): bstack11l1l11_opy_ (u"࠭ࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳࡯ࡹ࡯࡯ࠩ†")
  }
  response = bstack11lll1llll_opy_(bstack11l1l11_opy_ (u"ࠧࡑࡗࡗࠫ‡"), bstack1llll1llll11_opy_ + bstack11l1l11_opy_ (u"ࠨ࠱ࡷࡩࡸࡺ࡟ࡳࡷࡱࡷ࠴ࡹࡴࡰࡲࠪ•"), data, { bstack11l1l11_opy_ (u"ࠩ࡫ࡩࡦࡪࡥࡳࡵࠪ‣"): headers })
  try:
    if response.status_code == 200:
      logger.info(bstack11l1l11_opy_ (u"ࠥࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡔࡦࡵࡷࠤࡗࡻ࡮ࠡ࡯ࡤࡶࡰ࡫ࡤࠡࡣࡶࠤࡨࡵ࡭ࡱ࡮ࡨࡸࡪࡪࠠࡢࡶࠣࠦ․") + bstack1ll1l111_opy_().isoformat() + bstack11l1l11_opy_ (u"ࠫ࡟࠭‥"))
      return {bstack11l1l11_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬ…"): bstack11l1l11_opy_ (u"࠭ࡳࡶࡥࡦࡩࡸࡹࠧ‧"), bstack11l1l11_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ "): bstack11l1l11_opy_ (u"ࠨࠩ ")}
    else:
      response.raise_for_status()
  except requests.RequestException as error:
    logger.error(bstack11l1l11_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡽࡨࡪ࡮ࡨࠤࡲࡧࡲ࡬࡫ࡱ࡫ࠥࡩ࡯࡮ࡲ࡯ࡩࡹ࡯࡯࡯ࠢࡲࡪࠥࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡖࡨࡷࡹࠦࡒࡶࡰ࠽ࠤࠧ‪") + str(error))
    return {
        bstack11l1l11_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪ‫"): bstack11l1l11_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪ‬"),
        bstack11l1l11_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭‭"): str(error)
    }
def bstack1llll1ll1l1l_opy_(bstack1lllll111ll1_opy_):
    return re.match(bstack11l1l11_opy_ (u"ࡸࠧ࡟࡞ࡧ࠯࠭ࡢ࠮࡝ࡦ࠮࠭ࡄࠪࠧ‮"), bstack1lllll111ll1_opy_.strip()) is not None
def bstack1ll1ll1l1_opy_(caps, options, desired_capabilities={}, config=None):
    try:
        if options:
          bstack1llll1llll1l_opy_ = options.to_capabilities()
        elif desired_capabilities:
          bstack1llll1llll1l_opy_ = desired_capabilities
        else:
          bstack1llll1llll1l_opy_ = {}
        bstack1l111llll1l_opy_ = (bstack1llll1llll1l_opy_.get(bstack11l1l11_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡐࡤࡱࡪ࠭ "), bstack11l1l11_opy_ (u"ࠨࠩ‰")).lower() or caps.get(bstack11l1l11_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡒࡦࡳࡥࠨ‱"), bstack11l1l11_opy_ (u"ࠪࠫ′")).lower())
        if bstack1l111llll1l_opy_ == bstack11l1l11_opy_ (u"ࠫ࡮ࡵࡳࠨ″"):
            return True
        if bstack1l111llll1l_opy_ == bstack11l1l11_opy_ (u"ࠬࡧ࡮ࡥࡴࡲ࡭ࡩ࠭‴"):
            bstack1l111l11l11_opy_ = str(float(caps.get(bstack11l1l11_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠨ‵")) or bstack1llll1llll1l_opy_.get(bstack11l1l11_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨ‶"), {}).get(bstack11l1l11_opy_ (u"ࠨࡱࡶ࡚ࡪࡸࡳࡪࡱࡱࠫ‷"),bstack11l1l11_opy_ (u"ࠩࠪ‸"))))
            if bstack1l111llll1l_opy_ == bstack11l1l11_opy_ (u"ࠪࡥࡳࡪࡲࡰ࡫ࡧࠫ‹") and int(bstack1l111l11l11_opy_.split(bstack11l1l11_opy_ (u"ࠫ࠳࠭›"))[0]) < float(bstack11l1l1l1lll_opy_):
                logger.warning(str(bstack11l1l111ll1_opy_))
                return False
            return True
        bstack1l111l111ll_opy_ = caps.get(bstack11l1l11_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭※"), {}).get(bstack11l1l11_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪࡔࡡ࡮ࡧࠪ‼"), caps.get(bstack11l1l11_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࠧ‽"), bstack11l1l11_opy_ (u"ࠨࠩ‾")))
        if bstack1l111l111ll_opy_:
            logger.warning(bstack11l1l11_opy_ (u"ࠤࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡷࡪ࡮࡯ࠤࡷࡻ࡮ࠡࡱࡱࡰࡾࠦ࡯࡯ࠢࡇࡩࡸࡱࡴࡰࡲࠣࡦࡷࡵࡷࡴࡧࡵࡷ࠳ࠨ‿"))
            return False
        browser = caps.get(bstack11l1l11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨ⁀"), bstack11l1l11_opy_ (u"ࠫࠬ⁁")).lower() or bstack1llll1llll1l_opy_.get(bstack11l1l11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪ⁂"), bstack11l1l11_opy_ (u"࠭ࠧ⁃")).lower()
        if browser != bstack11l1l11_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࠧ⁄"):
            logger.warning(bstack11l1l11_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡽࡩ࡭࡮ࠣࡶࡺࡴࠠࡰࡰ࡯ࡽࠥࡵ࡮ࠡࡅ࡫ࡶࡴࡳࡥࠡࡤࡵࡳࡼࡹࡥࡳࡵ࠱ࠦ⁅"))
            return False
        browser_version = caps.get(bstack11l1l11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪ⁆")) or caps.get(bstack11l1l11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬ⁇")) or bstack1llll1llll1l_opy_.get(bstack11l1l11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬ⁈")) or bstack1llll1llll1l_opy_.get(bstack11l1l11_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭⁉"), {}).get(bstack11l1l11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧ⁊")) or bstack1llll1llll1l_opy_.get(bstack11l1l11_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨ⁋"), {}).get(bstack11l1l11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡹࡩࡷࡹࡩࡰࡰࠪ⁌"))
        bstack1l111l11ll1_opy_ = bstack1llll1lll1ll_opy_.bstack1l111l1lll1_opy_
        bstack1lllll1111l1_opy_ = False
        if config is not None:
          bstack1lllll1111l1_opy_ = bstack11l1l11_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭⁍") in config and str(config[bstack11l1l11_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧ⁎")]).lower() != bstack11l1l11_opy_ (u"ࠫ࡫ࡧ࡬ࡴࡧࠪ⁏")
        if os.environ.get(bstack11l1l11_opy_ (u"ࠬࡏࡓࡠࡐࡒࡒࡤࡈࡓࡕࡃࡆࡏࡤࡏࡎࡇࡔࡄࡣࡆ࠷࠱࡚ࡡࡖࡉࡘ࡙ࡉࡐࡐࠪ⁐"), bstack11l1l11_opy_ (u"࠭ࠧ⁑")).lower() == bstack11l1l11_opy_ (u"ࠧࡵࡴࡸࡩࠬ⁒") or bstack1lllll1111l1_opy_:
          bstack1l111l11ll1_opy_ = bstack1llll1lll1ll_opy_.bstack1l1111ll1ll_opy_
        if browser_version and browser_version != bstack11l1l11_opy_ (u"ࠨ࡮ࡤࡸࡪࡹࡴࠨ⁓") and int(browser_version.split(bstack11l1l11_opy_ (u"ࠩ࠱ࠫ⁔"))[0]) <= bstack1l111l11ll1_opy_:
          logger.warning(bstack1llll1111_opy_ (u"ࠪࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡸ࡫࡯ࡰࠥࡸࡵ࡯ࠢࡲࡲࡱࡿࠠࡰࡰࠣࡇ࡭ࡸ࡯࡮ࡧࠣࡦࡷࡵࡷࡴࡧࡵࠤࡻ࡫ࡲࡴ࡫ࡲࡲࠥ࡭ࡲࡦࡣࡷࡩࡷࠦࡴࡩࡣࡱࠤࢀࡳࡩ࡯ࡡࡤ࠵࠶ࡿ࡟ࡴࡷࡳࡴࡴࡸࡴࡦࡦࡢࡧ࡭ࡸ࡯࡮ࡧࡢࡺࡪࡸࡳࡪࡱࡱࢁ࠳࠭⁕"))
          return False
        if not options:
          bstack1l111ll1ll1_opy_ = caps.get(bstack11l1l11_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩ⁖")) or bstack1llll1llll1l_opy_.get(bstack11l1l11_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ⁗"), {})
          if bstack11l1l11_opy_ (u"࠭࠭࠮ࡪࡨࡥࡩࡲࡥࡴࡵࠪ⁘") in bstack1l111ll1ll1_opy_.get(bstack11l1l11_opy_ (u"ࠧࡢࡴࡪࡷࠬ⁙"), []):
              logger.warning(bstack11l1l11_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡽࡩ࡭࡮ࠣࡲࡴࡺࠠࡳࡷࡱࠤࡴࡴࠠ࡭ࡧࡪࡥࡨࡿࠠࡩࡧࡤࡨࡱ࡫ࡳࡴࠢࡰࡳࡩ࡫࠮ࠡࡕࡺ࡭ࡹࡩࡨࠡࡶࡲࠤࡳ࡫ࡷࠡࡪࡨࡥࡩࡲࡥࡴࡵࠣࡱࡴࡪࡥࠡࡱࡵࠤࡦࡼ࡯ࡪࡦࠣࡹࡸ࡯࡮ࡨࠢ࡫ࡩࡦࡪ࡬ࡦࡵࡶࠤࡲࡵࡤࡦ࠰ࠥ⁚"))
              return False
        return True
    except Exception as error:
        logger.debug(bstack11l1l11_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡸࡤࡰ࡮ࡪࡡࡵࡧࠣࡥ࠶࠷ࡹࠡࡵࡸࡴࡵࡵࡲࡵࠢ࠽ࠦ⁛") + str(error))
        return False
def set_capabilities(caps, config):
  try:
    bstack1l1l111ll1l_opy_ = config.get(bstack11l1l11_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪ⁜"), {})
    bstack1l1l111ll1l_opy_[bstack11l1l11_opy_ (u"ࠫࡦࡻࡴࡩࡖࡲ࡯ࡪࡴࠧ⁝")] = os.getenv(bstack11l1l11_opy_ (u"ࠬࡈࡓࡠࡃ࠴࠵࡞ࡥࡊࡘࡖࠪ⁞"))
    bstack1111l1ll1ll_opy_ = json.loads(os.getenv(bstack11l1l11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡢࡅࡈࡉࡅࡔࡕࡌࡆࡎࡒࡉࡕ࡛ࡢࡇࡔࡔࡆࡊࡉࡘࡖࡆ࡚ࡉࡐࡐࡢ࡝ࡒࡒࠧ "), bstack11l1l11_opy_ (u"ࠧࡼࡿࠪ⁠"))).get(bstack11l1l11_opy_ (u"ࠨࡵࡦࡥࡳࡴࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩ⁡"))
    if not config[bstack11l1l11_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡑࡴࡲࡨࡺࡩࡴࡎࡣࡳࠫ⁢")].get(bstack11l1l11_opy_ (u"ࠥࡥࡵࡶ࡟ࡢࡷࡷࡳࡲࡧࡴࡦࠤ⁣")):
      if bstack11l1l11_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬ⁤") in caps:
        caps[bstack11l1l11_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭⁥")][bstack11l1l11_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭⁦")] = bstack1l1l111ll1l_opy_
        caps[bstack11l1l11_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨ⁧")][bstack11l1l11_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨ⁨")][bstack11l1l11_opy_ (u"ࠩࡶࡧࡦࡴ࡮ࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪ⁩")] = bstack1111l1ll1ll_opy_
      else:
        caps[bstack11l1l11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩ⁪")] = bstack1l1l111ll1l_opy_
        caps[bstack11l1l11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪ⁫")][bstack11l1l11_opy_ (u"ࠬࡹࡣࡢࡰࡱࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭⁬")] = bstack1111l1ll1ll_opy_
  except Exception as error:
    logger.debug(bstack11l1l11_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡺ࡬࡮ࡲࡥࠡࡵࡨࡸࡹ࡯࡮ࡨࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷ࠳ࠦࡅࡳࡴࡲࡶ࠿ࠦࠢ⁭") +  str(error))
def bstack11l111111_opy_(driver, bstack1lllll11l1ll_opy_):
  try:
    setattr(driver, bstack11l1l11_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡁ࠲࠳ࡼࡗ࡭ࡵࡵ࡭ࡦࡖࡧࡦࡴࠧ⁮"), True)
    session = driver.session_id
    if session:
      bstack1llll1lll1l1_opy_ = True
      current_url = driver.current_url
      try:
        url = urlparse(current_url)
      except Exception as e:
        bstack1llll1lll1l1_opy_ = False
      bstack1llll1lll1l1_opy_ = url.scheme in [bstack11l1l11_opy_ (u"ࠣࡪࡷࡸࡵࠨ⁯"), bstack11l1l11_opy_ (u"ࠤ࡫ࡸࡹࡶࡳࠣ⁰")]
      if bstack1llll1lll1l1_opy_:
        if bstack1lllll11l1ll_opy_:
          logger.info(bstack11l1l11_opy_ (u"ࠥࡗࡪࡺࡵࡱࠢࡩࡳࡷࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡴࡦࡵࡷ࡭ࡳ࡭ࠠࡩࡣࡶࠤࡸࡺࡡࡳࡶࡨࡨ࠳ࠦࡁࡶࡶࡲࡱࡦࡺࡥࠡࡶࡨࡷࡹࠦࡣࡢࡵࡨࠤࡪࡾࡥࡤࡷࡷ࡭ࡴࡴࠠࡸ࡫࡯ࡰࠥࡨࡥࡨ࡫ࡱࠤࡲࡵ࡭ࡦࡰࡷࡥࡷ࡯࡬ࡺ࠰ࠥⁱ"))
      return bstack1lllll11l1ll_opy_
  except Exception as e:
    logger.error(bstack11l1l11_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡷࡹࡧࡲࡵ࡫ࡱ࡫ࠥࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡶࡧࡦࡴࠠࡧࡱࡵࠤࡹ࡮ࡩࡴࠢࡷࡩࡸࡺࠠࡤࡣࡶࡩ࠿ࠦࠢ⁲") + str(e))
    return False
def bstack11l11l1l_opy_(driver, name, path):
  try:
    bstack1l111lll1l1_opy_ = {
        bstack11l1l11_opy_ (u"ࠬࡺࡨࡕࡧࡶࡸࡗࡻ࡮ࡖࡷ࡬ࡨࠬ⁳"): threading.current_thread().current_test_uuid,
        bstack11l1l11_opy_ (u"࠭ࡴࡩࡄࡸ࡭ࡱࡪࡕࡶ࡫ࡧࠫ⁴"): os.environ.get(bstack11l1l11_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬ⁵"), bstack11l1l11_opy_ (u"ࠨࠩ⁶")),
        bstack11l1l11_opy_ (u"ࠩࡷ࡬ࡏࡽࡴࡕࡱ࡮ࡩࡳ࠭⁷"): os.environ.get(bstack11l1l11_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢࡎ࡜࡚ࠧ⁸"), bstack11l1l11_opy_ (u"ࠫࠬ⁹"))
    }
    bstack1ll11lll11l_opy_ = bstack1l1l1111ll_opy_.bstack1ll1111llll_opy_(EVENTS.bstack11ll11ll11_opy_.value)
    logger.debug(bstack11l1l11_opy_ (u"ࠬࡖࡥࡳࡨࡲࡶࡲ࡯࡮ࡨࠢࡶࡧࡦࡴࠠࡣࡧࡩࡳࡷ࡫ࠠࡴࡣࡹ࡭ࡳ࡭ࠠࡳࡧࡶࡹࡱࡺࡳࠨ⁺"))
    try:
      if (bstack11lll111_opy_(threading.current_thread(), bstack11l1l11_opy_ (u"࠭ࡩࡴࡃࡳࡴࡆ࠷࠱ࡺࡖࡨࡷࡹ࠭⁻"), None) and bstack11lll111_opy_(threading.current_thread(), bstack11l1l11_opy_ (u"ࠧࡢࡲࡳࡅ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩ⁼"), None)):
        scripts = {bstack11l1l11_opy_ (u"ࠨࡵࡦࡥࡳ࠭⁽"): bstack11l1ll11ll_opy_.perform_scan}
        bstack1lllll111111_opy_ = json.loads(scripts[bstack11l1l11_opy_ (u"ࠤࡶࡧࡦࡴࠢ⁾")].replace(bstack11l1l11_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࠨⁿ"), bstack11l1l11_opy_ (u"ࠦࠧ₀")))
        bstack1lllll111111_opy_[bstack11l1l11_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨ₁")][bstack11l1l11_opy_ (u"࠭࡭ࡦࡶ࡫ࡳࡩ࠭₂")] = None
        scripts[bstack11l1l11_opy_ (u"ࠢࡴࡥࡤࡲࠧ₃")] = bstack11l1l11_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࠦ₄") + json.dumps(bstack1lllll111111_opy_)
        bstack11l1ll11ll_opy_.bstack1ll11ll11l_opy_(scripts)
        bstack11l1ll11ll_opy_.store()
        logger.debug(driver.execute_script(bstack11l1ll11ll_opy_.perform_scan))
      else:
        logger.debug(driver.execute_async_script(bstack11l1ll11ll_opy_.perform_scan, {bstack11l1l11_opy_ (u"ࠤࡰࡩࡹ࡮࡯ࡥࠤ₅"): name}))
      bstack1l1l1111ll_opy_.end(EVENTS.bstack11ll11ll11_opy_.value, bstack1ll11lll11l_opy_ + bstack11l1l11_opy_ (u"ࠥ࠾ࡸࡺࡡࡳࡶࠥ₆"), bstack1ll11lll11l_opy_ + bstack11l1l11_opy_ (u"ࠦ࠿࡫࡮ࡥࠤ₇"), True, None)
    except Exception as error:
      bstack1l1l1111ll_opy_.end(EVENTS.bstack11ll11ll11_opy_.value, bstack1ll11lll11l_opy_ + bstack11l1l11_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧ₈"), bstack1ll11lll11l_opy_ + bstack11l1l11_opy_ (u"ࠨ࠺ࡦࡰࡧࠦ₉"), False, str(error))
    bstack1ll11lll11l_opy_ = bstack1l1l1111ll_opy_.bstack11ll1ll111l_opy_(EVENTS.bstack1l111ll111l_opy_.value)
    bstack1l1l1111ll_opy_.mark(bstack1ll11lll11l_opy_ + bstack11l1l11_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢ₊"))
    try:
      if (bstack11lll111_opy_(threading.current_thread(), bstack11l1l11_opy_ (u"ࠨ࡫ࡶࡅࡵࡶࡁ࠲࠳ࡼࡘࡪࡹࡴࠨ₋"), None) and bstack11lll111_opy_(threading.current_thread(), bstack11l1l11_opy_ (u"ࠩࡤࡴࡵࡇ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫ₌"), None)):
        scripts = {bstack11l1l11_opy_ (u"ࠪࡷࡨࡧ࡮ࠨ₍"): bstack11l1ll11ll_opy_.perform_scan}
        bstack1lllll111111_opy_ = json.loads(scripts[bstack11l1l11_opy_ (u"ࠦࡸࡩࡡ࡯ࠤ₎")].replace(bstack11l1l11_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࠣ₏"), bstack11l1l11_opy_ (u"ࠨࠢₐ")))
        bstack1lllll111111_opy_[bstack11l1l11_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪₑ")][bstack11l1l11_opy_ (u"ࠨ࡯ࡨࡸ࡭ࡵࡤࠨₒ")] = None
        scripts[bstack11l1l11_opy_ (u"ࠤࡶࡧࡦࡴࠢₓ")] = bstack11l1l11_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࠨₔ") + json.dumps(bstack1lllll111111_opy_)
        bstack11l1ll11ll_opy_.bstack1ll11ll11l_opy_(scripts)
        bstack11l1ll11ll_opy_.store()
        logger.debug(driver.execute_script(bstack11l1ll11ll_opy_.perform_scan))
      else:
        logger.debug(driver.execute_async_script(bstack11l1ll11ll_opy_.bstack1lllll1l111l_opy_, bstack1l111lll1l1_opy_))
      bstack1l1l1111ll_opy_.end(bstack1ll11lll11l_opy_, bstack1ll11lll11l_opy_ + bstack11l1l11_opy_ (u"ࠦ࠿ࡹࡴࡢࡴࡷࠦₕ"), bstack1ll11lll11l_opy_ + bstack11l1l11_opy_ (u"ࠧࡀࡥ࡯ࡦࠥₖ"),True, None)
    except Exception as error:
      bstack1l1l1111ll_opy_.end(bstack1ll11lll11l_opy_, bstack1ll11lll11l_opy_ + bstack11l1l11_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨₗ"), bstack1ll11lll11l_opy_ + bstack11l1l11_opy_ (u"ࠢ࠻ࡧࡱࡨࠧₘ"),False, str(error))
    logger.info(bstack11l1l11_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡶࡨࡷࡹ࡯࡮ࡨࠢࡩࡳࡷࠦࡴࡩ࡫ࡶࠤࡹ࡫ࡳࡵࠢࡦࡥࡸ࡫ࠠࡩࡣࡶࠤࡪࡴࡤࡦࡦ࠱ࠦₙ"))
  except Exception as bstack1l111ll1111_opy_:
    logger.error(bstack11l1l11_opy_ (u"ࠤࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡵࡩࡸࡻ࡬ࡵࡵࠣࡧࡴࡻ࡬ࡥࠢࡱࡳࡹࠦࡢࡦࠢࡳࡶࡴࡩࡥࡴࡵࡨࡨࠥ࡬࡯ࡳࠢࡷ࡬ࡪࠦࡴࡦࡵࡷࠤࡨࡧࡳࡦ࠼ࠣࠦₚ") + str(path) + bstack11l1l11_opy_ (u"ࠥࠤࡊࡸࡲࡰࡴࠣ࠾ࠧₛ") + str(bstack1l111ll1111_opy_))
def bstack1llll1lllll1_opy_(driver):
    caps = driver.capabilities
    if caps.get(bstack11l1l11_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲࡔࡡ࡮ࡧࠥₜ")) and str(caps.get(bstack11l1l11_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࡎࡢ࡯ࡨࠦ₝"))).lower() == bstack11l1l11_opy_ (u"ࠨࡡ࡯ࡦࡵࡳ࡮ࡪࠢ₞"):
        bstack1l111l11l11_opy_ = caps.get(bstack11l1l11_opy_ (u"ࠢࡢࡲࡳ࡭ࡺࡳ࠺ࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠤ₟")) or caps.get(bstack11l1l11_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࡙ࡩࡷࡹࡩࡰࡰࠥ₠"))
        if bstack1l111l11l11_opy_ and int(str(bstack1l111l11l11_opy_)) < bstack11l1l1l1lll_opy_:
            return False
    return True
def bstack1llllll11l_opy_(config):
  if bstack11l1l11_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ₡") in config:
        return config[bstack11l1l11_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ₢")]
  for platform in config.get(bstack11l1l11_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ₣"), []):
      if bstack11l1l11_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ₤") in platform:
          return platform[bstack11l1l11_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭₥")]
  return None
def bstack1lll1l11ll_opy_(bstack11ll111l11_opy_):
  try:
    browser_name = bstack11ll111l11_opy_[bstack11l1l11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡰࡤࡱࡪ࠭₦")]
    browser_version = bstack11ll111l11_opy_[bstack11l1l11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡹࡩࡷࡹࡩࡰࡰࠪ₧")]
    chrome_options = bstack11ll111l11_opy_[bstack11l1l11_opy_ (u"ࠩࡦ࡬ࡷࡵ࡭ࡦࡡࡲࡴࡹ࡯࡯࡯ࡵࠪ₨")]
    try:
        bstack1lllll111l1l_opy_ = int(browser_version.split(bstack11l1l11_opy_ (u"ࠪ࠲ࠬ₩"))[0])
    except ValueError as e:
        logger.error(bstack11l1l11_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡯࡬ࡦࠢࡦࡳࡳࡼࡥࡳࡶ࡬ࡲ࡬ࠦࡢࡳࡱࡺࡷࡪࡸࠠࡷࡧࡵࡷ࡮ࡵ࡮ࠣ₪") + str(e))
        return False
    if not (browser_name and browser_name.lower() == bstack11l1l11_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࠬ₫")):
        logger.warning(bstack11l1l11_opy_ (u"ࠨࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡻ࡮ࡲ࡬ࠡࡴࡸࡲࠥࡵ࡮࡭ࡻࠣࡳࡳࠦࡃࡩࡴࡲࡱࡪࠦࡢࡳࡱࡺࡷࡪࡸࡳ࠯ࠤ€"))
        return False
    if bstack1lllll111l1l_opy_ < bstack1llll1lll1ll_opy_.bstack1l1111ll1ll_opy_:
        logger.warning(bstack1llll1111_opy_ (u"ࠧࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡷ࡫ࡱࡶ࡫ࡵࡩࡸࠦࡃࡩࡴࡲࡱࡪࠦࡶࡦࡴࡶ࡭ࡴࡴࠠࡼࡅࡒࡒࡘ࡚ࡁࡏࡖࡖ࠲ࡒࡏࡎࡊࡏࡘࡑࡤࡔࡏࡏࡡࡅࡗ࡙ࡇࡃࡌࡡࡌࡒࡋࡘࡁࡠࡃ࠴࠵࡞ࡥࡓࡖࡒࡓࡓࡗ࡚ࡅࡅࡡࡆࡌࡗࡕࡍࡆࡡ࡙ࡉࡗ࡙ࡉࡐࡐࢀࠤࡴࡸࠠࡩ࡫ࡪ࡬ࡪࡸ࠮ࠨ₭"))
        return False
    if chrome_options and any(bstack11l1l11_opy_ (u"ࠨ࠯࠰࡬ࡪࡧࡤ࡭ࡧࡶࡷࠬ₮") in value for value in chrome_options.values() if isinstance(value, str)):
        logger.warning(bstack11l1l11_opy_ (u"ࠤࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡷࡪ࡮࡯ࠤࡳࡵࡴࠡࡴࡸࡲࠥࡵ࡮ࠡ࡮ࡨ࡫ࡦࡩࡹࠡࡪࡨࡥࡩࡲࡥࡴࡵࠣࡱࡴࡪࡥ࠯ࠢࡖࡻ࡮ࡺࡣࡩࠢࡷࡳࠥࡴࡥࡸࠢ࡫ࡩࡦࡪ࡬ࡦࡵࡶࠤࡲࡵࡤࡦࠢࡲࡶࠥࡧࡶࡰ࡫ࡧࠤࡺࡹࡩ࡯ࡩࠣ࡬ࡪࡧࡤ࡭ࡧࡶࡷࠥࡳ࡯ࡥࡧ࠱ࠦ₯"))
        return False
    return True
  except Exception as e:
    logger.error(bstack11l1l11_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡩࡨࡦࡥ࡮࡭ࡳ࡭ࠠࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࠢࡶࡹࡵࡶ࡯ࡳࡶࠣࡪࡴࡸࠠ࡭ࡱࡦࡥࡱࠦࡃࡩࡴࡲࡱࡪࡀࠠࠣ₰") + str(e))
    return False
def bstack11l1l1lll1_opy_(bstack111l1l1111_opy_, config):
    try:
      bstack1l111l1llll_opy_ = bstack11l1l11_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ₱") in config and config[bstack11l1l11_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ₲")] == True
      bstack1lllll1111l1_opy_ = bstack11l1l11_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪ₳") in config and str(config[bstack11l1l11_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫ₴")]).lower() != bstack11l1l11_opy_ (u"ࠨࡨࡤࡰࡸ࡫ࠧ₵")
      if not (bstack1l111l1llll_opy_ and (not bstack1l1l11l1ll_opy_(config) or bstack1lllll1111l1_opy_)):
        return bstack111l1l1111_opy_
      bstack1llll1ll1ll1_opy_ = bstack11l1ll11ll_opy_.bstack1lllll1l11ll_opy_
      if bstack1llll1ll1ll1_opy_ is None:
        logger.debug(bstack11l1l11_opy_ (u"ࠤࡊࡳࡴ࡭࡬ࡦࠢࡦ࡬ࡷࡵ࡭ࡦࠢࡲࡴࡹ࡯࡯࡯ࡵࠣࡥࡷ࡫ࠠࡏࡱࡱࡩࠧ₶"))
        return bstack111l1l1111_opy_
      bstack1lllll11ll11_opy_ = int(str(bstack1111ll1l11l_opy_()).split(bstack11l1l11_opy_ (u"ࠪ࠲ࠬ₷"))[0])
      logger.debug(bstack11l1l11_opy_ (u"ࠦࡘ࡫࡬ࡦࡰ࡬ࡹࡲࠦࡶࡦࡴࡶ࡭ࡴࡴࠠࡥࡧࡷࡩࡨࡺࡥࡥ࠼ࠣࠦ₸") + str(bstack1lllll11ll11_opy_) + bstack11l1l11_opy_ (u"ࠧࠨ₹"))
      if bstack1lllll11ll11_opy_ == 3 and isinstance(bstack111l1l1111_opy_, dict) and bstack11l1l11_opy_ (u"࠭ࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠭₺") in bstack111l1l1111_opy_ and bstack1llll1ll1ll1_opy_ is not None:
        if bstack11l1l11_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬ₻") not in bstack111l1l1111_opy_[bstack11l1l11_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨ₼")]:
          bstack111l1l1111_opy_[bstack11l1l11_opy_ (u"ࠩࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩ₽")][bstack11l1l11_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨ₾")] = {}
        if bstack11l1l11_opy_ (u"ࠫࡦࡸࡧࡴࠩ₿") in bstack1llll1ll1ll1_opy_:
          if bstack11l1l11_opy_ (u"ࠬࡧࡲࡨࡵࠪ⃀") not in bstack111l1l1111_opy_[bstack11l1l11_opy_ (u"࠭ࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠭⃁")][bstack11l1l11_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬ⃂")]:
            bstack111l1l1111_opy_[bstack11l1l11_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨ⃃")][bstack11l1l11_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ⃄")][bstack11l1l11_opy_ (u"ࠪࡥࡷ࡭ࡳࠨ⃅")] = []
          for arg in bstack1llll1ll1ll1_opy_[bstack11l1l11_opy_ (u"ࠫࡦࡸࡧࡴࠩ⃆")]:
            if arg not in bstack111l1l1111_opy_[bstack11l1l11_opy_ (u"ࠬࡪࡥࡴ࡫ࡵࡩࡩࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠬ⃇")][bstack11l1l11_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫ⃈")][bstack11l1l11_opy_ (u"ࠧࡢࡴࡪࡷࠬ⃉")]:
              bstack111l1l1111_opy_[bstack11l1l11_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨ⃊")][bstack11l1l11_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ⃋")][bstack11l1l11_opy_ (u"ࠪࡥࡷ࡭ࡳࠨ⃌")].append(arg)
        if bstack11l1l11_opy_ (u"ࠫࡪࡾࡴࡦࡰࡶ࡭ࡴࡴࡳࠨ⃍") in bstack1llll1ll1ll1_opy_:
          if bstack11l1l11_opy_ (u"ࠬ࡫ࡸࡵࡧࡱࡷ࡮ࡵ࡮ࡴࠩ⃎") not in bstack111l1l1111_opy_[bstack11l1l11_opy_ (u"࠭ࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠭⃏")][bstack11l1l11_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬ⃐")]:
            bstack111l1l1111_opy_[bstack11l1l11_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨ⃑")][bstack11l1l11_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹ⃒ࠧ")][bstack11l1l11_opy_ (u"ࠪࡩࡽࡺࡥ࡯ࡵ࡬ࡳࡳࡹ⃓ࠧ")] = []
          for ext in bstack1llll1ll1ll1_opy_[bstack11l1l11_opy_ (u"ࠫࡪࡾࡴࡦࡰࡶ࡭ࡴࡴࡳࠨ⃔")]:
            if ext not in bstack111l1l1111_opy_[bstack11l1l11_opy_ (u"ࠬࡪࡥࡴ࡫ࡵࡩࡩࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠬ⃕")][bstack11l1l11_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫ⃖")][bstack11l1l11_opy_ (u"ࠧࡦࡺࡷࡩࡳࡹࡩࡰࡰࡶࠫ⃗")]:
              bstack111l1l1111_opy_[bstack11l1l11_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨ⃘")][bstack11l1l11_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹ⃙ࠧ")][bstack11l1l11_opy_ (u"ࠪࡩࡽࡺࡥ࡯ࡵ࡬ࡳࡳࡹ⃚ࠧ")].append(ext)
        if bstack11l1l11_opy_ (u"ࠫࡵࡸࡥࡧࡵࠪ⃛") in bstack1llll1ll1ll1_opy_:
          if bstack11l1l11_opy_ (u"ࠬࡶࡲࡦࡨࡶࠫ⃜") not in bstack111l1l1111_opy_[bstack11l1l11_opy_ (u"࠭ࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠭⃝")][bstack11l1l11_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬ⃞")]:
            bstack111l1l1111_opy_[bstack11l1l11_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨ⃟")][bstack11l1l11_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ⃠")][bstack11l1l11_opy_ (u"ࠪࡴࡷ࡫ࡦࡴࠩ⃡")] = {}
          bstack1111l1lll1l_opy_(bstack111l1l1111_opy_[bstack11l1l11_opy_ (u"ࠫࡩ࡫ࡳࡪࡴࡨࡨࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠫ⃢")][bstack11l1l11_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ⃣")][bstack11l1l11_opy_ (u"࠭ࡰࡳࡧࡩࡷࠬ⃤")],
                    bstack1llll1ll1ll1_opy_[bstack11l1l11_opy_ (u"ࠧࡱࡴࡨࡪࡸ⃥࠭")])
        os.environ[bstack11l1l11_opy_ (u"ࠨࡋࡖࡣࡓࡕࡎࡠࡄࡖࡘࡆࡉࡋࡠࡋࡑࡊࡗࡇ࡟ࡂ࠳࠴࡝ࡤ࡙ࡅࡔࡕࡌࡓࡓ⃦࠭")] = bstack11l1l11_opy_ (u"ࠩࡷࡶࡺ࡫ࠧ⃧")
        return bstack111l1l1111_opy_
      else:
        chrome_options = None
        if isinstance(bstack111l1l1111_opy_, ChromeOptions):
          chrome_options = bstack111l1l1111_opy_
        elif isinstance(bstack111l1l1111_opy_, dict):
          for value in bstack111l1l1111_opy_.values():
            if isinstance(value, ChromeOptions):
              chrome_options = value
              break
        if chrome_options is None:
          chrome_options = ChromeOptions()
          if isinstance(bstack111l1l1111_opy_, dict):
            bstack111l1l1111_opy_[bstack11l1l11_opy_ (u"ࠪࡳࡵࡺࡩࡰࡰࡶ⃨ࠫ")] = chrome_options
          else:
            bstack111l1l1111_opy_ = chrome_options
        if bstack1llll1ll1ll1_opy_ is not None:
          if bstack11l1l11_opy_ (u"ࠫࡦࡸࡧࡴࠩ⃩") in bstack1llll1ll1ll1_opy_:
                bstack1lllll11l111_opy_ = chrome_options.arguments or []
                new_args = bstack1llll1ll1ll1_opy_[bstack11l1l11_opy_ (u"ࠬࡧࡲࡨࡵ⃪ࠪ")]
                for arg in new_args:
                    if arg not in bstack1lllll11l111_opy_:
                        chrome_options.add_argument(arg)
          if bstack11l1l11_opy_ (u"࠭ࡥࡹࡶࡨࡲࡸ࡯࡯࡯ࡵ⃫ࠪ") in bstack1llll1ll1ll1_opy_:
                existing_extensions = chrome_options.experimental_options.get(bstack11l1l11_opy_ (u"ࠧࡦࡺࡷࡩࡳࡹࡩࡰࡰࡶ⃬ࠫ"), [])
                bstack1llll1ll1l11_opy_ = bstack1llll1ll1ll1_opy_[bstack11l1l11_opy_ (u"ࠨࡧࡻࡸࡪࡴࡳࡪࡱࡱࡷ⃭ࠬ")]
                for extension in bstack1llll1ll1l11_opy_:
                    if extension not in existing_extensions:
                        chrome_options.add_encoded_extension(extension)
          if bstack11l1l11_opy_ (u"ࠩࡳࡶࡪ࡬ࡳࠨ⃮") in bstack1llll1ll1ll1_opy_:
                bstack1llll1ll1lll_opy_ = chrome_options.experimental_options.get(bstack11l1l11_opy_ (u"ࠪࡴࡷ࡫ࡦࡴ⃯ࠩ"), {})
                bstack1lllll11l11l_opy_ = bstack1llll1ll1ll1_opy_[bstack11l1l11_opy_ (u"ࠫࡵࡸࡥࡧࡵࠪ⃰")]
                bstack1111l1lll1l_opy_(bstack1llll1ll1lll_opy_, bstack1lllll11l11l_opy_)
                chrome_options.add_experimental_option(bstack11l1l11_opy_ (u"ࠬࡶࡲࡦࡨࡶࠫ⃱"), bstack1llll1ll1lll_opy_)
        os.environ[bstack11l1l11_opy_ (u"࠭ࡉࡔࡡࡑࡓࡓࡥࡂࡔࡖࡄࡇࡐࡥࡉࡏࡈࡕࡅࡤࡇ࠱࠲࡛ࡢࡗࡊ࡙ࡓࡊࡑࡑࠫ⃲")] = bstack11l1l11_opy_ (u"ࠧࡵࡴࡸࡩࠬ⃳")
        return bstack111l1l1111_opy_
    except Exception as e:
      logger.error(bstack11l1l11_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡸࡪ࡬ࡰࡪࠦࡡࡥࡦ࡬ࡲ࡬ࠦ࡮ࡰࡰ࠰ࡆࡘࠦࡩ࡯ࡨࡵࡥࠥࡧ࠱࠲ࡻࠣࡧ࡭ࡸ࡯࡮ࡧࠣࡳࡵࡺࡩࡰࡰࡶ࠾ࠥࠨ⃴") + str(e))
      return bstack111l1l1111_opy_