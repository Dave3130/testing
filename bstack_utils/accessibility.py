# coding: UTF-8
import sys
bstack1111l11_opy_ = sys.version_info [0] == 2
bstack11111l_opy_ = 2048
bstack1111111_opy_ = 7
def bstack11l111_opy_ (bstack1ll1l1_opy_):
    global bstack1llll1_opy_
    bstack1l1l1_opy_ = ord (bstack1ll1l1_opy_ [-1])
    bstack1lll1_opy_ = bstack1ll1l1_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1lll1_opy_)
    bstack1l1l111_opy_ = bstack1lll1_opy_ [:bstack1l1l11_opy_] + bstack1lll1_opy_ [bstack1l1l11_opy_:]
    if bstack1111l11_opy_:
        bstack1111lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11111l_opy_ - (bstack1llllll_opy_ + bstack1l1l1_opy_) % bstack1111111_opy_) for bstack1llllll_opy_, char in enumerate (bstack1l1l111_opy_)])
    else:
        bstack1111lll_opy_ = str () .join ([chr (ord (char) - bstack11111l_opy_ - (bstack1llllll_opy_ + bstack1l1l1_opy_) % bstack1111111_opy_) for bstack1llllll_opy_, char in enumerate (bstack1l1l111_opy_)])
    return eval (bstack1111lll_opy_)
import os
import json
import requests
import logging
import threading
import bstack_utils.constants as bstack1llll1lllll1_opy_
from urllib.parse import urlparse
from bstack_utils.constants import bstack11l11ll111l_opy_ as bstack1llll1ll1l11_opy_, EVENTS
from bstack_utils.bstack1l1l1ll111_opy_ import bstack1l1l1ll111_opy_
from bstack_utils.helper import bstack1llll111_opy_, bstack1l11l111_opy_, bstack1ll1l1l1ll_opy_, bstack111l1ll1ll1_opy_, \
  bstack111l1111l11_opy_, bstack1l11l111l_opy_, get_host_info, bstack111l1ll1l1l_opy_, bstack11ll11ll1l_opy_, error_handler, bstack1111lll1l1l_opy_, bstack1111ll11ll1_opy_, bstack1l11lll1_opy_
from browserstack_sdk._version import __version__
from bstack_utils.bstack1lll11ll11_opy_ import get_logger
from bstack_utils.bstack1ll1111111_opy_ import bstack1lllll111l1_opy_
from selenium.webdriver.chrome.options import Options as ChromeOptions
from browserstack_sdk.sdk_cli.cli import cli
from bstack_utils.constants import *
logger = get_logger(__name__)
bstack1ll1111111_opy_ = bstack1lllll111l1_opy_()
@error_handler(class_method=False)
def _1llll1ll1l1l_opy_(driver, bstack111l1l1l_opy_):
  response = {}
  try:
    caps = driver.capabilities
    response = {
        bstack11l111_opy_ (u"࠭࡯ࡴࡡࡱࡥࡲ࡫ࠧᾷ"): caps.get(bstack11l111_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡐࡤࡱࡪ࠭Ᾰ"), None),
        bstack11l111_opy_ (u"ࠨࡱࡶࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬᾹ"): bstack111l1l1l_opy_.get(bstack11l111_opy_ (u"ࠩࡲࡷ࡛࡫ࡲࡴ࡫ࡲࡲࠬᾺ"), None),
        bstack11l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡳࡧ࡭ࡦࠩΆ"): caps.get(bstack11l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩᾼ"), None),
        bstack11l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡥࡶࡦࡴࡶ࡭ࡴࡴࠧ᾽"): caps.get(bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧι"), None)
    }
  except Exception as error:
    logger.debug(bstack11l111_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡦࡦࡶࡦ࡬࡮ࡴࡧࠡࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࠣࡨࡪࡺࡡࡪ࡮ࡶࠤࡼ࡯ࡴࡩࠢࡨࡶࡷࡵࡲࠡ࠼ࠣࠫ᾿") + str(error))
  return response
def on():
    if os.environ.get(bstack11l111_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭῀"), None) is None or os.environ[bstack11l111_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧ῁")] == bstack11l111_opy_ (u"ࠥࡲࡺࡲ࡬ࠣῂ"):
        return False
    return True
def bstack1l1111llll_opy_(config):
  return config.get(bstack11l111_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫῃ"), False) or any([p.get(bstack11l111_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬῄ"), False) == True for p in config.get(bstack11l111_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ῅"), [])])
def bstack1ll1l1l111_opy_(config, bstack1l1lll1l1l_opy_):
  try:
    bstack1llll1lll11l_opy_ = config.get(bstack11l111_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧῆ"), False)
    if int(bstack1l1lll1l1l_opy_) < len(config.get(bstack11l111_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫῇ"), [])) and config[bstack11l111_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬῈ")][bstack1l1lll1l1l_opy_]:
      bstack1llll1ll11ll_opy_ = config[bstack11l111_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭Έ")][bstack1l1lll1l1l_opy_].get(bstack11l111_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫῊ"), None)
    else:
      bstack1llll1ll11ll_opy_ = config.get(bstack11l111_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬΉ"), None)
    if bstack1llll1ll11ll_opy_ != None:
      bstack1llll1lll11l_opy_ = bstack1llll1ll11ll_opy_
    bstack1lllll11l1ll_opy_ = os.getenv(bstack11l111_opy_ (u"࠭ࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗࠫῌ")) is not None and len(os.getenv(bstack11l111_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠬ῍"))) > 0 and os.getenv(bstack11l111_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭῎")) != bstack11l111_opy_ (u"ࠩࡱࡹࡱࡲࠧ῏")
    return bstack1llll1lll11l_opy_ and bstack1lllll11l1ll_opy_
  except Exception as error:
    logger.debug(bstack11l111_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡹࡩࡷ࡯ࡦࡺ࡫ࡱ࡫ࠥࡺࡨࡦࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡶࡩࡸࡹࡩࡰࡰࠣࡻ࡮ࡺࡨࠡࡧࡵࡶࡴࡸࠠ࠻ࠢࠪῐ") + str(error))
  return False
def bstack1l11111ll_opy_(test_tags):
  bstack1l1111ll1ll_opy_ = os.getenv(bstack11l111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡠࡃࡆࡇࡊ࡙ࡓࡊࡄࡌࡐࡎ࡚࡙ࡠࡅࡒࡒࡋࡏࡇࡖࡔࡄࡘࡎࡕࡎࡠ࡛ࡐࡐࠬῑ"))
  if bstack1l1111ll1ll_opy_ is None:
    return True
  bstack1l1111ll1ll_opy_ = json.loads(bstack1l1111ll1ll_opy_)
  try:
    include_tags = bstack1l1111ll1ll_opy_[bstack11l111_opy_ (u"ࠬ࡯࡮ࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪῒ")] if bstack11l111_opy_ (u"࠭ࡩ࡯ࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫΐ") in bstack1l1111ll1ll_opy_ and isinstance(bstack1l1111ll1ll_opy_[bstack11l111_opy_ (u"ࠧࡪࡰࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩࠬ῔")], list) else []
    exclude_tags = bstack1l1111ll1ll_opy_[bstack11l111_opy_ (u"ࠨࡧࡻࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ࠭῕")] if bstack11l111_opy_ (u"ࠩࡨࡼࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧῖ") in bstack1l1111ll1ll_opy_ and isinstance(bstack1l1111ll1ll_opy_[bstack11l111_opy_ (u"ࠪࡩࡽࡩ࡬ࡶࡦࡨࡘࡦ࡭ࡳࡊࡰࡗࡩࡸࡺࡩ࡯ࡩࡖࡧࡴࡶࡥࠨῗ")], list) else []
    excluded = any(tag in exclude_tags for tag in test_tags)
    included = len(include_tags) == 0 or any(tag in include_tags for tag in test_tags)
    return not excluded and included
  except Exception as error:
    logger.debug(bstack11l111_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡯࡬ࡦࠢࡹࡥࡱ࡯ࡤࡢࡶ࡬ࡲ࡬ࠦࡴࡦࡵࡷࠤࡨࡧࡳࡦࠢࡩࡳࡷࠦࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡢࡦࡨࡲࡶࡪࠦࡳࡤࡣࡱࡲ࡮ࡴࡧ࠯ࠢࡈࡶࡷࡵࡲࠡ࠼ࠣࠦῘ") + str(error))
  return False
def bstack1lllll11l1l1_opy_(config, frameworkName, bstack1llll1ll1lll_opy_, bstack1lllll111ll1_opy_):
  bstack1lllll111l11_opy_ = bstack111l1ll1ll1_opy_(config)
  bstack1llll1ll111l_opy_ = bstack111l1111l11_opy_(config)
  if bstack1lllll111l11_opy_ is None or bstack1llll1ll111l_opy_ is None:
    logger.error(bstack11l111_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡹ࡫࡭ࡱ࡫ࠠࡤࡴࡨࡥࡹ࡯࡮ࡨࠢࡷࡩࡸࡺࠠࡳࡷࡱࠤ࡫ࡵࡲࠡࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱ࠾ࠥࡓࡩࡴࡵ࡬ࡲ࡬ࠦࡡࡶࡶ࡫ࡩࡳࡺࡩࡤࡣࡷ࡭ࡴࡴࠠࡵࡱ࡮ࡩࡳ࠭Ῑ"))
    return [None, None]
  try:
    settings = json.loads(os.getenv(bstack11l111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡢࡅࡈࡉࡅࡔࡕࡌࡆࡎࡒࡉࡕ࡛ࡢࡇࡔࡔࡆࡊࡉࡘࡖࡆ࡚ࡉࡐࡐࡢ࡝ࡒࡒࠧῚ"), bstack11l111_opy_ (u"ࠧࡼࡿࠪΊ")))
    data = {
        bstack11l111_opy_ (u"ࠨࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪ࠭῜"): config[bstack11l111_opy_ (u"ࠩࡳࡶࡴࡰࡥࡤࡶࡑࡥࡲ࡫ࠧ῝")],
        bstack11l111_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭῞"): config.get(bstack11l111_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧ῟"), os.path.basename(os.getcwd())),
        bstack11l111_opy_ (u"ࠬࡹࡴࡢࡴࡷࡘ࡮ࡳࡥࠨῠ"): bstack1llll111_opy_(),
        bstack11l111_opy_ (u"࠭ࡤࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࠫῡ"): config.get(bstack11l111_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡊࡥࡴࡥࡵ࡭ࡵࡺࡩࡰࡰࠪῢ"), bstack11l111_opy_ (u"ࠨࠩΰ")),
        bstack11l111_opy_ (u"ࠩࡶࡳࡺࡸࡣࡦࠩῤ"): {
            bstack11l111_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡔࡡ࡮ࡧࠪῥ"): frameworkName,
            bstack11l111_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࡖࡦࡴࡶ࡭ࡴࡴࠧῦ"): bstack1llll1ll1lll_opy_,
            bstack11l111_opy_ (u"ࠬࡹࡤ࡬ࡘࡨࡶࡸ࡯࡯࡯ࠩῧ"): __version__,
            bstack11l111_opy_ (u"࠭࡬ࡢࡰࡪࡹࡦ࡭ࡥࠨῨ"): bstack11l111_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧῩ"),
            bstack11l111_opy_ (u"ࠨࡶࡨࡷࡹࡌࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨῪ"): bstack11l111_opy_ (u"ࠩࡶࡩࡱ࡫࡮ࡪࡷࡰࠫΎ"),
            bstack11l111_opy_ (u"ࠪࡸࡪࡹࡴࡇࡴࡤࡱࡪࡽ࡯ࡳ࡭࡙ࡩࡷࡹࡩࡰࡰࠪῬ"): bstack1lllll111ll1_opy_
        },
        bstack11l111_opy_ (u"ࠫࡸ࡫ࡴࡵ࡫ࡱ࡫ࡸ࠭῭"): settings,
        bstack11l111_opy_ (u"ࠬࡼࡥࡳࡵ࡬ࡳࡳࡉ࡯࡯ࡶࡵࡳࡱ࠭΅"): bstack111l1ll1l1l_opy_(),
        bstack11l111_opy_ (u"࠭ࡣࡪࡋࡱࡪࡴ࠭`"): bstack1l11l111l_opy_(),
        bstack11l111_opy_ (u"ࠧࡩࡱࡶࡸࡎࡴࡦࡰࠩ῰"): get_host_info(),
        bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠪ῱"): bstack1ll1l1l1ll_opy_(config)
    }
    headers = {
        bstack11l111_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡘࡾࡶࡥࠨῲ"): bstack11l111_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭ῳ"),
    }
    config = {
        bstack11l111_opy_ (u"ࠫࡦࡻࡴࡩࠩῴ"): (bstack1lllll111l11_opy_, bstack1llll1ll111l_opy_),
        bstack11l111_opy_ (u"ࠬ࡮ࡥࡢࡦࡨࡶࡸ࠭῵"): headers
    }
    response = bstack11ll11ll1l_opy_(bstack11l111_opy_ (u"࠭ࡐࡐࡕࡗࠫῶ"), bstack1llll1ll1l11_opy_ + bstack11l111_opy_ (u"ࠧ࠰ࡸ࠵࠳ࡹ࡫ࡳࡵࡡࡵࡹࡳࡹࠧῷ"), data, config)
    bstack1llll1lll1ll_opy_ = response.json()
    if bstack1llll1lll1ll_opy_[bstack11l111_opy_ (u"ࠨࡵࡸࡧࡨ࡫ࡳࡴࠩῸ")]:
      parsed = json.loads(os.getenv(bstack11l111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡥࡁࡄࡅࡈࡗࡘࡏࡂࡊࡎࡌࡘ࡞ࡥࡃࡐࡐࡉࡍࡌ࡛ࡒࡂࡖࡌࡓࡓࡥ࡙ࡎࡎࠪΌ"), bstack11l111_opy_ (u"ࠪࡿࢂ࠭Ὼ")))
      parsed[bstack11l111_opy_ (u"ࠫࡸࡩࡡ࡯ࡰࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬΏ")] = bstack1llll1lll1ll_opy_[bstack11l111_opy_ (u"ࠬࡪࡡࡵࡣࠪῼ")][bstack11l111_opy_ (u"࠭ࡳࡤࡣࡱࡲࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧ´")]
      os.environ[bstack11l111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡣࡆࡉࡃࡆࡕࡖࡍࡇࡏࡌࡊࡖ࡜ࡣࡈࡕࡎࡇࡋࡊ࡙ࡗࡇࡔࡊࡑࡑࡣ࡞ࡓࡌࠨ῾")] = json.dumps(parsed)
      bstack1l1l1ll111_opy_.bstack11ll11l1ll_opy_(bstack1llll1lll1ll_opy_[bstack11l111_opy_ (u"ࠨࡦࡤࡸࡦ࠭῿")][bstack11l111_opy_ (u"ࠩࡶࡧࡷ࡯ࡰࡵࡵࠪ ")])
      bstack1l1l1ll111_opy_.bstack1lllll1l11ll_opy_(bstack1llll1lll1ll_opy_[bstack11l111_opy_ (u"ࠪࡨࡦࡺࡡࠨ ")][bstack11l111_opy_ (u"ࠫࡨࡵ࡭࡮ࡣࡱࡨࡸ࠭ ")])
      bstack1l1l1ll111_opy_.store()
      return bstack1llll1lll1ll_opy_[bstack11l111_opy_ (u"ࠬࡪࡡࡵࡣࠪ ")][bstack11l111_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࡚࡯࡬ࡧࡱࠫ ")], bstack1llll1lll1ll_opy_[bstack11l111_opy_ (u"ࠧࡥࡣࡷࡥࠬ ")][bstack11l111_opy_ (u"ࠨ࡫ࡧࠫ ")]
    else:
      logger.error(bstack11l111_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡽࡨࡪ࡮ࡨࠤࡷࡻ࡮࡯࡫ࡱ࡫ࠥࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮࠻ࠢࠪ ") + bstack1llll1lll1ll_opy_[bstack11l111_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ ")])
      if bstack1llll1lll1ll_opy_[bstack11l111_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ ")] == bstack11l111_opy_ (u"ࠬࡏ࡮ࡷࡣ࡯࡭ࡩࠦࡣࡰࡰࡩ࡭࡬ࡻࡲࡢࡶ࡬ࡳࡳࠦࡰࡢࡵࡶࡩࡩ࠴ࠧ "):
        for bstack1lllll1111l1_opy_ in bstack1llll1lll1ll_opy_[bstack11l111_opy_ (u"࠭ࡥࡳࡴࡲࡶࡸ࠭​")]:
          logger.error(bstack1lllll1111l1_opy_[bstack11l111_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ‌")])
      return None, None
  except Exception as error:
    logger.error(bstack11l111_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡼ࡮ࡩ࡭ࡧࠣࡧࡷ࡫ࡡࡵ࡫ࡱ࡫ࠥࡺࡥࡴࡶࠣࡶࡺࡴࠠࡧࡱࡵࠤࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࠺ࠡࠤ‍") +  str(error))
    return None, None
def bstack1llll1llllll_opy_():
  if os.getenv(bstack11l111_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧ‎")) is None:
    return {
        bstack11l111_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪ‏"): bstack11l111_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪ‐"),
        bstack11l111_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭‑"): bstack11l111_opy_ (u"࠭ࡂࡶ࡫࡯ࡨࠥࡩࡲࡦࡣࡷ࡭ࡴࡴࠠࡩࡣࡧࠤ࡫ࡧࡩ࡭ࡧࡧ࠲ࠬ‒")
    }
  data = {bstack11l111_opy_ (u"ࠧࡦࡰࡧࡘ࡮ࡳࡥࠨ–"): bstack1llll111_opy_()}
  headers = {
      bstack11l111_opy_ (u"ࠨࡃࡸࡸ࡭ࡵࡲࡪࡼࡤࡸ࡮ࡵ࡮ࠨ—"): bstack11l111_opy_ (u"ࠩࡅࡩࡦࡸࡥࡳࠢࠪ―") + os.getenv(bstack11l111_opy_ (u"ࠥࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠣ‖")),
      bstack11l111_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲࡚ࡹࡱࡧࠪ‗"): bstack11l111_opy_ (u"ࠬࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲࡮ࡸࡵ࡮ࠨ‘")
  }
  response = bstack11ll11ll1l_opy_(bstack11l111_opy_ (u"࠭ࡐࡖࡖࠪ’"), bstack1llll1ll1l11_opy_ + bstack11l111_opy_ (u"ࠧ࠰ࡶࡨࡷࡹࡥࡲࡶࡰࡶ࠳ࡸࡺ࡯ࡱࠩ‚"), data, { bstack11l111_opy_ (u"ࠨࡪࡨࡥࡩ࡫ࡲࡴࠩ‛"): headers })
  try:
    if response.status_code == 200:
      logger.info(bstack11l111_opy_ (u"ࠤࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲ࡚ࠥࡥࡴࡶࠣࡖࡺࡴࠠ࡮ࡣࡵ࡯ࡪࡪࠠࡢࡵࠣࡧࡴࡳࡰ࡭ࡧࡷࡩࡩࠦࡡࡵࠢࠥ“") + bstack1l11l111_opy_().isoformat() + bstack11l111_opy_ (u"ࠪ࡞ࠬ”"))
      return {bstack11l111_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫ„"): bstack11l111_opy_ (u"ࠬࡹࡵࡤࡥࡨࡷࡸ࠭‟"), bstack11l111_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ†"): bstack11l111_opy_ (u"ࠧࠨ‡")}
    else:
      response.raise_for_status()
  except requests.RequestException as error:
    logger.error(bstack11l111_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡼ࡮ࡩ࡭ࡧࠣࡱࡦࡸ࡫ࡪࡰࡪࠤࡨࡵ࡭ࡱ࡮ࡨࡸ࡮ࡵ࡮ࠡࡱࡩࠤࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡕࡧࡶࡸࠥࡘࡵ࡯࠼ࠣࠦ•") + str(error))
    return {
        bstack11l111_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩ‣"): bstack11l111_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩ․"),
        bstack11l111_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ‥"): str(error)
    }
def bstack1llll1ll1ll1_opy_(bstack1llll1ll1111_opy_):
    return re.match(bstack11l111_opy_ (u"ࡷ࠭࡞࡝ࡦ࠮ࠬࡡ࠴࡜ࡥ࠭ࠬࡃࠩ࠭…"), bstack1llll1ll1111_opy_.strip()) is not None
def bstack11lll111l1_opy_(caps, options, desired_capabilities={}, config=None):
    try:
        if options:
          bstack1llll1ll11l1_opy_ = options.to_capabilities()
        elif desired_capabilities:
          bstack1llll1ll11l1_opy_ = desired_capabilities
        else:
          bstack1llll1ll11l1_opy_ = {}
        bstack1l111ll1l1l_opy_ = (bstack1llll1ll11l1_opy_.get(bstack11l111_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡏࡣࡰࡩࠬ‧"), bstack11l111_opy_ (u"ࠧࠨ ")).lower() or caps.get(bstack11l111_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡑࡥࡲ࡫ࠧ "), bstack11l111_opy_ (u"ࠩࠪ‪")).lower())
        if bstack1l111ll1l1l_opy_ == bstack11l111_opy_ (u"ࠪ࡭ࡴࡹࠧ‫"):
            return True
        if bstack1l111ll1l1l_opy_ == bstack11l111_opy_ (u"ࠫࡦࡴࡤࡳࡱ࡬ࡨࠬ‬"):
            bstack1l111l1l111_opy_ = str(float(caps.get(bstack11l111_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡖࡦࡴࡶ࡭ࡴࡴࠧ‭")) or bstack1llll1ll11l1_opy_.get(bstack11l111_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧ‮"), {}).get(bstack11l111_opy_ (u"ࠧࡰࡵ࡙ࡩࡷࡹࡩࡰࡰࠪ "),bstack11l111_opy_ (u"ࠨࠩ‰"))))
            if bstack1l111ll1l1l_opy_ == bstack11l111_opy_ (u"ࠩࡤࡲࡩࡸ࡯ࡪࡦࠪ‱") and int(bstack1l111l1l111_opy_.split(bstack11l111_opy_ (u"ࠪ࠲ࠬ′"))[0]) < float(bstack11l1l1l11l1_opy_):
                logger.warning(str(bstack11l11ll1ll1_opy_))
                return False
            return True
        bstack1l1111lll11_opy_ = caps.get(bstack11l111_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬ″"), {}).get(bstack11l111_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࡓࡧ࡭ࡦࠩ‴"), caps.get(bstack11l111_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪ࠭‵"), bstack11l111_opy_ (u"ࠧࠨ‶")))
        if bstack1l1111lll11_opy_:
            logger.warning(bstack11l111_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡽࡩ࡭࡮ࠣࡶࡺࡴࠠࡰࡰ࡯ࡽࠥࡵ࡮ࠡࡆࡨࡷࡰࡺ࡯ࡱࠢࡥࡶࡴࡽࡳࡦࡴࡶ࠲ࠧ‷"))
            return False
        browser = caps.get(bstack11l111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧ‸"), bstack11l111_opy_ (u"ࠪࠫ‹")).lower() or bstack1llll1ll11l1_opy_.get(bstack11l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩ›"), bstack11l111_opy_ (u"ࠬ࠭※")).lower()
        if browser != bstack11l111_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪ࠭‼"):
            logger.warning(bstack11l111_opy_ (u"ࠢࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡼ࡯࡬࡭ࠢࡵࡹࡳࠦ࡯࡯࡮ࡼࠤࡴࡴࠠࡄࡪࡵࡳࡲ࡫ࠠࡣࡴࡲࡻࡸ࡫ࡲࡴ࠰ࠥ‽"))
            return False
        browser_version = caps.get(bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩ‾")) or caps.get(bstack11l111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡺࡪࡸࡳࡪࡱࡱࠫ‿")) or bstack1llll1ll11l1_opy_.get(bstack11l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫ⁀")) or bstack1llll1ll11l1_opy_.get(bstack11l111_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬ⁁"), {}).get(bstack11l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭⁂")) or bstack1llll1ll11l1_opy_.get(bstack11l111_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧ⁃"), {}).get(bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡸࡨࡶࡸ࡯࡯࡯ࠩ⁄"))
        bstack1l111l1lll1_opy_ = bstack1llll1lllll1_opy_.bstack1l111ll1l11_opy_
        bstack1lllll111111_opy_ = False
        if config is not None:
          bstack1lllll111111_opy_ = bstack11l111_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬ⁅") in config and str(config[bstack11l111_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭⁆")]).lower() != bstack11l111_opy_ (u"ࠪࡪࡦࡲࡳࡦࠩ⁇")
        if os.environ.get(bstack11l111_opy_ (u"ࠫࡎ࡙࡟ࡏࡑࡑࡣࡇ࡙ࡔࡂࡅࡎࡣࡎࡔࡆࡓࡃࡢࡅ࠶࠷࡙ࡠࡕࡈࡗࡘࡏࡏࡏࠩ⁈"), bstack11l111_opy_ (u"ࠬ࠭⁉")).lower() == bstack11l111_opy_ (u"࠭ࡴࡳࡷࡨࠫ⁊") or bstack1lllll111111_opy_:
          bstack1l111l1lll1_opy_ = bstack1llll1lllll1_opy_.bstack1l111llll11_opy_
        if browser_version and browser_version != bstack11l111_opy_ (u"ࠧ࡭ࡣࡷࡩࡸࡺࠧ⁋") and int(browser_version.split(bstack11l111_opy_ (u"ࠨ࠰ࠪ⁌"))[0]) <= bstack1l111l1lll1_opy_:
          logger.warning(bstack1lll1lll1ll_opy_ (u"ࠩࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡷࡪ࡮࡯ࠤࡷࡻ࡮ࠡࡱࡱࡰࡾࠦ࡯࡯ࠢࡆ࡬ࡷࡵ࡭ࡦࠢࡥࡶࡴࡽࡳࡦࡴࠣࡺࡪࡸࡳࡪࡱࡱࠤ࡬ࡸࡥࡢࡶࡨࡶࠥࡺࡨࡢࡰࠣࡿࡲ࡯࡮ࡠࡣ࠴࠵ࡾࡥࡳࡶࡲࡳࡳࡷࡺࡥࡥࡡࡦ࡬ࡷࡵ࡭ࡦࡡࡹࡩࡷࡹࡩࡰࡰࢀ࠲ࠬ⁍"))
          return False
        if not options:
          bstack1l1111ll111_opy_ = caps.get(bstack11l111_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨ⁎")) or bstack1llll1ll11l1_opy_.get(bstack11l111_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩ⁏"), {})
          if bstack11l111_opy_ (u"ࠬ࠳࠭ࡩࡧࡤࡨࡱ࡫ࡳࡴࠩ⁐") in bstack1l1111ll111_opy_.get(bstack11l111_opy_ (u"࠭ࡡࡳࡩࡶࠫ⁑"), []):
              logger.warning(bstack11l111_opy_ (u"ࠢࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡼ࡯࡬࡭ࠢࡱࡳࡹࠦࡲࡶࡰࠣࡳࡳࠦ࡬ࡦࡩࡤࡧࡾࠦࡨࡦࡣࡧࡰࡪࡹࡳࠡ࡯ࡲࡨࡪ࠴ࠠࡔࡹ࡬ࡸࡨ࡮ࠠࡵࡱࠣࡲࡪࡽࠠࡩࡧࡤࡨࡱ࡫ࡳࡴࠢࡰࡳࡩ࡫ࠠࡰࡴࠣࡥࡻࡵࡩࡥࠢࡸࡷ࡮ࡴࡧࠡࡪࡨࡥࡩࡲࡥࡴࡵࠣࡱࡴࡪࡥ࠯ࠤ⁒"))
              return False
        return True
    except Exception as error:
        logger.debug(bstack11l111_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡷࡣ࡯࡭ࡩࡧࡴࡦࠢࡤ࠵࠶ࡿࠠࡴࡷࡳࡴࡴࡸࡴࠡ࠼ࠥ⁓") + str(error))
        return False
def set_capabilities(caps, config):
  try:
    bstack1l1l1l1llll_opy_ = config.get(bstack11l111_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩ⁔"), {})
    bstack1l1l1l1llll_opy_[bstack11l111_opy_ (u"ࠪࡥࡺࡺࡨࡕࡱ࡮ࡩࡳ࠭⁕")] = os.getenv(bstack11l111_opy_ (u"ࠫࡇ࡙࡟ࡂ࠳࠴࡝ࡤࡐࡗࡕࠩ⁖"))
    bstack1111l1l111l_opy_ = json.loads(os.getenv(bstack11l111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡡࡄࡇࡈࡋࡓࡔࡋࡅࡍࡑࡏࡔ࡚ࡡࡆࡓࡓࡌࡉࡈࡗࡕࡅ࡙ࡏࡏࡏࡡ࡜ࡑࡑ࠭⁗"), bstack11l111_opy_ (u"࠭ࡻࡾࠩ⁘"))).get(bstack11l111_opy_ (u"ࠧࡴࡥࡤࡲࡳ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨ⁙"))
    if not config[bstack11l111_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡐࡳࡱࡧࡹࡨࡺࡍࡢࡲࠪ⁚")].get(bstack11l111_opy_ (u"ࠤࡤࡴࡵࡥࡡࡶࡶࡲࡱࡦࡺࡥࠣ⁛")):
      if bstack11l111_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫ⁜") in caps:
        caps[bstack11l111_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬ⁝")][bstack11l111_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬ⁞")] = bstack1l1l1l1llll_opy_
        caps[bstack11l111_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧ ")][bstack11l111_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧ⁠")][bstack11l111_opy_ (u"ࠨࡵࡦࡥࡳࡴࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩ⁡")] = bstack1111l1l111l_opy_
      else:
        caps[bstack11l111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨ⁢")] = bstack1l1l1l1llll_opy_
        caps[bstack11l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩ⁣")][bstack11l111_opy_ (u"ࠫࡸࡩࡡ࡯ࡰࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬ⁤")] = bstack1111l1l111l_opy_
  except Exception as error:
    logger.debug(bstack11l111_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡹ࡫࡭ࡱ࡫ࠠࡴࡧࡷࡸ࡮ࡴࡧࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶ࠲ࠥࡋࡲࡳࡱࡵ࠾ࠥࠨ⁥") +  str(error))
def bstack111l11lll1_opy_(driver, bstack1lllll11l111_opy_):
  try:
    setattr(driver, bstack11l111_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡇ࠱࠲ࡻࡖ࡬ࡴࡻ࡬ࡥࡕࡦࡥࡳ࠭⁦"), True)
    session = driver.session_id
    if session:
      bstack1llll1lll111_opy_ = True
      current_url = driver.current_url
      try:
        url = urlparse(current_url)
      except Exception as e:
        bstack1llll1lll111_opy_ = False
      bstack1llll1lll111_opy_ = url.scheme in [bstack11l111_opy_ (u"ࠢࡩࡶࡷࡴࠧ⁧"), bstack11l111_opy_ (u"ࠣࡪࡷࡸࡵࡹࠢ⁨")]
      if bstack1llll1lll111_opy_:
        if bstack1lllll11l111_opy_:
          logger.info(bstack11l111_opy_ (u"ࠤࡖࡩࡹࡻࡰࠡࡨࡲࡶࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡺࡥࡴࡶ࡬ࡲ࡬ࠦࡨࡢࡵࠣࡷࡹࡧࡲࡵࡧࡧ࠲ࠥࡇࡵࡵࡱࡰࡥࡹ࡫ࠠࡵࡧࡶࡸࠥࡩࡡࡴࡧࠣࡩࡽ࡫ࡣࡶࡶ࡬ࡳࡳࠦࡷࡪ࡮࡯ࠤࡧ࡫ࡧࡪࡰࠣࡱࡴࡳࡥ࡯ࡶࡤࡶ࡮ࡲࡹ࠯ࠤ⁩"))
      return bstack1lllll11l111_opy_
  except Exception as e:
    logger.error(bstack11l111_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡶࡸࡦࡸࡴࡪࡰࡪࠤࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡵࡦࡥࡳࠦࡦࡰࡴࠣࡸ࡭࡯ࡳࠡࡶࡨࡷࡹࠦࡣࡢࡵࡨ࠾ࠥࠨ⁪") + str(e))
    return False
def bstack11l11lll_opy_(driver, name, path):
  try:
    bstack1l111l1ll1l_opy_ = {
        bstack11l111_opy_ (u"ࠫࡹ࡮ࡔࡦࡵࡷࡖࡺࡴࡕࡶ࡫ࡧࠫ⁫"): threading.current_thread().current_test_uuid,
        bstack11l111_opy_ (u"ࠬࡺࡨࡃࡷ࡬ࡰࡩ࡛ࡵࡪࡦࠪ⁬"): os.environ.get(bstack11l111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫ⁭"), bstack11l111_opy_ (u"ࠧࠨ⁮")),
        bstack11l111_opy_ (u"ࠨࡶ࡫ࡎࡼࡺࡔࡰ࡭ࡨࡲࠬ⁯"): os.environ.get(bstack11l111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙࠭⁰"), bstack11l111_opy_ (u"ࠪࠫⁱ"))
    }
    bstack1ll11l1lll1_opy_ = bstack1ll1111111_opy_.bstack1ll1l1l111l_opy_(EVENTS.bstack111llll11l_opy_.value)
    logger.debug(bstack11l111_opy_ (u"ࠫࡕ࡫ࡲࡧࡱࡵࡱ࡮ࡴࡧࠡࡵࡦࡥࡳࠦࡢࡦࡨࡲࡶࡪࠦࡳࡢࡸ࡬ࡲ࡬ࠦࡲࡦࡵࡸࡰࡹࡹࠧ⁲"))
    try:
      if (bstack1l11lll1_opy_(threading.current_thread(), bstack11l111_opy_ (u"ࠬ࡯ࡳࡂࡲࡳࡅ࠶࠷ࡹࡕࡧࡶࡸࠬ⁳"), None) and bstack1l11lll1_opy_(threading.current_thread(), bstack11l111_opy_ (u"࠭ࡡࡱࡲࡄ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨ⁴"), None)):
        scripts = {bstack11l111_opy_ (u"ࠧࡴࡥࡤࡲࠬ⁵"): bstack1l1l1ll111_opy_.perform_scan}
        bstack1llll1lll1l1_opy_ = json.loads(scripts[bstack11l111_opy_ (u"ࠣࡵࡦࡥࡳࠨ⁶")].replace(bstack11l111_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࠧ⁷"), bstack11l111_opy_ (u"ࠥࠦ⁸")))
        bstack1llll1lll1l1_opy_[bstack11l111_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧ⁹")][bstack11l111_opy_ (u"ࠬࡳࡥࡵࡪࡲࡨࠬ⁺")] = None
        scripts[bstack11l111_opy_ (u"ࠨࡳࡤࡣࡱࠦ⁻")] = bstack11l111_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࠥ⁼") + json.dumps(bstack1llll1lll1l1_opy_)
        bstack1l1l1ll111_opy_.bstack11ll11l1ll_opy_(scripts)
        bstack1l1l1ll111_opy_.store()
        logger.debug(driver.execute_script(bstack1l1l1ll111_opy_.perform_scan))
      else:
        logger.debug(driver.execute_async_script(bstack1l1l1ll111_opy_.perform_scan, {bstack11l111_opy_ (u"ࠣ࡯ࡨࡸ࡭ࡵࡤࠣ⁽"): name}))
      bstack1ll1111111_opy_.end(EVENTS.bstack111llll11l_opy_.value, bstack1ll11l1lll1_opy_ + bstack11l111_opy_ (u"ࠤ࠽ࡷࡹࡧࡲࡵࠤ⁾"), bstack1ll11l1lll1_opy_ + bstack11l111_opy_ (u"ࠥ࠾ࡪࡴࡤࠣⁿ"), True, None)
    except Exception as error:
      bstack1ll1111111_opy_.end(EVENTS.bstack111llll11l_opy_.value, bstack1ll11l1lll1_opy_ + bstack11l111_opy_ (u"ࠦ࠿ࡹࡴࡢࡴࡷࠦ₀"), bstack1ll11l1lll1_opy_ + bstack11l111_opy_ (u"ࠧࡀࡥ࡯ࡦࠥ₁"), False, str(error))
    bstack1ll11l1lll1_opy_ = bstack1ll1111111_opy_.bstack11ll1l1llll_opy_(EVENTS.bstack1l111lll1ll_opy_.value)
    bstack1ll1111111_opy_.mark(bstack1ll11l1lll1_opy_ + bstack11l111_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨ₂"))
    try:
      if (bstack1l11lll1_opy_(threading.current_thread(), bstack11l111_opy_ (u"ࠧࡪࡵࡄࡴࡵࡇ࠱࠲ࡻࡗࡩࡸࡺࠧ₃"), None) and bstack1l11lll1_opy_(threading.current_thread(), bstack11l111_opy_ (u"ࠨࡣࡳࡴࡆ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪ₄"), None)):
        scripts = {bstack11l111_opy_ (u"ࠩࡶࡧࡦࡴࠧ₅"): bstack1l1l1ll111_opy_.perform_scan}
        bstack1llll1lll1l1_opy_ = json.loads(scripts[bstack11l111_opy_ (u"ࠥࡷࡨࡧ࡮ࠣ₆")].replace(bstack11l111_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࠢ₇"), bstack11l111_opy_ (u"ࠧࠨ₈")))
        bstack1llll1lll1l1_opy_[bstack11l111_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩ₉")][bstack11l111_opy_ (u"ࠧ࡮ࡧࡷ࡬ࡴࡪࠧ₊")] = None
        scripts[bstack11l111_opy_ (u"ࠣࡵࡦࡥࡳࠨ₋")] = bstack11l111_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࠧ₌") + json.dumps(bstack1llll1lll1l1_opy_)
        bstack1l1l1ll111_opy_.bstack11ll11l1ll_opy_(scripts)
        bstack1l1l1ll111_opy_.store()
        logger.debug(driver.execute_script(bstack1l1l1ll111_opy_.perform_scan))
      else:
        logger.debug(driver.execute_async_script(bstack1l1l1ll111_opy_.bstack1lllll1l1111_opy_, bstack1l111l1ll1l_opy_))
      bstack1ll1111111_opy_.end(bstack1ll11l1lll1_opy_, bstack1ll11l1lll1_opy_ + bstack11l111_opy_ (u"ࠥ࠾ࡸࡺࡡࡳࡶࠥ₍"), bstack1ll11l1lll1_opy_ + bstack11l111_opy_ (u"ࠦ࠿࡫࡮ࡥࠤ₎"),True, None)
    except Exception as error:
      bstack1ll1111111_opy_.end(bstack1ll11l1lll1_opy_, bstack1ll11l1lll1_opy_ + bstack11l111_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧ₏"), bstack1ll11l1lll1_opy_ + bstack11l111_opy_ (u"ࠨ࠺ࡦࡰࡧࠦₐ"),False, str(error))
    logger.info(bstack11l111_opy_ (u"ࠢࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡵࡧࡶࡸ࡮ࡴࡧࠡࡨࡲࡶࠥࡺࡨࡪࡵࠣࡸࡪࡹࡴࠡࡥࡤࡷࡪࠦࡨࡢࡵࠣࡩࡳࡪࡥࡥ࠰ࠥₑ"))
  except Exception as bstack1l111l11l1l_opy_:
    logger.error(bstack11l111_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡴࡨࡷࡺࡲࡴࡴࠢࡦࡳࡺࡲࡤࠡࡰࡲࡸࠥࡨࡥࠡࡲࡵࡳࡨ࡫ࡳࡴࡧࡧࠤ࡫ࡵࡲࠡࡶ࡫ࡩࠥࡺࡥࡴࡶࠣࡧࡦࡹࡥ࠻ࠢࠥₒ") + str(path) + bstack11l111_opy_ (u"ࠤࠣࡉࡷࡸ࡯ࡳࠢ࠽ࠦₓ") + str(bstack1l111l11l1l_opy_))
def bstack1lllll11l11l_opy_(driver):
    caps = driver.capabilities
    if caps.get(bstack11l111_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱࡓࡧ࡭ࡦࠤₔ")) and str(caps.get(bstack11l111_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲࡔࡡ࡮ࡧࠥₕ"))).lower() == bstack11l111_opy_ (u"ࠧࡧ࡮ࡥࡴࡲ࡭ࡩࠨₖ"):
        bstack1l111l1l111_opy_ = caps.get(bstack11l111_opy_ (u"ࠨࡡࡱࡲ࡬ࡹࡲࡀࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠣₗ")) or caps.get(bstack11l111_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠤₘ"))
        if bstack1l111l1l111_opy_ and int(str(bstack1l111l1l111_opy_)) < bstack11l1l1l11l1_opy_:
            return False
    return True
def bstack1lll1l1lll_opy_(config):
  if bstack11l111_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨₙ") in config:
        return config[bstack11l111_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩₚ")]
  for platform in config.get(bstack11l111_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ₛ"), []):
      if bstack11l111_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫₜ") in platform:
          return platform[bstack11l111_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ₝")]
  return None
def bstack111ll11ll1_opy_(bstack111l1ll1l_opy_):
  try:
    browser_name = bstack111l1ll1l_opy_[bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸ࡟࡯ࡣࡰࡩࠬ₞")]
    browser_version = bstack111l1ll1l_opy_[bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡸࡨࡶࡸ࡯࡯࡯ࠩ₟")]
    chrome_options = bstack111l1ll1l_opy_[bstack11l111_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࡠࡱࡳࡸ࡮ࡵ࡮ࡴࠩ₠")]
    try:
        bstack1lllll111lll_opy_ = int(browser_version.split(bstack11l111_opy_ (u"ࠩ࠱ࠫ₡"))[0])
    except ValueError as e:
        logger.error(bstack11l111_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡺ࡬࡮ࡲࡥࠡࡥࡲࡲࡻ࡫ࡲࡵ࡫ࡱ࡫ࠥࡨࡲࡰࡹࡶࡩࡷࠦࡶࡦࡴࡶ࡭ࡴࡴࠢ₢") + str(e))
        return False
    if not (browser_name and browser_name.lower() == bstack11l111_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࠫ₣")):
        logger.warning(bstack11l111_opy_ (u"ࠧࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡺ࡭ࡱࡲࠠࡳࡷࡱࠤࡴࡴ࡬ࡺࠢࡲࡲࠥࡉࡨࡳࡱࡰࡩࠥࡨࡲࡰࡹࡶࡩࡷࡹ࠮ࠣ₤"))
        return False
    if bstack1lllll111lll_opy_ < bstack1llll1lllll1_opy_.bstack1l111llll11_opy_:
        logger.warning(bstack1lll1lll1ll_opy_ (u"࠭ࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡶࡪࡷࡵࡪࡴࡨࡷࠥࡉࡨࡳࡱࡰࡩࠥࡼࡥࡳࡵ࡬ࡳࡳࠦࡻࡄࡑࡑࡗ࡙ࡇࡎࡕࡕ࠱ࡑࡎࡔࡉࡎࡗࡐࡣࡓࡕࡎࡠࡄࡖࡘࡆࡉࡋࡠࡋࡑࡊࡗࡇ࡟ࡂ࠳࠴࡝ࡤ࡙ࡕࡑࡒࡒࡖ࡙ࡋࡄࡠࡅࡋࡖࡔࡓࡅࡠࡘࡈࡖࡘࡏࡏࡏࡿࠣࡳࡷࠦࡨࡪࡩ࡫ࡩࡷ࠴ࠧ₥"))
        return False
    if chrome_options and any(bstack11l111_opy_ (u"ࠧ࠮࠯࡫ࡩࡦࡪ࡬ࡦࡵࡶࠫ₦") in value for value in chrome_options.values() if isinstance(value, str)):
        logger.warning(bstack11l111_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡽࡩ࡭࡮ࠣࡲࡴࡺࠠࡳࡷࡱࠤࡴࡴࠠ࡭ࡧࡪࡥࡨࡿࠠࡩࡧࡤࡨࡱ࡫ࡳࡴࠢࡰࡳࡩ࡫࠮ࠡࡕࡺ࡭ࡹࡩࡨࠡࡶࡲࠤࡳ࡫ࡷࠡࡪࡨࡥࡩࡲࡥࡴࡵࠣࡱࡴࡪࡥࠡࡱࡵࠤࡦࡼ࡯ࡪࡦࠣࡹࡸ࡯࡮ࡨࠢ࡫ࡩࡦࡪ࡬ࡦࡵࡶࠤࡲࡵࡤࡦ࠰ࠥ₧"))
        return False
    return True
  except Exception as e:
    logger.error(bstack11l111_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡨ࡮ࡥࡤ࡭࡬ࡲ࡬ࠦࡰ࡭ࡣࡷࡪࡴࡸ࡭ࠡࡵࡸࡴࡵࡵࡲࡵࠢࡩࡳࡷࠦ࡬ࡰࡥࡤࡰࠥࡉࡨࡳࡱࡰࡩ࠿ࠦࠢ₨") + str(e))
    return False
def bstack11l1l1l1l_opy_(bstack11llll1111_opy_, config):
    try:
      bstack1l1111lll1l_opy_ = bstack11l111_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ₩") in config and config[bstack11l111_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ₪")] == True
      bstack1lllll111111_opy_ = bstack11l111_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩ₫") in config and str(config[bstack11l111_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪ€")]).lower() != bstack11l111_opy_ (u"ࠧࡧࡣ࡯ࡷࡪ࠭₭")
      if not (bstack1l1111lll1l_opy_ and (not bstack1ll1l1l1ll_opy_(config) or bstack1lllll111111_opy_)):
        return bstack11llll1111_opy_
      bstack1lllll11111l_opy_ = bstack1l1l1ll111_opy_.bstack1lllll11ll1l_opy_
      if bstack1lllll11111l_opy_ is None:
        logger.debug(bstack11l111_opy_ (u"ࠣࡉࡲࡳ࡬ࡲࡥࠡࡥ࡫ࡶࡴࡳࡥࠡࡱࡳࡸ࡮ࡵ࡮ࡴࠢࡤࡶࡪࠦࡎࡰࡰࡨࠦ₮"))
        return bstack11llll1111_opy_
      bstack1llll1l1llll_opy_ = int(str(bstack1111ll11ll1_opy_()).split(bstack11l111_opy_ (u"ࠩ࠱ࠫ₯"))[0])
      logger.debug(bstack11l111_opy_ (u"ࠥࡗࡪࡲࡥ࡯࡫ࡸࡱࠥࡼࡥࡳࡵ࡬ࡳࡳࠦࡤࡦࡶࡨࡧࡹ࡫ࡤ࠻ࠢࠥ₰") + str(bstack1llll1l1llll_opy_) + bstack11l111_opy_ (u"ࠦࠧ₱"))
      if bstack1llll1l1llll_opy_ == 3 and isinstance(bstack11llll1111_opy_, dict) and bstack11l111_opy_ (u"ࠬࡪࡥࡴ࡫ࡵࡩࡩࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠬ₲") in bstack11llll1111_opy_ and bstack1lllll11111l_opy_ is not None:
        if bstack11l111_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫ₳") not in bstack11llll1111_opy_[bstack11l111_opy_ (u"ࠧࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠧ₴")]:
          bstack11llll1111_opy_[bstack11l111_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨ₵")][bstack11l111_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ₶")] = {}
        if bstack11l111_opy_ (u"ࠪࡥࡷ࡭ࡳࠨ₷") in bstack1lllll11111l_opy_:
          if bstack11l111_opy_ (u"ࠫࡦࡸࡧࡴࠩ₸") not in bstack11llll1111_opy_[bstack11l111_opy_ (u"ࠬࡪࡥࡴ࡫ࡵࡩࡩࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠬ₹")][bstack11l111_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫ₺")]:
            bstack11llll1111_opy_[bstack11l111_opy_ (u"ࠧࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠧ₻")][bstack11l111_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭₼")][bstack11l111_opy_ (u"ࠩࡤࡶ࡬ࡹࠧ₽")] = []
          for arg in bstack1lllll11111l_opy_[bstack11l111_opy_ (u"ࠪࡥࡷ࡭ࡳࠨ₾")]:
            if arg not in bstack11llll1111_opy_[bstack11l111_opy_ (u"ࠫࡩ࡫ࡳࡪࡴࡨࡨࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠫ₿")][bstack11l111_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ⃀")][bstack11l111_opy_ (u"࠭ࡡࡳࡩࡶࠫ⃁")]:
              bstack11llll1111_opy_[bstack11l111_opy_ (u"ࠧࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠧ⃂")][bstack11l111_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭⃃")][bstack11l111_opy_ (u"ࠩࡤࡶ࡬ࡹࠧ⃄")].append(arg)
        if bstack11l111_opy_ (u"ࠪࡩࡽࡺࡥ࡯ࡵ࡬ࡳࡳࡹࠧ⃅") in bstack1lllll11111l_opy_:
          if bstack11l111_opy_ (u"ࠫࡪࡾࡴࡦࡰࡶ࡭ࡴࡴࡳࠨ⃆") not in bstack11llll1111_opy_[bstack11l111_opy_ (u"ࠬࡪࡥࡴ࡫ࡵࡩࡩࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠬ⃇")][bstack11l111_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫ⃈")]:
            bstack11llll1111_opy_[bstack11l111_opy_ (u"ࠧࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠧ⃉")][bstack11l111_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭⃊")][bstack11l111_opy_ (u"ࠩࡨࡼࡹ࡫࡮ࡴ࡫ࡲࡲࡸ࠭⃋")] = []
          for ext in bstack1lllll11111l_opy_[bstack11l111_opy_ (u"ࠪࡩࡽࡺࡥ࡯ࡵ࡬ࡳࡳࡹࠧ⃌")]:
            if ext not in bstack11llll1111_opy_[bstack11l111_opy_ (u"ࠫࡩ࡫ࡳࡪࡴࡨࡨࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠫ⃍")][bstack11l111_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ⃎")][bstack11l111_opy_ (u"࠭ࡥࡹࡶࡨࡲࡸ࡯࡯࡯ࡵࠪ⃏")]:
              bstack11llll1111_opy_[bstack11l111_opy_ (u"ࠧࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠧ⃐")][bstack11l111_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭⃑")][bstack11l111_opy_ (u"ࠩࡨࡼࡹ࡫࡮ࡴ࡫ࡲࡲࡸ⃒࠭")].append(ext)
        if bstack11l111_opy_ (u"ࠪࡴࡷ࡫ࡦࡴ⃓ࠩ") in bstack1lllll11111l_opy_:
          if bstack11l111_opy_ (u"ࠫࡵࡸࡥࡧࡵࠪ⃔") not in bstack11llll1111_opy_[bstack11l111_opy_ (u"ࠬࡪࡥࡴ࡫ࡵࡩࡩࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠬ⃕")][bstack11l111_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫ⃖")]:
            bstack11llll1111_opy_[bstack11l111_opy_ (u"ࠧࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠧ⃗")][bstack11l111_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ⃘࠭")][bstack11l111_opy_ (u"ࠩࡳࡶࡪ࡬ࡳࠨ⃙")] = {}
          bstack1111lll1l1l_opy_(bstack11llll1111_opy_[bstack11l111_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵ⃚ࠪ")][bstack11l111_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩ⃛")][bstack11l111_opy_ (u"ࠬࡶࡲࡦࡨࡶࠫ⃜")],
                    bstack1lllll11111l_opy_[bstack11l111_opy_ (u"࠭ࡰࡳࡧࡩࡷࠬ⃝")])
        os.environ[bstack11l111_opy_ (u"ࠧࡊࡕࡢࡒࡔࡔ࡟ࡃࡕࡗࡅࡈࡑ࡟ࡊࡐࡉࡖࡆࡥࡁ࠲࠳࡜ࡣࡘࡋࡓࡔࡋࡒࡒࠬ⃞")] = bstack11l111_opy_ (u"ࠨࡶࡵࡹࡪ࠭⃟")
        return bstack11llll1111_opy_
      else:
        chrome_options = None
        if isinstance(bstack11llll1111_opy_, ChromeOptions):
          chrome_options = bstack11llll1111_opy_
        elif isinstance(bstack11llll1111_opy_, dict):
          for value in bstack11llll1111_opy_.values():
            if isinstance(value, ChromeOptions):
              chrome_options = value
              break
        if chrome_options is None:
          chrome_options = ChromeOptions()
          if isinstance(bstack11llll1111_opy_, dict):
            bstack11llll1111_opy_[bstack11l111_opy_ (u"ࠩࡲࡴࡹ࡯࡯࡯ࡵࠪ⃠")] = chrome_options
          else:
            bstack11llll1111_opy_ = chrome_options
        if bstack1lllll11111l_opy_ is not None:
          if bstack11l111_opy_ (u"ࠪࡥࡷ࡭ࡳࠨ⃡") in bstack1lllll11111l_opy_:
                bstack1llll1llll1l_opy_ = chrome_options.arguments or []
                new_args = bstack1lllll11111l_opy_[bstack11l111_opy_ (u"ࠫࡦࡸࡧࡴࠩ⃢")]
                for arg in new_args:
                    if arg not in bstack1llll1llll1l_opy_:
                        chrome_options.add_argument(arg)
          if bstack11l111_opy_ (u"ࠬ࡫ࡸࡵࡧࡱࡷ࡮ࡵ࡮ࡴࠩ⃣") in bstack1lllll11111l_opy_:
                existing_extensions = chrome_options.experimental_options.get(bstack11l111_opy_ (u"࠭ࡥࡹࡶࡨࡲࡸ࡯࡯࡯ࡵࠪ⃤"), [])
                bstack1lllll111l1l_opy_ = bstack1lllll11111l_opy_[bstack11l111_opy_ (u"ࠧࡦࡺࡷࡩࡳࡹࡩࡰࡰࡶ⃥ࠫ")]
                for extension in bstack1lllll111l1l_opy_:
                    if extension not in existing_extensions:
                        chrome_options.add_encoded_extension(extension)
          if bstack11l111_opy_ (u"ࠨࡲࡵࡩ࡫ࡹ⃦ࠧ") in bstack1lllll11111l_opy_:
                bstack1lllll1111ll_opy_ = chrome_options.experimental_options.get(bstack11l111_opy_ (u"ࠩࡳࡶࡪ࡬ࡳࠨ⃧"), {})
                bstack1llll1llll11_opy_ = bstack1lllll11111l_opy_[bstack11l111_opy_ (u"ࠪࡴࡷ࡫ࡦࡴ⃨ࠩ")]
                bstack1111lll1l1l_opy_(bstack1lllll1111ll_opy_, bstack1llll1llll11_opy_)
                chrome_options.add_experimental_option(bstack11l111_opy_ (u"ࠫࡵࡸࡥࡧࡵࠪ⃩"), bstack1lllll1111ll_opy_)
        os.environ[bstack11l111_opy_ (u"ࠬࡏࡓࡠࡐࡒࡒࡤࡈࡓࡕࡃࡆࡏࡤࡏࡎࡇࡔࡄࡣࡆ࠷࠱࡚ࡡࡖࡉࡘ࡙ࡉࡐࡐ⃪ࠪ")] = bstack11l111_opy_ (u"࠭ࡴࡳࡷࡨ⃫ࠫ")
        return bstack11llll1111_opy_
    except Exception as e:
      logger.error(bstack11l111_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡷࡩ࡫࡯ࡩࠥࡧࡤࡥ࡫ࡱ࡫ࠥࡴ࡯࡯࠯ࡅࡗࠥ࡯࡮ࡧࡴࡤࠤࡦ࠷࠱ࡺࠢࡦ࡬ࡷࡵ࡭ࡦࠢࡲࡴࡹ࡯࡯࡯ࡵ࠽ࠤ⃬ࠧ") + str(e))
      return bstack11llll1111_opy_