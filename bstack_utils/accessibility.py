# coding: UTF-8
import sys
bstack1l11l_opy_ = sys.version_info [0] == 2
bstack1111_opy_ = 2048
bstack1lll1_opy_ = 7
def bstack1lllll1l_opy_ (bstack1ll1l11_opy_):
    global bstack11l1ll_opy_
    bstack111lll_opy_ = ord (bstack1ll1l11_opy_ [-1])
    bstack1l111l1_opy_ = bstack1ll1l11_opy_ [:-1]
    bstack1111l_opy_ = bstack111lll_opy_ % len (bstack1l111l1_opy_)
    bstack1111ll_opy_ = bstack1l111l1_opy_ [:bstack1111l_opy_] + bstack1l111l1_opy_ [bstack1111l_opy_:]
    if bstack1l11l_opy_:
        bstack1l1l1_opy_ = unicode () .join ([unichr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    else:
        bstack1l1l1_opy_ = str () .join ([chr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    return eval (bstack1l1l1_opy_)
import os
import json
import requests
import logging
import threading
import bstack_utils.constants as bstack1lllll11111l_opy_
from urllib.parse import urlparse
from bstack_utils.constants import bstack11l11ll111l_opy_ as bstack1lllll111111_opy_, EVENTS
from bstack_utils.bstack11l11l11ll_opy_ import bstack11l11l11ll_opy_
from bstack_utils.helper import bstack1l1111ll_opy_, bstack1l111ll1_opy_, bstack111l1lll11_opy_, bstack1111ll11111_opy_, \
  bstack111l111ll11_opy_, bstack1l1l11llll_opy_, get_host_info, bstack1111lll1l1l_opy_, bstack11l1l111l1_opy_, error_handler, bstack1111l1llll1_opy_, bstack111l11ll111_opy_, bstack1l11l1l1_opy_
from browserstack_sdk._version import __version__
from bstack_utils.bstack11llll111l_opy_ import get_logger
from bstack_utils.bstack111l1111l_opy_ import bstack1llllllll1l_opy_
from selenium.webdriver.chrome.options import Options as ChromeOptions
from browserstack_sdk.sdk_cli.cli import cli
from bstack_utils.constants import *
logger = get_logger(__name__)
bstack111l1111l_opy_ = bstack1llllllll1l_opy_()
@error_handler(class_method=False)
def _1lllll111l11_opy_(driver, bstack1llllll1l_opy_):
  response = {}
  try:
    caps = driver.capabilities
    response = {
        bstack1lllll1l_opy_ (u"ࠬࡵࡳࡠࡰࡤࡱࡪ࠭ῧ"): caps.get(bstack1lllll1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡏࡣࡰࡩࠬῨ"), None),
        bstack1lllll1l_opy_ (u"ࠧࡰࡵࡢࡺࡪࡸࡳࡪࡱࡱࠫῩ"): bstack1llllll1l_opy_.get(bstack1lllll1l_opy_ (u"ࠨࡱࡶ࡚ࡪࡸࡳࡪࡱࡱࠫῪ"), None),
        bstack1lllll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡲࡦࡳࡥࠨΎ"): caps.get(bstack1lllll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨῬ"), None),
        bstack1lllll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭῭"): caps.get(bstack1lllll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭΅"), None)
    }
  except Exception as error:
    logger.debug(bstack1lllll1l_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥ࡬ࡥࡵࡥ࡫࡭ࡳ࡭ࠠࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࠢࡧࡩࡹࡧࡩ࡭ࡵࠣࡻ࡮ࡺࡨࠡࡧࡵࡶࡴࡸࠠ࠻ࠢࠪ`") + str(error))
  return response
def on():
    if os.environ.get(bstack1lllll1l_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠬ῰"), None) is None or os.environ[bstack1lllll1l_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭῱")] == bstack1lllll1l_opy_ (u"ࠤࡱࡹࡱࡲࠢῲ"):
        return False
    return True
def bstack111ll111ll_opy_(config):
  return config.get(bstack1lllll1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪῳ"), False) or any([p.get(bstack1lllll1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫῴ"), False) == True for p in config.get(bstack1lllll1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ῵"), [])])
def bstack1l1lll1l1l_opy_(config, bstack11ll1l1ll_opy_):
  try:
    bstack1llll1lllll1_opy_ = config.get(bstack1lllll1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ῶ"), False)
    if int(bstack11ll1l1ll_opy_) < len(config.get(bstack1lllll1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪῷ"), [])) and config[bstack1lllll1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫῸ")][bstack11ll1l1ll_opy_]:
      bstack1llll1l1l111_opy_ = config[bstack1lllll1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬΌ")][bstack11ll1l1ll_opy_].get(bstack1lllll1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪῺ"), None)
    else:
      bstack1llll1l1l111_opy_ = config.get(bstack1lllll1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫΏ"), None)
    if bstack1llll1l1l111_opy_ != None:
      bstack1llll1lllll1_opy_ = bstack1llll1l1l111_opy_
    bstack1llll1llllll_opy_ = os.getenv(bstack1lllll1l_opy_ (u"ࠬࡈࡓࡠࡃ࠴࠵࡞ࡥࡊࡘࡖࠪῼ")) is not None and len(os.getenv(bstack1lllll1l_opy_ (u"࠭ࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗࠫ´"))) > 0 and os.getenv(bstack1lllll1l_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠬ῾")) != bstack1lllll1l_opy_ (u"ࠨࡰࡸࡰࡱ࠭῿")
    return bstack1llll1lllll1_opy_ and bstack1llll1llllll_opy_
  except Exception as error:
    logger.debug(bstack1lllll1l_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡸࡨࡶ࡮࡬ࡹࡪࡰࡪࠤࡹ࡮ࡥࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡺ࡭ࡹ࡮ࠠࡦࡴࡵࡳࡷࠦ࠺ࠡࠩ ") + str(error))
  return False
def bstack1ll1l11ll_opy_(test_tags):
  bstack1l1111ll1ll_opy_ = os.getenv(bstack1lllll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚࡟ࡂࡅࡆࡉࡘ࡙ࡉࡃࡋࡏࡍ࡙࡟࡟ࡄࡑࡑࡊࡎࡍࡕࡓࡃࡗࡍࡔࡔ࡟࡚ࡏࡏࠫ "))
  if bstack1l1111ll1ll_opy_ is None:
    return True
  bstack1l1111ll1ll_opy_ = json.loads(bstack1l1111ll1ll_opy_)
  try:
    include_tags = bstack1l1111ll1ll_opy_[bstack1lllll1l_opy_ (u"ࠫ࡮ࡴࡣ࡭ࡷࡧࡩ࡙ࡧࡧࡴࡋࡱࡘࡪࡹࡴࡪࡰࡪࡗࡨࡵࡰࡦࠩ ")] if bstack1lllll1l_opy_ (u"ࠬ࡯࡮ࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪ ") in bstack1l1111ll1ll_opy_ and isinstance(bstack1l1111ll1ll_opy_[bstack1lllll1l_opy_ (u"࠭ࡩ࡯ࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫ ")], list) else []
    exclude_tags = bstack1l1111ll1ll_opy_[bstack1lllll1l_opy_ (u"ࠧࡦࡺࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩࠬ ")] if bstack1lllll1l_opy_ (u"ࠨࡧࡻࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ࠭ ") in bstack1l1111ll1ll_opy_ and isinstance(bstack1l1111ll1ll_opy_[bstack1lllll1l_opy_ (u"ࠩࡨࡼࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧ ")], list) else []
    excluded = any(tag in exclude_tags for tag in test_tags)
    included = len(include_tags) == 0 or any(tag in include_tags for tag in test_tags)
    return not excluded and included
  except Exception as error:
    logger.debug(bstack1lllll1l_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡺ࡬࡮ࡲࡥࠡࡸࡤࡰ࡮ࡪࡡࡵ࡫ࡱ࡫ࠥࡺࡥࡴࡶࠣࡧࡦࡹࡥࠡࡨࡲࡶࠥࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡨࡥࡧࡱࡵࡩࠥࡹࡣࡢࡰࡱ࡭ࡳ࡭࠮ࠡࡇࡵࡶࡴࡸࠠ࠻ࠢࠥ ") + str(error))
  return False
def bstack1llll1l1l11l_opy_(config, frameworkName, bstack1llll1l1l1l1_opy_, bstack1llll1lll1l1_opy_):
  bstack1llll1llll1l_opy_ = bstack1111ll11111_opy_(config)
  bstack1llll1ll11l1_opy_ = bstack111l111ll11_opy_(config)
  if bstack1llll1llll1l_opy_ is None or bstack1llll1ll11l1_opy_ is None:
    logger.error(bstack1lllll1l_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡸࡪ࡬ࡰࡪࠦࡣࡳࡧࡤࡸ࡮ࡴࡧࠡࡶࡨࡷࡹࠦࡲࡶࡰࠣࡪࡴࡸࠠࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰ࠽ࠤࡒ࡯ࡳࡴ࡫ࡱ࡫ࠥࡧࡵࡵࡪࡨࡲࡹ࡯ࡣࡢࡶ࡬ࡳࡳࠦࡴࡰ࡭ࡨࡲࠬ "))
    return [None, None]
  try:
    settings = json.loads(os.getenv(bstack1lllll1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡡࡄࡇࡈࡋࡓࡔࡋࡅࡍࡑࡏࡔ࡚ࡡࡆࡓࡓࡌࡉࡈࡗࡕࡅ࡙ࡏࡏࡏࡡ࡜ࡑࡑ࠭ "), bstack1lllll1l_opy_ (u"࠭ࡻࡾࠩ​")))
    data = {
        bstack1lllll1l_opy_ (u"ࠧࡱࡴࡲ࡮ࡪࡩࡴࡏࡣࡰࡩࠬ‌"): config[bstack1lllll1l_opy_ (u"ࠨࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪ࠭‍")],
        bstack1lllll1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ‎"): config.get(bstack1lllll1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭‏"), os.path.basename(os.getcwd())),
        bstack1lllll1l_opy_ (u"ࠫࡸࡺࡡࡳࡶࡗ࡭ࡲ࡫ࠧ‐"): bstack1l1111ll_opy_(),
        bstack1lllll1l_opy_ (u"ࠬࡪࡥࡴࡥࡵ࡭ࡵࡺࡩࡰࡰࠪ‑"): config.get(bstack1lllll1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡉ࡫ࡳࡤࡴ࡬ࡴࡹ࡯࡯࡯ࠩ‒"), bstack1lllll1l_opy_ (u"ࠧࠨ–")),
        bstack1lllll1l_opy_ (u"ࠨࡵࡲࡹࡷࡩࡥࠨ—"): {
            bstack1lllll1l_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡓࡧ࡭ࡦࠩ―"): frameworkName,
            bstack1lllll1l_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࡜ࡥࡳࡵ࡬ࡳࡳ࠭‖"): bstack1llll1l1l1l1_opy_,
            bstack1lllll1l_opy_ (u"ࠫࡸࡪ࡫ࡗࡧࡵࡷ࡮ࡵ࡮ࠨ‗"): __version__,
            bstack1lllll1l_opy_ (u"ࠬࡲࡡ࡯ࡩࡸࡥ࡬࡫ࠧ‘"): bstack1lllll1l_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭’"),
            bstack1lllll1l_opy_ (u"ࠧࡵࡧࡶࡸࡋࡸࡡ࡮ࡧࡺࡳࡷࡱࠧ‚"): bstack1lllll1l_opy_ (u"ࠨࡵࡨࡰࡪࡴࡩࡶ࡯ࠪ‛"),
            bstack1lllll1l_opy_ (u"ࠩࡷࡩࡸࡺࡆࡳࡣࡰࡩࡼࡵࡲ࡬ࡘࡨࡶࡸ࡯࡯࡯ࠩ“"): bstack1llll1lll1l1_opy_
        },
        bstack1lllll1l_opy_ (u"ࠪࡷࡪࡺࡴࡪࡰࡪࡷࠬ”"): settings,
        bstack1lllll1l_opy_ (u"ࠫࡻ࡫ࡲࡴ࡫ࡲࡲࡈࡵ࡮ࡵࡴࡲࡰࠬ„"): bstack1111lll1l1l_opy_(),
        bstack1lllll1l_opy_ (u"ࠬࡩࡩࡊࡰࡩࡳࠬ‟"): bstack1l1l11llll_opy_(),
        bstack1lllll1l_opy_ (u"࠭ࡨࡰࡵࡷࡍࡳ࡬࡯ࠨ†"): get_host_info(),
        bstack1lllll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠩ‡"): bstack111l1lll11_opy_(config)
    }
    headers = {
        bstack1lllll1l_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡗࡽࡵ࡫ࠧ•"): bstack1lllll1l_opy_ (u"ࠩࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯࡫ࡵࡲࡲࠬ‣"),
    }
    config = {
        bstack1lllll1l_opy_ (u"ࠪࡥࡺࡺࡨࠨ․"): (bstack1llll1llll1l_opy_, bstack1llll1ll11l1_opy_),
        bstack1lllll1l_opy_ (u"ࠫ࡭࡫ࡡࡥࡧࡵࡷࠬ‥"): headers
    }
    response = bstack11l1l111l1_opy_(bstack1lllll1l_opy_ (u"ࠬࡖࡏࡔࡖࠪ…"), bstack1lllll111111_opy_ + bstack1lllll1l_opy_ (u"࠭࠯ࡷ࠴࠲ࡸࡪࡹࡴࡠࡴࡸࡲࡸ࠭‧"), data, config)
    bstack1llll1l1ll1l_opy_ = response.json()
    if bstack1llll1l1ll1l_opy_[bstack1lllll1l_opy_ (u"ࠧࡴࡷࡦࡧࡪࡹࡳࠨ ")]:
      parsed = json.loads(os.getenv(bstack1lllll1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡤࡇࡃࡄࡇࡖࡗࡎࡈࡉࡍࡋࡗ࡝ࡤࡉࡏࡏࡈࡌࡋ࡚ࡘࡁࡕࡋࡒࡒࡤ࡟ࡍࡍࠩ "), bstack1lllll1l_opy_ (u"ࠩࡾࢁࠬ‪")))
      parsed[bstack1lllll1l_opy_ (u"ࠪࡷࡨࡧ࡮࡯ࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫ‫")] = bstack1llll1l1ll1l_opy_[bstack1lllll1l_opy_ (u"ࠫࡩࡧࡴࡢࠩ‬")][bstack1lllll1l_opy_ (u"ࠬࡹࡣࡢࡰࡱࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭‭")]
      os.environ[bstack1lllll1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡢࡅࡈࡉࡅࡔࡕࡌࡆࡎࡒࡉࡕ࡛ࡢࡇࡔࡔࡆࡊࡉࡘࡖࡆ࡚ࡉࡐࡐࡢ࡝ࡒࡒࠧ‮")] = json.dumps(parsed)
      bstack11l11l11ll_opy_.bstack11lll1lll_opy_(bstack1llll1l1ll1l_opy_[bstack1lllll1l_opy_ (u"ࠧࡥࡣࡷࡥࠬ ")][bstack1lllll1l_opy_ (u"ࠨࡵࡦࡶ࡮ࡶࡴࡴࠩ‰")])
      bstack11l11l11ll_opy_.bstack1lllll11l1l1_opy_(bstack1llll1l1ll1l_opy_[bstack1lllll1l_opy_ (u"ࠩࡧࡥࡹࡧࠧ‱")][bstack1lllll1l_opy_ (u"ࠪࡧࡴࡳ࡭ࡢࡰࡧࡷࠬ′")])
      bstack11l11l11ll_opy_.store()
      return bstack1llll1l1ll1l_opy_[bstack1lllll1l_opy_ (u"ࠫࡩࡧࡴࡢࠩ″")][bstack1lllll1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽ࡙ࡵ࡫ࡦࡰࠪ‴")], bstack1llll1l1ll1l_opy_[bstack1lllll1l_opy_ (u"࠭ࡤࡢࡶࡤࠫ‵")][bstack1lllll1l_opy_ (u"ࠧࡪࡦࠪ‶")]
    else:
      logger.error(bstack1lllll1l_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡼ࡮ࡩ࡭ࡧࠣࡶࡺࡴ࡮ࡪࡰࡪࠤࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࠺ࠡࠩ‷") + bstack1llll1l1ll1l_opy_[bstack1lllll1l_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ‸")])
      if bstack1llll1l1ll1l_opy_[bstack1lllll1l_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ‹")] == bstack1lllll1l_opy_ (u"ࠫࡎࡴࡶࡢ࡮࡬ࡨࠥࡩ࡯࡯ࡨ࡬࡫ࡺࡸࡡࡵ࡫ࡲࡲࠥࡶࡡࡴࡵࡨࡨ࠳࠭›"):
        for bstack1llll1l1lll1_opy_ in bstack1llll1l1ll1l_opy_[bstack1lllll1l_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࡷࠬ※")]:
          logger.error(bstack1llll1l1lll1_opy_[bstack1lllll1l_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ‼")])
      return None, None
  except Exception as error:
    logger.error(bstack1lllll1l_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡻ࡭࡯࡬ࡦࠢࡦࡶࡪࡧࡴࡪࡰࡪࠤࡹ࡫ࡳࡵࠢࡵࡹࡳࠦࡦࡰࡴࠣࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡀࠠࠣ‽") +  str(error))
    return None, None
def bstack1llll1ll11ll_opy_():
  if os.getenv(bstack1lllll1l_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭‾")) is None:
    return {
        bstack1lllll1l_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩ‿"): bstack1lllll1l_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩ⁀"),
        bstack1lllll1l_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ⁁"): bstack1lllll1l_opy_ (u"ࠬࡈࡵࡪ࡮ࡧࠤࡨࡸࡥࡢࡶ࡬ࡳࡳࠦࡨࡢࡦࠣࡪࡦ࡯࡬ࡦࡦ࠱ࠫ⁂")
    }
  data = {bstack1lllll1l_opy_ (u"࠭ࡥ࡯ࡦࡗ࡭ࡲ࡫ࠧ⁃"): bstack1l1111ll_opy_()}
  headers = {
      bstack1lllll1l_opy_ (u"ࠧࡂࡷࡷ࡬ࡴࡸࡩࡻࡣࡷ࡭ࡴࡴࠧ⁄"): bstack1lllll1l_opy_ (u"ࠨࡄࡨࡥࡷ࡫ࡲࠡࠩ⁅") + os.getenv(bstack1lllll1l_opy_ (u"ࠤࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠢ⁆")),
      bstack1lllll1l_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱࡙ࡿࡰࡦࠩ⁇"): bstack1lllll1l_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧ⁈")
  }
  response = bstack11l1l111l1_opy_(bstack1lllll1l_opy_ (u"ࠬࡖࡕࡕࠩ⁉"), bstack1lllll111111_opy_ + bstack1lllll1l_opy_ (u"࠭࠯ࡵࡧࡶࡸࡤࡸࡵ࡯ࡵ࠲ࡷࡹࡵࡰࠨ⁊"), data, { bstack1lllll1l_opy_ (u"ࠧࡩࡧࡤࡨࡪࡸࡳࠨ⁋"): headers })
  try:
    if response.status_code == 200:
      logger.info(bstack1lllll1l_opy_ (u"ࠣࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤ࡙࡫ࡳࡵࠢࡕࡹࡳࠦ࡭ࡢࡴ࡮ࡩࡩࠦࡡࡴࠢࡦࡳࡲࡶ࡬ࡦࡶࡨࡨࠥࡧࡴࠡࠤ⁌") + bstack1l111ll1_opy_().isoformat() + bstack1lllll1l_opy_ (u"ࠩ࡝ࠫ⁍"))
      return {bstack1lllll1l_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪ⁎"): bstack1lllll1l_opy_ (u"ࠫࡸࡻࡣࡤࡧࡶࡷࠬ⁏"), bstack1lllll1l_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭⁐"): bstack1lllll1l_opy_ (u"࠭ࠧ⁑")}
    else:
      response.raise_for_status()
  except requests.RequestException as error:
    logger.error(bstack1lllll1l_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡻ࡭࡯࡬ࡦࠢࡰࡥࡷࡱࡩ࡯ࡩࠣࡧࡴࡳࡰ࡭ࡧࡷ࡭ࡴࡴࠠࡰࡨࠣࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡔࡦࡵࡷࠤࡗࡻ࡮࠻ࠢࠥ⁒") + str(error))
    return {
        bstack1lllll1l_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨ⁓"): bstack1lllll1l_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨ⁔"),
        bstack1lllll1l_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ⁕"): str(error)
    }
def bstack1llll1ll1ll1_opy_(bstack1llll1ll1111_opy_):
    return re.match(bstack1lllll1l_opy_ (u"ࡶࠬࡤ࡜ࡥ࠭ࠫࡠ࠳ࡢࡤࠬࠫࡂࠨࠬ⁖"), bstack1llll1ll1111_opy_.strip()) is not None
def bstack1l1l1l1ll_opy_(caps, options, desired_capabilities={}, config=None):
    try:
        if options:
          bstack1llll1llll11_opy_ = options.to_capabilities()
        elif desired_capabilities:
          bstack1llll1llll11_opy_ = desired_capabilities
        else:
          bstack1llll1llll11_opy_ = {}
        bstack1l1111l11ll_opy_ = (bstack1llll1llll11_opy_.get(bstack1lllll1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡎࡢ࡯ࡨࠫ⁗"), bstack1lllll1l_opy_ (u"࠭ࠧ⁘")).lower() or caps.get(bstack1lllll1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡐࡤࡱࡪ࠭⁙"), bstack1lllll1l_opy_ (u"ࠨࠩ⁚")).lower())
        if bstack1l1111l11ll_opy_ == bstack1lllll1l_opy_ (u"ࠩ࡬ࡳࡸ࠭⁛"):
            return True
        if bstack1l1111l11ll_opy_ == bstack1lllll1l_opy_ (u"ࠪࡥࡳࡪࡲࡰ࡫ࡧࠫ⁜"):
            bstack1l111l1l1l1_opy_ = str(float(caps.get(bstack1lllll1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲ࡜ࡥࡳࡵ࡬ࡳࡳ࠭⁝")) or bstack1llll1llll11_opy_.get(bstack1lllll1l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭⁞"), {}).get(bstack1lllll1l_opy_ (u"࠭࡯ࡴࡘࡨࡶࡸ࡯࡯࡯ࠩ "),bstack1lllll1l_opy_ (u"ࠧࠨ⁠"))))
            if bstack1l1111l11ll_opy_ == bstack1lllll1l_opy_ (u"ࠨࡣࡱࡨࡷࡵࡩࡥࠩ⁡") and int(bstack1l111l1l1l1_opy_.split(bstack1lllll1l_opy_ (u"ࠩ࠱ࠫ⁢"))[0]) < float(bstack11l11lllll1_opy_):
                logger.warning(str(bstack11l11lll11l_opy_))
                return False
            return True
        bstack1l1111l11l1_opy_ = caps.get(bstack1lllll1l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫ⁣"), {}).get(bstack1lllll1l_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࡒࡦࡳࡥࠨ⁤"), caps.get(bstack1lllll1l_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࠬ⁥"), bstack1lllll1l_opy_ (u"࠭ࠧ⁦")))
        if bstack1l1111l11l1_opy_:
            logger.warning(bstack1lllll1l_opy_ (u"ࠢࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡼ࡯࡬࡭ࠢࡵࡹࡳࠦ࡯࡯࡮ࡼࠤࡴࡴࠠࡅࡧࡶ࡯ࡹࡵࡰࠡࡤࡵࡳࡼࡹࡥࡳࡵ࠱ࠦ⁧"))
            return False
        browser = caps.get(bstack1lllll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭⁨"), bstack1lllll1l_opy_ (u"ࠩࠪ⁩")).lower() or bstack1llll1llll11_opy_.get(bstack1lllll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨ⁪"), bstack1lllll1l_opy_ (u"ࠫࠬ⁫")).lower()
        if browser != bstack1lllll1l_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࠬ⁬"):
            logger.warning(bstack1lllll1l_opy_ (u"ࠨࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡻ࡮ࡲ࡬ࠡࡴࡸࡲࠥࡵ࡮࡭ࡻࠣࡳࡳࠦࡃࡩࡴࡲࡱࡪࠦࡢࡳࡱࡺࡷࡪࡸࡳ࠯ࠤ⁭"))
            return False
        browser_version = caps.get(bstack1lllll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨ⁮")) or caps.get(bstack1lllll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡹࡩࡷࡹࡩࡰࡰࠪ⁯")) or bstack1llll1llll11_opy_.get(bstack1lllll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪ⁰")) or bstack1llll1llll11_opy_.get(bstack1lllll1l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫⁱ"), {}).get(bstack1lllll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬ⁲")) or bstack1llll1llll11_opy_.get(bstack1lllll1l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭⁳"), {}).get(bstack1lllll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨ⁴"))
        bstack1l111l1l1ll_opy_ = bstack1lllll11111l_opy_.bstack1l111l11l1l_opy_
        bstack1lllll1111ll_opy_ = False
        if config is not None:
          bstack1lllll1111ll_opy_ = bstack1lllll1l_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫ⁵") in config and str(config[bstack1lllll1l_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬ⁶")]).lower() != bstack1lllll1l_opy_ (u"ࠩࡩࡥࡱࡹࡥࠨ⁷")
        if os.environ.get(bstack1lllll1l_opy_ (u"ࠪࡍࡘࡥࡎࡐࡐࡢࡆࡘ࡚ࡁࡄࡍࡢࡍࡓࡌࡒࡂࡡࡄ࠵࠶࡟࡟ࡔࡇࡖࡗࡎࡕࡎࠨ⁸"), bstack1lllll1l_opy_ (u"ࠫࠬ⁹")).lower() == bstack1lllll1l_opy_ (u"ࠬࡺࡲࡶࡧࠪ⁺") or bstack1lllll1111ll_opy_:
          bstack1l111l1l1ll_opy_ = bstack1lllll11111l_opy_.bstack1l1111l1111_opy_
        if browser_version and browser_version != bstack1lllll1l_opy_ (u"࠭࡬ࡢࡶࡨࡷࡹ࠭⁻") and int(browser_version.split(bstack1lllll1l_opy_ (u"ࠧ࠯ࠩ⁼"))[0]) <= bstack1l111l1l1ll_opy_:
          logger.warning(bstack11ll1l1l_opy_ (u"ࠨࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡽࡩ࡭࡮ࠣࡶࡺࡴࠠࡰࡰ࡯ࡽࠥࡵ࡮ࠡࡅ࡫ࡶࡴࡳࡥࠡࡤࡵࡳࡼࡹࡥࡳࠢࡹࡩࡷࡹࡩࡰࡰࠣ࡫ࡷ࡫ࡡࡵࡧࡵࠤࡹ࡮ࡡ࡯ࠢࡾࡱ࡮ࡴ࡟ࡢ࠳࠴ࡽࡤࡹࡵࡱࡲࡲࡶࡹ࡫ࡤࡠࡥ࡫ࡶࡴࡳࡥࡠࡸࡨࡶࡸ࡯࡯࡯ࡿ࠱ࠫ⁽"))
          return False
        if not options:
          bstack1l11111ll1l_opy_ = caps.get(bstack1lllll1l_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ⁾")) or bstack1llll1llll11_opy_.get(bstack1lllll1l_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨⁿ"), {})
          if bstack1lllll1l_opy_ (u"ࠫ࠲࠳ࡨࡦࡣࡧࡰࡪࡹࡳࠨ₀") in bstack1l11111ll1l_opy_.get(bstack1lllll1l_opy_ (u"ࠬࡧࡲࡨࡵࠪ₁"), []):
              logger.warning(bstack1lllll1l_opy_ (u"ࠨࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡻ࡮ࡲ࡬ࠡࡰࡲࡸࠥࡸࡵ࡯ࠢࡲࡲࠥࡲࡥࡨࡣࡦࡽࠥ࡮ࡥࡢࡦ࡯ࡩࡸࡹࠠ࡮ࡱࡧࡩ࠳ࠦࡓࡸ࡫ࡷࡧ࡭ࠦࡴࡰࠢࡱࡩࡼࠦࡨࡦࡣࡧࡰࡪࡹࡳࠡ࡯ࡲࡨࡪࠦ࡯ࡳࠢࡤࡺࡴ࡯ࡤࠡࡷࡶ࡭ࡳ࡭ࠠࡩࡧࡤࡨࡱ࡫ࡳࡴࠢࡰࡳࡩ࡫࠮ࠣ₂"))
              return False
        return True
    except Exception as error:
        logger.debug(bstack1lllll1l_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡶࡢ࡮࡬ࡨࡦࡺࡥࠡࡣ࠴࠵ࡾࠦࡳࡶࡲࡳࡳࡷࡺࠠ࠻ࠤ₃") + str(error))
        return False
def set_capabilities(caps, config):
  try:
    bstack1l1l1l111ll_opy_ = config.get(bstack1lllll1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨ₄"), {})
    bstack1l1l1l111ll_opy_[bstack1lllll1l_opy_ (u"ࠩࡤࡹࡹ࡮ࡔࡰ࡭ࡨࡲࠬ₅")] = os.getenv(bstack1lllll1l_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨ₆"))
    bstack111l1l1ll11_opy_ = json.loads(os.getenv(bstack1lllll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡠࡃࡆࡇࡊ࡙ࡓࡊࡄࡌࡐࡎ࡚࡙ࡠࡅࡒࡒࡋࡏࡇࡖࡔࡄࡘࡎࡕࡎࡠ࡛ࡐࡐࠬ₇"), bstack1lllll1l_opy_ (u"ࠬࢁࡽࠨ₈"))).get(bstack1lllll1l_opy_ (u"࠭ࡳࡤࡣࡱࡲࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧ₉"))
    if not config[bstack1lllll1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡖࡲࡰࡦࡸࡧࡹࡓࡡࡱࠩ₊")].get(bstack1lllll1l_opy_ (u"ࠣࡣࡳࡴࡤࡧࡵࡵࡱࡰࡥࡹ࡫ࠢ₋")):
      if bstack1lllll1l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪ₌") in caps:
        caps[bstack1lllll1l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫ₍")][bstack1lllll1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫ₎")] = bstack1l1l1l111ll_opy_
        caps[bstack1lllll1l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭₏")][bstack1lllll1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭ₐ")][bstack1lllll1l_opy_ (u"ࠧࡴࡥࡤࡲࡳ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨₑ")] = bstack111l1l1ll11_opy_
      else:
        caps[bstack1lllll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧₒ")] = bstack1l1l1l111ll_opy_
        caps[bstack1lllll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨₓ")][bstack1lllll1l_opy_ (u"ࠪࡷࡨࡧ࡮࡯ࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫₔ")] = bstack111l1l1ll11_opy_
  except Exception as error:
    logger.debug(bstack1lllll1l_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡸࡪ࡬ࡰࡪࠦࡳࡦࡶࡷ࡭ࡳ࡭ࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵ࠱ࠤࡊࡸࡲࡰࡴ࠽ࠤࠧₕ") +  str(error))
def bstack1ll1lll1l_opy_(driver, bstack1llll1ll111l_opy_):
  try:
    setattr(driver, bstack1lllll1l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡆ࠷࠱ࡺࡕ࡫ࡳࡺࡲࡤࡔࡥࡤࡲࠬₖ"), True)
    session = driver.session_id
    if session:
      bstack1llll1lll111_opy_ = True
      current_url = driver.current_url
      try:
        url = urlparse(current_url)
      except Exception as e:
        bstack1llll1lll111_opy_ = False
      bstack1llll1lll111_opy_ = url.scheme in [bstack1lllll1l_opy_ (u"ࠨࡨࡵࡶࡳࠦₗ"), bstack1lllll1l_opy_ (u"ࠢࡩࡶࡷࡴࡸࠨₘ")]
      if bstack1llll1lll111_opy_:
        if bstack1llll1ll111l_opy_:
          logger.info(bstack1lllll1l_opy_ (u"ࠣࡕࡨࡸࡺࡶࠠࡧࡱࡵࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡹ࡫ࡳࡵ࡫ࡱ࡫ࠥ࡮ࡡࡴࠢࡶࡸࡦࡸࡴࡦࡦ࠱ࠤࡆࡻࡴࡰ࡯ࡤࡸࡪࠦࡴࡦࡵࡷࠤࡨࡧࡳࡦࠢࡨࡼࡪࡩࡵࡵ࡫ࡲࡲࠥࡽࡩ࡭࡮ࠣࡦࡪ࡭ࡩ࡯ࠢࡰࡳࡲ࡫࡮ࡵࡣࡵ࡭ࡱࡿ࠮ࠣₙ"))
      return bstack1llll1ll111l_opy_
  except Exception as e:
    logger.error(bstack1lllll1l_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡵࡷࡥࡷࡺࡩ࡯ࡩࠣࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡴࡥࡤࡲࠥ࡬࡯ࡳࠢࡷ࡬࡮ࡹࠠࡵࡧࡶࡸࠥࡩࡡࡴࡧ࠽ࠤࠧₚ") + str(e))
    return False
def bstack1lllll11l_opy_(driver, name, path):
  try:
    bstack1l111l1l111_opy_ = {
        bstack1lllll1l_opy_ (u"ࠪࡸ࡭࡚ࡥࡴࡶࡕࡹࡳ࡛ࡵࡪࡦࠪₛ"): threading.current_thread().current_test_uuid,
        bstack1lllll1l_opy_ (u"ࠫࡹ࡮ࡂࡶ࡫࡯ࡨ࡚ࡻࡩࡥࠩₜ"): os.environ.get(bstack1lllll1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪ₝"), bstack1lllll1l_opy_ (u"࠭ࠧ₞")),
        bstack1lllll1l_opy_ (u"ࠧࡵࡪࡍࡻࡹ࡚࡯࡬ࡧࡱࠫ₟"): os.environ.get(bstack1lllll1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡌ࡚ࡘࠬ₠"), bstack1lllll1l_opy_ (u"ࠩࠪ₡"))
    }
    bstack1ll111ll1l1_opy_ = bstack111l1111l_opy_.bstack1ll11l111l1_opy_(EVENTS.bstack11111l1l11_opy_.value)
    logger.debug(bstack1lllll1l_opy_ (u"ࠪࡔࡪࡸࡦࡰࡴࡰ࡭ࡳ࡭ࠠࡴࡥࡤࡲࠥࡨࡥࡧࡱࡵࡩࠥࡹࡡࡷ࡫ࡱ࡫ࠥࡸࡥࡴࡷ࡯ࡸࡸ࠭₢"))
    try:
      if (bstack1l11l1l1_opy_(threading.current_thread(), bstack1lllll1l_opy_ (u"ࠫ࡮ࡹࡁࡱࡲࡄ࠵࠶ࡿࡔࡦࡵࡷࠫ₣"), None) and bstack1l11l1l1_opy_(threading.current_thread(), bstack1lllll1l_opy_ (u"ࠬࡧࡰࡱࡃ࠴࠵ࡾࡖ࡬ࡢࡶࡩࡳࡷࡳࠧ₤"), None)):
        scripts = {bstack1lllll1l_opy_ (u"࠭ࡳࡤࡣࡱࠫ₥"): bstack11l11l11ll_opy_.perform_scan}
        bstack1llll1ll1l11_opy_ = json.loads(scripts[bstack1lllll1l_opy_ (u"ࠢࡴࡥࡤࡲࠧ₦")].replace(bstack1lllll1l_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࠦ₧"), bstack1lllll1l_opy_ (u"ࠤࠥ₨")))
        bstack1llll1ll1l11_opy_[bstack1lllll1l_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭₩")][bstack1lllll1l_opy_ (u"ࠫࡲ࡫ࡴࡩࡱࡧࠫ₪")] = None
        scripts[bstack1lllll1l_opy_ (u"ࠧࡹࡣࡢࡰࠥ₫")] = bstack1lllll1l_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࠤ€") + json.dumps(bstack1llll1ll1l11_opy_)
        bstack11l11l11ll_opy_.bstack11lll1lll_opy_(scripts)
        bstack11l11l11ll_opy_.store()
        logger.debug(driver.execute_script(bstack11l11l11ll_opy_.perform_scan))
      else:
        logger.debug(driver.execute_async_script(bstack11l11l11ll_opy_.perform_scan, {bstack1lllll1l_opy_ (u"ࠢ࡮ࡧࡷ࡬ࡴࡪࠢ₭"): name}))
      bstack111l1111l_opy_.end(EVENTS.bstack11111l1l11_opy_.value, bstack1ll111ll1l1_opy_ + bstack1lllll1l_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣ₮"), bstack1ll111ll1l1_opy_ + bstack1lllll1l_opy_ (u"ࠤ࠽ࡩࡳࡪࠢ₯"), True, None)
    except Exception as error:
      bstack111l1111l_opy_.end(EVENTS.bstack11111l1l11_opy_.value, bstack1ll111ll1l1_opy_ + bstack1lllll1l_opy_ (u"ࠥ࠾ࡸࡺࡡࡳࡶࠥ₰"), bstack1ll111ll1l1_opy_ + bstack1lllll1l_opy_ (u"ࠦ࠿࡫࡮ࡥࠤ₱"), False, str(error))
    bstack1ll111ll1l1_opy_ = bstack111l1111l_opy_.bstack11ll1l1l111_opy_(EVENTS.bstack1l111ll1l11_opy_.value)
    bstack111l1111l_opy_.mark(bstack1ll111ll1l1_opy_ + bstack1lllll1l_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧ₲"))
    try:
      if (bstack1l11l1l1_opy_(threading.current_thread(), bstack1lllll1l_opy_ (u"࠭ࡩࡴࡃࡳࡴࡆ࠷࠱ࡺࡖࡨࡷࡹ࠭₳"), None) and bstack1l11l1l1_opy_(threading.current_thread(), bstack1lllll1l_opy_ (u"ࠧࡢࡲࡳࡅ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩ₴"), None)):
        scripts = {bstack1lllll1l_opy_ (u"ࠨࡵࡦࡥࡳ࠭₵"): bstack11l11l11ll_opy_.perform_scan}
        bstack1llll1ll1l11_opy_ = json.loads(scripts[bstack1lllll1l_opy_ (u"ࠤࡶࡧࡦࡴࠢ₶")].replace(bstack1lllll1l_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࠨ₷"), bstack1lllll1l_opy_ (u"ࠦࠧ₸")))
        bstack1llll1ll1l11_opy_[bstack1lllll1l_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨ₹")][bstack1lllll1l_opy_ (u"࠭࡭ࡦࡶ࡫ࡳࡩ࠭₺")] = None
        scripts[bstack1lllll1l_opy_ (u"ࠢࡴࡥࡤࡲࠧ₻")] = bstack1lllll1l_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࠦ₼") + json.dumps(bstack1llll1ll1l11_opy_)
        bstack11l11l11ll_opy_.bstack11lll1lll_opy_(scripts)
        bstack11l11l11ll_opy_.store()
        logger.debug(driver.execute_script(bstack11l11l11ll_opy_.perform_scan))
      else:
        logger.debug(driver.execute_async_script(bstack11l11l11ll_opy_.bstack1lllll111ll1_opy_, bstack1l111l1l111_opy_))
      bstack111l1111l_opy_.end(bstack1ll111ll1l1_opy_, bstack1ll111ll1l1_opy_ + bstack1lllll1l_opy_ (u"ࠤ࠽ࡷࡹࡧࡲࡵࠤ₽"), bstack1ll111ll1l1_opy_ + bstack1lllll1l_opy_ (u"ࠥ࠾ࡪࡴࡤࠣ₾"),True, None)
    except Exception as error:
      bstack111l1111l_opy_.end(bstack1ll111ll1l1_opy_, bstack1ll111ll1l1_opy_ + bstack1lllll1l_opy_ (u"ࠦ࠿ࡹࡴࡢࡴࡷࠦ₿"), bstack1ll111ll1l1_opy_ + bstack1lllll1l_opy_ (u"ࠧࡀࡥ࡯ࡦࠥ⃀"),False, str(error))
    logger.info(bstack1lllll1l_opy_ (u"ࠨࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡴࡦࡵࡷ࡭ࡳ࡭ࠠࡧࡱࡵࠤࡹ࡮ࡩࡴࠢࡷࡩࡸࡺࠠࡤࡣࡶࡩࠥ࡮ࡡࡴࠢࡨࡲࡩ࡫ࡤ࠯ࠤ⃁"))
  except Exception as bstack1l111l1lll1_opy_:
    logger.error(bstack1lllll1l_opy_ (u"ࠢࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡳࡧࡶࡹࡱࡺࡳࠡࡥࡲࡹࡱࡪࠠ࡯ࡱࡷࠤࡧ࡫ࠠࡱࡴࡲࡧࡪࡹࡳࡦࡦࠣࡪࡴࡸࠠࡵࡪࡨࠤࡹ࡫ࡳࡵࠢࡦࡥࡸ࡫࠺ࠡࠤ⃂") + str(path) + bstack1lllll1l_opy_ (u"ࠣࠢࡈࡶࡷࡵࡲࠡ࠼ࠥ⃃") + str(bstack1l111l1lll1_opy_))
def bstack1llll1lll11l_opy_(driver):
    caps = driver.capabilities
    if caps.get(bstack1lllll1l_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰࡒࡦࡳࡥࠣ⃄")) and str(caps.get(bstack1lllll1l_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱࡓࡧ࡭ࡦࠤ⃅"))).lower() == bstack1lllll1l_opy_ (u"ࠦࡦࡴࡤࡳࡱ࡬ࡨࠧ⃆"):
        bstack1l111l1l1l1_opy_ = caps.get(bstack1lllll1l_opy_ (u"ࠧࡧࡰࡱ࡫ࡸࡱ࠿ࡶ࡬ࡢࡶࡩࡳࡷࡳࡖࡦࡴࡶ࡭ࡴࡴࠢ⃇")) or caps.get(bstack1lllll1l_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠣ⃈"))
        if bstack1l111l1l1l1_opy_ and int(str(bstack1l111l1l1l1_opy_)) < bstack11l11lllll1_opy_:
            return False
    return True
def bstack111l1l11l_opy_(config):
  if bstack1lllll1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ⃉") in config:
        return config[bstack1lllll1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ⃊")]
  for platform in config.get(bstack1lllll1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ⃋"), []):
      if bstack1lllll1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ⃌") in platform:
          return platform[bstack1lllll1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ⃍")]
  return None
def bstack1ll11111l_opy_(bstack1lll11111l_opy_):
  try:
    browser_name = bstack1lll11111l_opy_[bstack1lllll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡥ࡮ࡢ࡯ࡨࠫ⃎")]
    browser_version = bstack1lll11111l_opy_[bstack1lllll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨ⃏")]
    chrome_options = bstack1lll11111l_opy_[bstack1lllll1l_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫࡟ࡰࡲࡷ࡭ࡴࡴࡳࠨ⃐")]
    try:
        bstack1llll1l1l1ll_opy_ = int(browser_version.split(bstack1lllll1l_opy_ (u"ࠨ࠰ࠪ⃑"))[0])
    except ValueError as e:
        logger.error(bstack1lllll1l_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡹ࡫࡭ࡱ࡫ࠠࡤࡱࡱࡺࡪࡸࡴࡪࡰࡪࠤࡧࡸ࡯ࡸࡵࡨࡶࠥࡼࡥࡳࡵ࡬ࡳࡳࠨ⃒") + str(e))
        return False
    if not (browser_name and browser_name.lower() == bstack1lllll1l_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧ⃓ࠪ")):
        logger.warning(bstack1lllll1l_opy_ (u"ࠦࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡹ࡬ࡰࡱࠦࡲࡶࡰࠣࡳࡳࡲࡹࠡࡱࡱࠤࡈ࡮ࡲࡰ࡯ࡨࠤࡧࡸ࡯ࡸࡵࡨࡶࡸ࠴ࠢ⃔"))
        return False
    if bstack1llll1l1l1ll_opy_ < bstack1lllll11111l_opy_.bstack1l1111l1111_opy_:
        logger.warning(bstack11ll1l1l_opy_ (u"ࠬࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡵࡩࡶࡻࡩࡳࡧࡶࠤࡈ࡮ࡲࡰ࡯ࡨࠤࡻ࡫ࡲࡴ࡫ࡲࡲࠥࢁࡃࡐࡐࡖࡘࡆࡔࡔࡔ࠰ࡐࡍࡓࡏࡍࡖࡏࡢࡒࡔࡔ࡟ࡃࡕࡗࡅࡈࡑ࡟ࡊࡐࡉࡖࡆࡥࡁ࠲࠳࡜ࡣࡘ࡛ࡐࡑࡑࡕࡘࡊࡊ࡟ࡄࡊࡕࡓࡒࡋ࡟ࡗࡇࡕࡗࡎࡕࡎࡾࠢࡲࡶࠥ࡮ࡩࡨࡪࡨࡶ࠳࠭⃕"))
        return False
    if chrome_options and any(bstack1lllll1l_opy_ (u"࠭࠭࠮ࡪࡨࡥࡩࡲࡥࡴࡵࠪ⃖") in value for value in chrome_options.values() if isinstance(value, str)):
        logger.warning(bstack1lllll1l_opy_ (u"ࠢࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡼ࡯࡬࡭ࠢࡱࡳࡹࠦࡲࡶࡰࠣࡳࡳࠦ࡬ࡦࡩࡤࡧࡾࠦࡨࡦࡣࡧࡰࡪࡹࡳࠡ࡯ࡲࡨࡪ࠴ࠠࡔࡹ࡬ࡸࡨ࡮ࠠࡵࡱࠣࡲࡪࡽࠠࡩࡧࡤࡨࡱ࡫ࡳࡴࠢࡰࡳࡩ࡫ࠠࡰࡴࠣࡥࡻࡵࡩࡥࠢࡸࡷ࡮ࡴࡧࠡࡪࡨࡥࡩࡲࡥࡴࡵࠣࡱࡴࡪࡥ࠯ࠤ⃗"))
        return False
    return True
  except Exception as e:
    logger.error(bstack1lllll1l_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡪࡰࠣࡧ࡭࡫ࡣ࡬࡫ࡱ࡫ࠥࡶ࡬ࡢࡶࡩࡳࡷࡳࠠࡴࡷࡳࡴࡴࡸࡴࠡࡨࡲࡶࠥࡲ࡯ࡤࡣ࡯ࠤࡈ࡮ࡲࡰ࡯ࡨ࠾ࠥࠨ⃘") + str(e))
    return False
def bstack1l111ll1ll_opy_(bstack1ll11llll_opy_, config):
    try:
      bstack1l1111l1lll_opy_ = bstack1lllll1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺ⃙ࠩ") in config and config[bstack1lllll1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻ⃚ࠪ")] == True
      bstack1lllll1111ll_opy_ = bstack1lllll1l_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨ⃛") in config and str(config[bstack1lllll1l_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩ⃜")]).lower() != bstack1lllll1l_opy_ (u"࠭ࡦࡢ࡮ࡶࡩࠬ⃝")
      if not (bstack1l1111l1lll_opy_ and (not bstack111l1lll11_opy_(config) or bstack1lllll1111ll_opy_)):
        return bstack1ll11llll_opy_
      bstack1llll1l1llll_opy_ = bstack11l11l11ll_opy_.bstack1lllll11l11l_opy_
      if bstack1llll1l1llll_opy_ is None:
        logger.debug(bstack1lllll1l_opy_ (u"ࠢࡈࡱࡲ࡫ࡱ࡫ࠠࡤࡪࡵࡳࡲ࡫ࠠࡰࡲࡷ࡭ࡴࡴࡳࠡࡣࡵࡩࠥࡔ࡯࡯ࡧࠥ⃞"))
        return bstack1ll11llll_opy_
      bstack1lllll1111l1_opy_ = int(str(bstack111l11ll111_opy_()).split(bstack1lllll1l_opy_ (u"ࠨ࠰ࠪ⃟"))[0])
      logger.debug(bstack1lllll1l_opy_ (u"ࠤࡖࡩࡱ࡫࡮ࡪࡷࡰࠤࡻ࡫ࡲࡴ࡫ࡲࡲࠥࡪࡥࡵࡧࡦࡸࡪࡪ࠺ࠡࠤ⃠") + str(bstack1lllll1111l1_opy_) + bstack1lllll1l_opy_ (u"ࠥࠦ⃡"))
      if bstack1lllll1111l1_opy_ == 3 and isinstance(bstack1ll11llll_opy_, dict) and bstack1lllll1l_opy_ (u"ࠫࡩ࡫ࡳࡪࡴࡨࡨࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠫ⃢") in bstack1ll11llll_opy_ and bstack1llll1l1llll_opy_ is not None:
        if bstack1lllll1l_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ⃣") not in bstack1ll11llll_opy_[bstack1lllll1l_opy_ (u"࠭ࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠭⃤")]:
          bstack1ll11llll_opy_[bstack1lllll1l_opy_ (u"ࠧࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹ⃥ࠧ")][bstack1lllll1l_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ⃦࠭")] = {}
        if bstack1lllll1l_opy_ (u"ࠩࡤࡶ࡬ࡹࠧ⃧") in bstack1llll1l1llll_opy_:
          if bstack1lllll1l_opy_ (u"ࠪࡥࡷ࡭ࡳࠨ⃨") not in bstack1ll11llll_opy_[bstack1lllll1l_opy_ (u"ࠫࡩ࡫ࡳࡪࡴࡨࡨࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠫ⃩")][bstack1lllll1l_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵ⃪ࠪ")]:
            bstack1ll11llll_opy_[bstack1lllll1l_opy_ (u"࠭ࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ⃫࠭")][bstack1lllll1l_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷ⃬ࠬ")][bstack1lllll1l_opy_ (u"ࠨࡣࡵ࡫ࡸ⃭࠭")] = []
          for arg in bstack1llll1l1llll_opy_[bstack1lllll1l_opy_ (u"ࠩࡤࡶ࡬ࡹ⃮ࠧ")]:
            if arg not in bstack1ll11llll_opy_[bstack1lllll1l_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵ⃯ࠪ")][bstack1lllll1l_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩ⃰")][bstack1lllll1l_opy_ (u"ࠬࡧࡲࡨࡵࠪ⃱")]:
              bstack1ll11llll_opy_[bstack1lllll1l_opy_ (u"࠭ࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠭⃲")][bstack1lllll1l_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬ⃳")][bstack1lllll1l_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭⃴")].append(arg)
        if bstack1lllll1l_opy_ (u"ࠩࡨࡼࡹ࡫࡮ࡴ࡫ࡲࡲࡸ࠭⃵") in bstack1llll1l1llll_opy_:
          if bstack1lllll1l_opy_ (u"ࠪࡩࡽࡺࡥ࡯ࡵ࡬ࡳࡳࡹࠧ⃶") not in bstack1ll11llll_opy_[bstack1lllll1l_opy_ (u"ࠫࡩ࡫ࡳࡪࡴࡨࡨࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠫ⃷")][bstack1lllll1l_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ⃸")]:
            bstack1ll11llll_opy_[bstack1lllll1l_opy_ (u"࠭ࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠭⃹")][bstack1lllll1l_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬ⃺")][bstack1lllll1l_opy_ (u"ࠨࡧࡻࡸࡪࡴࡳࡪࡱࡱࡷࠬ⃻")] = []
          for ext in bstack1llll1l1llll_opy_[bstack1lllll1l_opy_ (u"ࠩࡨࡼࡹ࡫࡮ࡴ࡫ࡲࡲࡸ࠭⃼")]:
            if ext not in bstack1ll11llll_opy_[bstack1lllll1l_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪ⃽")][bstack1lllll1l_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩ⃾")][bstack1lllll1l_opy_ (u"ࠬ࡫ࡸࡵࡧࡱࡷ࡮ࡵ࡮ࡴࠩ⃿")]:
              bstack1ll11llll_opy_[bstack1lllll1l_opy_ (u"࠭ࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠭℀")][bstack1lllll1l_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬ℁")][bstack1lllll1l_opy_ (u"ࠨࡧࡻࡸࡪࡴࡳࡪࡱࡱࡷࠬℂ")].append(ext)
        if bstack1lllll1l_opy_ (u"ࠩࡳࡶࡪ࡬ࡳࠨ℃") in bstack1llll1l1llll_opy_:
          if bstack1lllll1l_opy_ (u"ࠪࡴࡷ࡫ࡦࡴࠩ℄") not in bstack1ll11llll_opy_[bstack1lllll1l_opy_ (u"ࠫࡩ࡫ࡳࡪࡴࡨࡨࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠫ℅")][bstack1lllll1l_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ℆")]:
            bstack1ll11llll_opy_[bstack1lllll1l_opy_ (u"࠭ࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠭ℇ")][bstack1lllll1l_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬ℈")][bstack1lllll1l_opy_ (u"ࠨࡲࡵࡩ࡫ࡹࠧ℉")] = {}
          bstack1111l1llll1_opy_(bstack1ll11llll_opy_[bstack1lllll1l_opy_ (u"ࠩࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩℊ")][bstack1lllll1l_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨℋ")][bstack1lllll1l_opy_ (u"ࠫࡵࡸࡥࡧࡵࠪℌ")],
                    bstack1llll1l1llll_opy_[bstack1lllll1l_opy_ (u"ࠬࡶࡲࡦࡨࡶࠫℍ")])
        os.environ[bstack1lllll1l_opy_ (u"࠭ࡉࡔࡡࡑࡓࡓࡥࡂࡔࡖࡄࡇࡐࡥࡉࡏࡈࡕࡅࡤࡇ࠱࠲࡛ࡢࡗࡊ࡙ࡓࡊࡑࡑࠫℎ")] = bstack1lllll1l_opy_ (u"ࠧࡵࡴࡸࡩࠬℏ")
        return bstack1ll11llll_opy_
      else:
        chrome_options = None
        if isinstance(bstack1ll11llll_opy_, ChromeOptions):
          chrome_options = bstack1ll11llll_opy_
        elif isinstance(bstack1ll11llll_opy_, dict):
          for value in bstack1ll11llll_opy_.values():
            if isinstance(value, ChromeOptions):
              chrome_options = value
              break
        if chrome_options is None:
          chrome_options = ChromeOptions()
          if isinstance(bstack1ll11llll_opy_, dict):
            bstack1ll11llll_opy_[bstack1lllll1l_opy_ (u"ࠨࡱࡳࡸ࡮ࡵ࡮ࡴࠩℐ")] = chrome_options
          else:
            bstack1ll11llll_opy_ = chrome_options
        if bstack1llll1l1llll_opy_ is not None:
          if bstack1lllll1l_opy_ (u"ࠩࡤࡶ࡬ࡹࠧℑ") in bstack1llll1l1llll_opy_:
                bstack1llll1ll1l1l_opy_ = chrome_options.arguments or []
                new_args = bstack1llll1l1llll_opy_[bstack1lllll1l_opy_ (u"ࠪࡥࡷ࡭ࡳࠨℒ")]
                for arg in new_args:
                    if arg not in bstack1llll1ll1l1l_opy_:
                        chrome_options.add_argument(arg)
          if bstack1lllll1l_opy_ (u"ࠫࡪࡾࡴࡦࡰࡶ࡭ࡴࡴࡳࠨℓ") in bstack1llll1l1llll_opy_:
                existing_extensions = chrome_options.experimental_options.get(bstack1lllll1l_opy_ (u"ࠬ࡫ࡸࡵࡧࡱࡷ࡮ࡵ࡮ࡴࠩ℔"), [])
                bstack1llll1l1ll11_opy_ = bstack1llll1l1llll_opy_[bstack1lllll1l_opy_ (u"࠭ࡥࡹࡶࡨࡲࡸ࡯࡯࡯ࡵࠪℕ")]
                for extension in bstack1llll1l1ll11_opy_:
                    if extension not in existing_extensions:
                        chrome_options.add_encoded_extension(extension)
          if bstack1lllll1l_opy_ (u"ࠧࡱࡴࡨࡪࡸ࠭№") in bstack1llll1l1llll_opy_:
                bstack1llll1lll1ll_opy_ = chrome_options.experimental_options.get(bstack1lllll1l_opy_ (u"ࠨࡲࡵࡩ࡫ࡹࠧ℗"), {})
                bstack1llll1ll1lll_opy_ = bstack1llll1l1llll_opy_[bstack1lllll1l_opy_ (u"ࠩࡳࡶࡪ࡬ࡳࠨ℘")]
                bstack1111l1llll1_opy_(bstack1llll1lll1ll_opy_, bstack1llll1ll1lll_opy_)
                chrome_options.add_experimental_option(bstack1lllll1l_opy_ (u"ࠪࡴࡷ࡫ࡦࡴࠩℙ"), bstack1llll1lll1ll_opy_)
        os.environ[bstack1lllll1l_opy_ (u"ࠫࡎ࡙࡟ࡏࡑࡑࡣࡇ࡙ࡔࡂࡅࡎࡣࡎࡔࡆࡓࡃࡢࡅ࠶࠷࡙ࡠࡕࡈࡗࡘࡏࡏࡏࠩℚ")] = bstack1lllll1l_opy_ (u"ࠬࡺࡲࡶࡧࠪℛ")
        return bstack1ll11llll_opy_
    except Exception as e:
      logger.error(bstack1lllll1l_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡽࡨࡪ࡮ࡨࠤࡦࡪࡤࡪࡰࡪࠤࡳࡵ࡮࠮ࡄࡖࠤ࡮ࡴࡦࡳࡣࠣࡥ࠶࠷ࡹࠡࡥ࡫ࡶࡴࡳࡥࠡࡱࡳࡸ࡮ࡵ࡮ࡴ࠼ࠣࠦℜ") + str(e))
      return bstack1ll11llll_opy_