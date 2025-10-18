# coding: UTF-8
import sys
bstack11ll1l1_opy_ = sys.version_info [0] == 2
bstack11111ll_opy_ = 2048
bstack111lll1_opy_ = 7
def bstack1l1lll1_opy_ (bstack1lllll_opy_):
    global bstack111111l_opy_
    bstack1llll_opy_ = ord (bstack1lllll_opy_ [-1])
    bstack11lll1l_opy_ = bstack1lllll_opy_ [:-1]
    bstack1111_opy_ = bstack1llll_opy_ % len (bstack11lll1l_opy_)
    bstack11ll11l_opy_ = bstack11lll1l_opy_ [:bstack1111_opy_] + bstack11lll1l_opy_ [bstack1111_opy_:]
    if bstack11ll1l1_opy_:
        bstack1llll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    else:
        bstack1llll1_opy_ = str () .join ([chr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    return eval (bstack1llll1_opy_)
import os
import json
import requests
import logging
import threading
import bstack_utils.constants as bstack1lllll111ll1_opy_
from urllib.parse import urlparse
from bstack_utils.constants import bstack11l1l1l11ll_opy_ as bstack1llll1ll11l1_opy_, EVENTS
from bstack_utils.bstack1l11111ll_opy_ import bstack1l11111ll_opy_
from bstack_utils.helper import bstack1ll1llll_opy_, bstack1l11111l_opy_, bstack1l1l1l1l1_opy_, bstack111l1111l1l_opy_, \
  bstack111l11ll1ll_opy_, bstack11lll11l11_opy_, get_host_info, bstack1111llll1ll_opy_, bstack1l1l1l1l1l_opy_, error_handler, bstack1111l1ll1ll_opy_, bstack1111ll1l111_opy_, bstack1l1l1l1l_opy_
from browserstack_sdk._version import __version__
from bstack_utils.bstack111l11l1l_opy_ import get_logger
from bstack_utils.bstack11l1l1111l_opy_ import bstack1llll1ll11l_opy_
from selenium.webdriver.chrome.options import Options as ChromeOptions
from browserstack_sdk.sdk_cli.cli import cli
from bstack_utils.constants import *
logger = get_logger(__name__)
bstack11l1l1111l_opy_ = bstack1llll1ll11l_opy_()
@error_handler(class_method=False)
def _1lllll111l11_opy_(driver, bstack1111l1l1_opy_):
  response = {}
  try:
    caps = driver.capabilities
    response = {
        bstack1l1lll1_opy_ (u"ࠬࡵࡳࡠࡰࡤࡱࡪ࠭ῄ"): caps.get(bstack1l1lll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡏࡣࡰࡩࠬ῅"), None),
        bstack1l1lll1_opy_ (u"ࠧࡰࡵࡢࡺࡪࡸࡳࡪࡱࡱࠫῆ"): bstack1111l1l1_opy_.get(bstack1l1lll1_opy_ (u"ࠨࡱࡶ࡚ࡪࡸࡳࡪࡱࡱࠫῇ"), None),
        bstack1l1lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡲࡦࡳࡥࠨῈ"): caps.get(bstack1l1lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨΈ"), None),
        bstack1l1lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭Ὴ"): caps.get(bstack1l1lll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭Ή"), None)
    }
  except Exception as error:
    logger.debug(bstack1l1lll1_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥ࡬ࡥࡵࡥ࡫࡭ࡳ࡭ࠠࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࠢࡧࡩࡹࡧࡩ࡭ࡵࠣࡻ࡮ࡺࡨࠡࡧࡵࡶࡴࡸࠠ࠻ࠢࠪῌ") + str(error))
  return response
def on():
    if os.environ.get(bstack1l1lll1_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠬ῍"), None) is None or os.environ[bstack1l1lll1_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭῎")] == bstack1l1lll1_opy_ (u"ࠤࡱࡹࡱࡲࠢ῏"):
        return False
    return True
def bstack11ll11ll1l_opy_(config):
  return config.get(bstack1l1lll1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪῐ"), False) or any([p.get(bstack1l1lll1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫῑ"), False) == True for p in config.get(bstack1l1lll1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨῒ"), [])])
def bstack11lll1lll_opy_(config, bstack1l11l1lll_opy_):
  try:
    bstack1llll1ll1ll1_opy_ = config.get(bstack1l1lll1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ΐ"), False)
    if int(bstack1l11l1lll_opy_) < len(config.get(bstack1l1lll1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ῔"), [])) and config[bstack1l1lll1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ῕")][bstack1l11l1lll_opy_]:
      bstack1llll1llllll_opy_ = config[bstack1l1lll1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬῖ")][bstack1l11l1lll_opy_].get(bstack1l1lll1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪῗ"), None)
    else:
      bstack1llll1llllll_opy_ = config.get(bstack1l1lll1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫῘ"), None)
    if bstack1llll1llllll_opy_ != None:
      bstack1llll1ll1ll1_opy_ = bstack1llll1llllll_opy_
    bstack1llll1llll11_opy_ = os.getenv(bstack1l1lll1_opy_ (u"ࠬࡈࡓࡠࡃ࠴࠵࡞ࡥࡊࡘࡖࠪῙ")) is not None and len(os.getenv(bstack1l1lll1_opy_ (u"࠭ࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗࠫῚ"))) > 0 and os.getenv(bstack1l1lll1_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠬΊ")) != bstack1l1lll1_opy_ (u"ࠨࡰࡸࡰࡱ࠭῜")
    return bstack1llll1ll1ll1_opy_ and bstack1llll1llll11_opy_
  except Exception as error:
    logger.debug(bstack1l1lll1_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡸࡨࡶ࡮࡬ࡹࡪࡰࡪࠤࡹ࡮ࡥࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡺ࡭ࡹ࡮ࠠࡦࡴࡵࡳࡷࠦ࠺ࠡࠩ῝") + str(error))
  return False
def bstack1ll11111l1_opy_(test_tags):
  bstack1l111l1ll11_opy_ = os.getenv(bstack1l1lll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚࡟ࡂࡅࡆࡉࡘ࡙ࡉࡃࡋࡏࡍ࡙࡟࡟ࡄࡑࡑࡊࡎࡍࡕࡓࡃࡗࡍࡔࡔ࡟࡚ࡏࡏࠫ῞"))
  if bstack1l111l1ll11_opy_ is None:
    return True
  bstack1l111l1ll11_opy_ = json.loads(bstack1l111l1ll11_opy_)
  try:
    include_tags = bstack1l111l1ll11_opy_[bstack1l1lll1_opy_ (u"ࠫ࡮ࡴࡣ࡭ࡷࡧࡩ࡙ࡧࡧࡴࡋࡱࡘࡪࡹࡴࡪࡰࡪࡗࡨࡵࡰࡦࠩ῟")] if bstack1l1lll1_opy_ (u"ࠬ࡯࡮ࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪῠ") in bstack1l111l1ll11_opy_ and isinstance(bstack1l111l1ll11_opy_[bstack1l1lll1_opy_ (u"࠭ࡩ࡯ࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫῡ")], list) else []
    exclude_tags = bstack1l111l1ll11_opy_[bstack1l1lll1_opy_ (u"ࠧࡦࡺࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩࠬῢ")] if bstack1l1lll1_opy_ (u"ࠨࡧࡻࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ࠭ΰ") in bstack1l111l1ll11_opy_ and isinstance(bstack1l111l1ll11_opy_[bstack1l1lll1_opy_ (u"ࠩࡨࡼࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧῤ")], list) else []
    excluded = any(tag in exclude_tags for tag in test_tags)
    included = len(include_tags) == 0 or any(tag in include_tags for tag in test_tags)
    return not excluded and included
  except Exception as error:
    logger.debug(bstack1l1lll1_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡺ࡬࡮ࡲࡥࠡࡸࡤࡰ࡮ࡪࡡࡵ࡫ࡱ࡫ࠥࡺࡥࡴࡶࠣࡧࡦࡹࡥࠡࡨࡲࡶࠥࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡨࡥࡧࡱࡵࡩࠥࡹࡣࡢࡰࡱ࡭ࡳ࡭࠮ࠡࡇࡵࡶࡴࡸࠠ࠻ࠢࠥῥ") + str(error))
  return False
def bstack1lllll111l1l_opy_(config, frameworkName, bstack1llll1lll111_opy_, bstack1llll1llll1l_opy_):
  bstack1llll1lll1l1_opy_ = bstack111l1111l1l_opy_(config)
  bstack1lllll11l1l1_opy_ = bstack111l11ll1ll_opy_(config)
  if bstack1llll1lll1l1_opy_ is None or bstack1lllll11l1l1_opy_ is None:
    logger.error(bstack1l1lll1_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡸࡪ࡬ࡰࡪࠦࡣࡳࡧࡤࡸ࡮ࡴࡧࠡࡶࡨࡷࡹࠦࡲࡶࡰࠣࡪࡴࡸࠠࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰ࠽ࠤࡒ࡯ࡳࡴ࡫ࡱ࡫ࠥࡧࡵࡵࡪࡨࡲࡹ࡯ࡣࡢࡶ࡬ࡳࡳࠦࡴࡰ࡭ࡨࡲࠬῦ"))
    return [None, None]
  try:
    settings = json.loads(os.getenv(bstack1l1lll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡡࡄࡇࡈࡋࡓࡔࡋࡅࡍࡑࡏࡔ࡚ࡡࡆࡓࡓࡌࡉࡈࡗࡕࡅ࡙ࡏࡏࡏࡡ࡜ࡑࡑ࠭ῧ"), bstack1l1lll1_opy_ (u"࠭ࡻࡾࠩῨ")))
    data = {
        bstack1l1lll1_opy_ (u"ࠧࡱࡴࡲ࡮ࡪࡩࡴࡏࡣࡰࡩࠬῩ"): config[bstack1l1lll1_opy_ (u"ࠨࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪ࠭Ὺ")],
        bstack1l1lll1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬΎ"): config.get(bstack1l1lll1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭Ῥ"), os.path.basename(os.getcwd())),
        bstack1l1lll1_opy_ (u"ࠫࡸࡺࡡࡳࡶࡗ࡭ࡲ࡫ࠧ῭"): bstack1ll1llll_opy_(),
        bstack1l1lll1_opy_ (u"ࠬࡪࡥࡴࡥࡵ࡭ࡵࡺࡩࡰࡰࠪ΅"): config.get(bstack1l1lll1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡉ࡫ࡳࡤࡴ࡬ࡴࡹ࡯࡯࡯ࠩ`"), bstack1l1lll1_opy_ (u"ࠧࠨ῰")),
        bstack1l1lll1_opy_ (u"ࠨࡵࡲࡹࡷࡩࡥࠨ῱"): {
            bstack1l1lll1_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡓࡧ࡭ࡦࠩῲ"): frameworkName,
            bstack1l1lll1_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ῳ"): bstack1llll1lll111_opy_,
            bstack1l1lll1_opy_ (u"ࠫࡸࡪ࡫ࡗࡧࡵࡷ࡮ࡵ࡮ࠨῴ"): __version__,
            bstack1l1lll1_opy_ (u"ࠬࡲࡡ࡯ࡩࡸࡥ࡬࡫ࠧ῵"): bstack1l1lll1_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭ῶ"),
            bstack1l1lll1_opy_ (u"ࠧࡵࡧࡶࡸࡋࡸࡡ࡮ࡧࡺࡳࡷࡱࠧῷ"): bstack1l1lll1_opy_ (u"ࠨࡵࡨࡰࡪࡴࡩࡶ࡯ࠪῸ"),
            bstack1l1lll1_opy_ (u"ࠩࡷࡩࡸࡺࡆࡳࡣࡰࡩࡼࡵࡲ࡬ࡘࡨࡶࡸ࡯࡯࡯ࠩΌ"): bstack1llll1llll1l_opy_
        },
        bstack1l1lll1_opy_ (u"ࠪࡷࡪࡺࡴࡪࡰࡪࡷࠬῺ"): settings,
        bstack1l1lll1_opy_ (u"ࠫࡻ࡫ࡲࡴ࡫ࡲࡲࡈࡵ࡮ࡵࡴࡲࡰࠬΏ"): bstack1111llll1ll_opy_(),
        bstack1l1lll1_opy_ (u"ࠬࡩࡩࡊࡰࡩࡳࠬῼ"): bstack11lll11l11_opy_(),
        bstack1l1lll1_opy_ (u"࠭ࡨࡰࡵࡷࡍࡳ࡬࡯ࠨ´"): get_host_info(),
        bstack1l1lll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠩ῾"): bstack1l1l1l1l1_opy_(config)
    }
    headers = {
        bstack1l1lll1_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡗࡽࡵ࡫ࠧ῿"): bstack1l1lll1_opy_ (u"ࠩࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯࡫ࡵࡲࡲࠬ "),
    }
    config = {
        bstack1l1lll1_opy_ (u"ࠪࡥࡺࡺࡨࠨ "): (bstack1llll1lll1l1_opy_, bstack1lllll11l1l1_opy_),
        bstack1l1lll1_opy_ (u"ࠫ࡭࡫ࡡࡥࡧࡵࡷࠬ "): headers
    }
    response = bstack1l1l1l1l1l_opy_(bstack1l1lll1_opy_ (u"ࠬࡖࡏࡔࡖࠪ "), bstack1llll1ll11l1_opy_ + bstack1l1lll1_opy_ (u"࠭࠯ࡷ࠴࠲ࡸࡪࡹࡴࡠࡴࡸࡲࡸ࠭ "), data, config)
    bstack1lllll11ll11_opy_ = response.json()
    if bstack1lllll11ll11_opy_[bstack1l1lll1_opy_ (u"ࠧࡴࡷࡦࡧࡪࡹࡳࠨ ")]:
      parsed = json.loads(os.getenv(bstack1l1lll1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡤࡇࡃࡄࡇࡖࡗࡎࡈࡉࡍࡋࡗ࡝ࡤࡉࡏࡏࡈࡌࡋ࡚ࡘࡁࡕࡋࡒࡒࡤ࡟ࡍࡍࠩ "), bstack1l1lll1_opy_ (u"ࠩࡾࢁࠬ ")))
      parsed[bstack1l1lll1_opy_ (u"ࠪࡷࡨࡧ࡮࡯ࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫ ")] = bstack1lllll11ll11_opy_[bstack1l1lll1_opy_ (u"ࠫࡩࡧࡴࡢࠩ ")][bstack1l1lll1_opy_ (u"ࠬࡹࡣࡢࡰࡱࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ ")]
      os.environ[bstack1l1lll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡢࡅࡈࡉࡅࡔࡕࡌࡆࡎࡒࡉࡕ࡛ࡢࡇࡔࡔࡆࡊࡉࡘࡖࡆ࡚ࡉࡐࡐࡢ࡝ࡒࡒࠧ​")] = json.dumps(parsed)
      bstack1l11111ll_opy_.bstack11l11l1ll_opy_(bstack1lllll11ll11_opy_[bstack1l1lll1_opy_ (u"ࠧࡥࡣࡷࡥࠬ‌")][bstack1l1lll1_opy_ (u"ࠨࡵࡦࡶ࡮ࡶࡴࡴࠩ‍")])
      bstack1l11111ll_opy_.bstack1lllll1l11l1_opy_(bstack1lllll11ll11_opy_[bstack1l1lll1_opy_ (u"ࠩࡧࡥࡹࡧࠧ‎")][bstack1l1lll1_opy_ (u"ࠪࡧࡴࡳ࡭ࡢࡰࡧࡷࠬ‏")])
      bstack1l11111ll_opy_.store()
      return bstack1lllll11ll11_opy_[bstack1l1lll1_opy_ (u"ࠫࡩࡧࡴࡢࠩ‐")][bstack1l1lll1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽ࡙ࡵ࡫ࡦࡰࠪ‑")], bstack1lllll11ll11_opy_[bstack1l1lll1_opy_ (u"࠭ࡤࡢࡶࡤࠫ‒")][bstack1l1lll1_opy_ (u"ࠧࡪࡦࠪ–")]
    else:
      logger.error(bstack1l1lll1_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡼ࡮ࡩ࡭ࡧࠣࡶࡺࡴ࡮ࡪࡰࡪࠤࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࠺ࠡࠩ—") + bstack1lllll11ll11_opy_[bstack1l1lll1_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ―")])
      if bstack1lllll11ll11_opy_[bstack1l1lll1_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ‖")] == bstack1l1lll1_opy_ (u"ࠫࡎࡴࡶࡢ࡮࡬ࡨࠥࡩ࡯࡯ࡨ࡬࡫ࡺࡸࡡࡵ࡫ࡲࡲࠥࡶࡡࡴࡵࡨࡨ࠳࠭‗"):
        for bstack1llll1ll1111_opy_ in bstack1lllll11ll11_opy_[bstack1l1lll1_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࡷࠬ‘")]:
          logger.error(bstack1llll1ll1111_opy_[bstack1l1lll1_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ’")])
      return None, None
  except Exception as error:
    logger.error(bstack1l1lll1_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡻ࡭࡯࡬ࡦࠢࡦࡶࡪࡧࡴࡪࡰࡪࠤࡹ࡫ࡳࡵࠢࡵࡹࡳࠦࡦࡰࡴࠣࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡀࠠࠣ‚") +  str(error))
    return None, None
def bstack1lllll11l111_opy_():
  if os.getenv(bstack1l1lll1_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭‛")) is None:
    return {
        bstack1l1lll1_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩ“"): bstack1l1lll1_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩ”"),
        bstack1l1lll1_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ„"): bstack1l1lll1_opy_ (u"ࠬࡈࡵࡪ࡮ࡧࠤࡨࡸࡥࡢࡶ࡬ࡳࡳࠦࡨࡢࡦࠣࡪࡦ࡯࡬ࡦࡦ࠱ࠫ‟")
    }
  data = {bstack1l1lll1_opy_ (u"࠭ࡥ࡯ࡦࡗ࡭ࡲ࡫ࠧ†"): bstack1ll1llll_opy_()}
  headers = {
      bstack1l1lll1_opy_ (u"ࠧࡂࡷࡷ࡬ࡴࡸࡩࡻࡣࡷ࡭ࡴࡴࠧ‡"): bstack1l1lll1_opy_ (u"ࠨࡄࡨࡥࡷ࡫ࡲࠡࠩ•") + os.getenv(bstack1l1lll1_opy_ (u"ࠤࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠢ‣")),
      bstack1l1lll1_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱࡙ࡿࡰࡦࠩ․"): bstack1l1lll1_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧ‥")
  }
  response = bstack1l1l1l1l1l_opy_(bstack1l1lll1_opy_ (u"ࠬࡖࡕࡕࠩ…"), bstack1llll1ll11l1_opy_ + bstack1l1lll1_opy_ (u"࠭࠯ࡵࡧࡶࡸࡤࡸࡵ࡯ࡵ࠲ࡷࡹࡵࡰࠨ‧"), data, { bstack1l1lll1_opy_ (u"ࠧࡩࡧࡤࡨࡪࡸࡳࠨ "): headers })
  try:
    if response.status_code == 200:
      logger.info(bstack1l1lll1_opy_ (u"ࠣࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤ࡙࡫ࡳࡵࠢࡕࡹࡳࠦ࡭ࡢࡴ࡮ࡩࡩࠦࡡࡴࠢࡦࡳࡲࡶ࡬ࡦࡶࡨࡨࠥࡧࡴࠡࠤ ") + bstack1l11111l_opy_().isoformat() + bstack1l1lll1_opy_ (u"ࠩ࡝ࠫ‪"))
      return {bstack1l1lll1_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪ‫"): bstack1l1lll1_opy_ (u"ࠫࡸࡻࡣࡤࡧࡶࡷࠬ‬"), bstack1l1lll1_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭‭"): bstack1l1lll1_opy_ (u"࠭ࠧ‮")}
    else:
      response.raise_for_status()
  except requests.RequestException as error:
    logger.error(bstack1l1lll1_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡻ࡭࡯࡬ࡦࠢࡰࡥࡷࡱࡩ࡯ࡩࠣࡧࡴࡳࡰ࡭ࡧࡷ࡭ࡴࡴࠠࡰࡨࠣࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡔࡦࡵࡷࠤࡗࡻ࡮࠻ࠢࠥ ") + str(error))
    return {
        bstack1l1lll1_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨ‰"): bstack1l1lll1_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨ‱"),
        bstack1l1lll1_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ′"): str(error)
    }
def bstack1llll1ll1l1l_opy_(bstack1lllll111lll_opy_):
    return re.match(bstack1l1lll1_opy_ (u"ࡶࠬࡤ࡜ࡥ࠭ࠫࡠ࠳ࡢࡤࠬࠫࡂࠨࠬ″"), bstack1lllll111lll_opy_.strip()) is not None
def bstack1l11ll1l11_opy_(caps, options, desired_capabilities={}, config=None):
    try:
        if options:
          bstack1llll1ll1lll_opy_ = options.to_capabilities()
        elif desired_capabilities:
          bstack1llll1ll1lll_opy_ = desired_capabilities
        else:
          bstack1llll1ll1lll_opy_ = {}
        bstack1l111l11lll_opy_ = (bstack1llll1ll1lll_opy_.get(bstack1l1lll1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡎࡢ࡯ࡨࠫ‴"), bstack1l1lll1_opy_ (u"࠭ࠧ‵")).lower() or caps.get(bstack1l1lll1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡐࡤࡱࡪ࠭‶"), bstack1l1lll1_opy_ (u"ࠨࠩ‷")).lower())
        if bstack1l111l11lll_opy_ == bstack1l1lll1_opy_ (u"ࠩ࡬ࡳࡸ࠭‸"):
            return True
        if bstack1l111l11lll_opy_ == bstack1l1lll1_opy_ (u"ࠪࡥࡳࡪࡲࡰ࡫ࡧࠫ‹"):
            bstack1l111l1l111_opy_ = str(float(caps.get(bstack1l1lll1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲ࡜ࡥࡳࡵ࡬ࡳࡳ࠭›")) or bstack1llll1ll1lll_opy_.get(bstack1l1lll1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭※"), {}).get(bstack1l1lll1_opy_ (u"࠭࡯ࡴࡘࡨࡶࡸ࡯࡯࡯ࠩ‼"),bstack1l1lll1_opy_ (u"ࠧࠨ‽"))))
            if bstack1l111l11lll_opy_ == bstack1l1lll1_opy_ (u"ࠨࡣࡱࡨࡷࡵࡩࡥࠩ‾") and int(bstack1l111l1l111_opy_.split(bstack1l1lll1_opy_ (u"ࠩ࠱ࠫ‿"))[0]) < float(bstack11l11ll1l1l_opy_):
                logger.warning(str(bstack11l1l1l1111_opy_))
                return False
            return True
        bstack1l111l1lll1_opy_ = caps.get(bstack1l1lll1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫ⁀"), {}).get(bstack1l1lll1_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࡒࡦࡳࡥࠨ⁁"), caps.get(bstack1l1lll1_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࠬ⁂"), bstack1l1lll1_opy_ (u"࠭ࠧ⁃")))
        if bstack1l111l1lll1_opy_:
            logger.warning(bstack1l1lll1_opy_ (u"ࠢࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡼ࡯࡬࡭ࠢࡵࡹࡳࠦ࡯࡯࡮ࡼࠤࡴࡴࠠࡅࡧࡶ࡯ࡹࡵࡰࠡࡤࡵࡳࡼࡹࡥࡳࡵ࠱ࠦ⁄"))
            return False
        browser = caps.get(bstack1l1lll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭⁅"), bstack1l1lll1_opy_ (u"ࠩࠪ⁆")).lower() or bstack1llll1ll1lll_opy_.get(bstack1l1lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨ⁇"), bstack1l1lll1_opy_ (u"ࠫࠬ⁈")).lower()
        if browser != bstack1l1lll1_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࠬ⁉"):
            logger.warning(bstack1l1lll1_opy_ (u"ࠨࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡻ࡮ࡲ࡬ࠡࡴࡸࡲࠥࡵ࡮࡭ࡻࠣࡳࡳࠦࡃࡩࡴࡲࡱࡪࠦࡢࡳࡱࡺࡷࡪࡸࡳ࠯ࠤ⁊"))
            return False
        browser_version = caps.get(bstack1l1lll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨ⁋")) or caps.get(bstack1l1lll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡹࡩࡷࡹࡩࡰࡰࠪ⁌")) or bstack1llll1ll1lll_opy_.get(bstack1l1lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪ⁍")) or bstack1llll1ll1lll_opy_.get(bstack1l1lll1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫ⁎"), {}).get(bstack1l1lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬ⁏")) or bstack1llll1ll1lll_opy_.get(bstack1l1lll1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭⁐"), {}).get(bstack1l1lll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨ⁑"))
        bstack1l111ll1ll1_opy_ = bstack1lllll111ll1_opy_.bstack1l1111lllll_opy_
        bstack1llll1ll111l_opy_ = False
        if config is not None:
          bstack1llll1ll111l_opy_ = bstack1l1lll1_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫ⁒") in config and str(config[bstack1l1lll1_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬ⁓")]).lower() != bstack1l1lll1_opy_ (u"ࠩࡩࡥࡱࡹࡥࠨ⁔")
        if os.environ.get(bstack1l1lll1_opy_ (u"ࠪࡍࡘࡥࡎࡐࡐࡢࡆࡘ࡚ࡁࡄࡍࡢࡍࡓࡌࡒࡂࡡࡄ࠵࠶࡟࡟ࡔࡇࡖࡗࡎࡕࡎࠨ⁕"), bstack1l1lll1_opy_ (u"ࠫࠬ⁖")).lower() == bstack1l1lll1_opy_ (u"ࠬࡺࡲࡶࡧࠪ⁗") or bstack1llll1ll111l_opy_:
          bstack1l111ll1ll1_opy_ = bstack1lllll111ll1_opy_.bstack1l111llll11_opy_
        if browser_version and browser_version != bstack1l1lll1_opy_ (u"࠭࡬ࡢࡶࡨࡷࡹ࠭⁘") and int(browser_version.split(bstack1l1lll1_opy_ (u"ࠧ࠯ࠩ⁙"))[0]) <= bstack1l111ll1ll1_opy_:
          logger.warning(bstack1lll1ll1l11_opy_ (u"ࠨࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡽࡩ࡭࡮ࠣࡶࡺࡴࠠࡰࡰ࡯ࡽࠥࡵ࡮ࠡࡅ࡫ࡶࡴࡳࡥࠡࡤࡵࡳࡼࡹࡥࡳࠢࡹࡩࡷࡹࡩࡰࡰࠣ࡫ࡷ࡫ࡡࡵࡧࡵࠤࡹ࡮ࡡ࡯ࠢࡾࡱ࡮ࡴ࡟ࡢ࠳࠴ࡽࡤࡹࡵࡱࡲࡲࡶࡹ࡫ࡤࡠࡥ࡫ࡶࡴࡳࡥࡠࡸࡨࡶࡸ࡯࡯࡯ࡿ࠱ࠫ⁚"))
          return False
        if not options:
          bstack1l111l1ll1l_opy_ = caps.get(bstack1l1lll1_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ⁛")) or bstack1llll1ll1lll_opy_.get(bstack1l1lll1_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨ⁜"), {})
          if bstack1l1lll1_opy_ (u"ࠫ࠲࠳ࡨࡦࡣࡧࡰࡪࡹࡳࠨ⁝") in bstack1l111l1ll1l_opy_.get(bstack1l1lll1_opy_ (u"ࠬࡧࡲࡨࡵࠪ⁞"), []):
              logger.warning(bstack1l1lll1_opy_ (u"ࠨࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡻ࡮ࡲ࡬ࠡࡰࡲࡸࠥࡸࡵ࡯ࠢࡲࡲࠥࡲࡥࡨࡣࡦࡽࠥ࡮ࡥࡢࡦ࡯ࡩࡸࡹࠠ࡮ࡱࡧࡩ࠳ࠦࡓࡸ࡫ࡷࡧ࡭ࠦࡴࡰࠢࡱࡩࡼࠦࡨࡦࡣࡧࡰࡪࡹࡳࠡ࡯ࡲࡨࡪࠦ࡯ࡳࠢࡤࡺࡴ࡯ࡤࠡࡷࡶ࡭ࡳ࡭ࠠࡩࡧࡤࡨࡱ࡫ࡳࡴࠢࡰࡳࡩ࡫࠮ࠣ "))
              return False
        return True
    except Exception as error:
        logger.debug(bstack1l1lll1_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡶࡢ࡮࡬ࡨࡦࡺࡥࠡࡣ࠴࠵ࡾࠦࡳࡶࡲࡳࡳࡷࡺࠠ࠻ࠤ⁠") + str(error))
        return False
def set_capabilities(caps, config):
  try:
    bstack1l1l111l111_opy_ = config.get(bstack1l1lll1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨ⁡"), {})
    bstack1l1l111l111_opy_[bstack1l1lll1_opy_ (u"ࠩࡤࡹࡹ࡮ࡔࡰ࡭ࡨࡲࠬ⁢")] = os.getenv(bstack1l1lll1_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨ⁣"))
    bstack1111l1ll1l1_opy_ = json.loads(os.getenv(bstack1l1lll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡠࡃࡆࡇࡊ࡙ࡓࡊࡄࡌࡐࡎ࡚࡙ࡠࡅࡒࡒࡋࡏࡇࡖࡔࡄࡘࡎࡕࡎࡠ࡛ࡐࡐࠬ⁤"), bstack1l1lll1_opy_ (u"ࠬࢁࡽࠨ⁥"))).get(bstack1l1lll1_opy_ (u"࠭ࡳࡤࡣࡱࡲࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧ⁦"))
    if not config[bstack1l1lll1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡖࡲࡰࡦࡸࡧࡹࡓࡡࡱࠩ⁧")].get(bstack1l1lll1_opy_ (u"ࠣࡣࡳࡴࡤࡧࡵࡵࡱࡰࡥࡹ࡫ࠢ⁨")):
      if bstack1l1lll1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪ⁩") in caps:
        caps[bstack1l1lll1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫ⁪")][bstack1l1lll1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫ⁫")] = bstack1l1l111l111_opy_
        caps[bstack1l1lll1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭⁬")][bstack1l1lll1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭⁭")][bstack1l1lll1_opy_ (u"ࠧࡴࡥࡤࡲࡳ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨ⁮")] = bstack1111l1ll1l1_opy_
      else:
        caps[bstack1l1lll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧ⁯")] = bstack1l1l111l111_opy_
        caps[bstack1l1lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨ⁰")][bstack1l1lll1_opy_ (u"ࠪࡷࡨࡧ࡮࡯ࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫⁱ")] = bstack1111l1ll1l1_opy_
  except Exception as error:
    logger.debug(bstack1l1lll1_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡸࡪ࡬ࡰࡪࠦࡳࡦࡶࡷ࡭ࡳ࡭ࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵ࠱ࠤࡊࡸࡲࡰࡴ࠽ࠤࠧ⁲") +  str(error))
def bstack11lllll111_opy_(driver, bstack1llll1ll1l11_opy_):
  try:
    setattr(driver, bstack1l1lll1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡆ࠷࠱ࡺࡕ࡫ࡳࡺࡲࡤࡔࡥࡤࡲࠬ⁳"), True)
    session = driver.session_id
    if session:
      bstack1lllll11111l_opy_ = True
      current_url = driver.current_url
      try:
        url = urlparse(current_url)
      except Exception as e:
        bstack1lllll11111l_opy_ = False
      bstack1lllll11111l_opy_ = url.scheme in [bstack1l1lll1_opy_ (u"ࠨࡨࡵࡶࡳࠦ⁴"), bstack1l1lll1_opy_ (u"ࠢࡩࡶࡷࡴࡸࠨ⁵")]
      if bstack1lllll11111l_opy_:
        if bstack1llll1ll1l11_opy_:
          logger.info(bstack1l1lll1_opy_ (u"ࠣࡕࡨࡸࡺࡶࠠࡧࡱࡵࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡹ࡫ࡳࡵ࡫ࡱ࡫ࠥ࡮ࡡࡴࠢࡶࡸࡦࡸࡴࡦࡦ࠱ࠤࡆࡻࡴࡰ࡯ࡤࡸࡪࠦࡴࡦࡵࡷࠤࡨࡧࡳࡦࠢࡨࡼࡪࡩࡵࡵ࡫ࡲࡲࠥࡽࡩ࡭࡮ࠣࡦࡪ࡭ࡩ࡯ࠢࡰࡳࡲ࡫࡮ࡵࡣࡵ࡭ࡱࡿ࠮ࠣ⁶"))
      return bstack1llll1ll1l11_opy_
  except Exception as e:
    logger.error(bstack1l1lll1_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡵࡷࡥࡷࡺࡩ࡯ࡩࠣࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡴࡥࡤࡲࠥ࡬࡯ࡳࠢࡷ࡬࡮ࡹࠠࡵࡧࡶࡸࠥࡩࡡࡴࡧ࠽ࠤࠧ⁷") + str(e))
    return False
def bstack1111lll1_opy_(driver, name, path):
  try:
    bstack1l111l11111_opy_ = {
        bstack1l1lll1_opy_ (u"ࠪࡸ࡭࡚ࡥࡴࡶࡕࡹࡳ࡛ࡵࡪࡦࠪ⁸"): threading.current_thread().current_test_uuid,
        bstack1l1lll1_opy_ (u"ࠫࡹ࡮ࡂࡶ࡫࡯ࡨ࡚ࡻࡩࡥࠩ⁹"): os.environ.get(bstack1l1lll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪ⁺"), bstack1l1lll1_opy_ (u"࠭ࠧ⁻")),
        bstack1l1lll1_opy_ (u"ࠧࡵࡪࡍࡻࡹ࡚࡯࡬ࡧࡱࠫ⁼"): os.environ.get(bstack1l1lll1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡌ࡚ࡘࠬ⁽"), bstack1l1lll1_opy_ (u"ࠩࠪ⁾"))
    }
    bstack1ll1l11l111_opy_ = bstack11l1l1111l_opy_.bstack1ll1ll1111l_opy_(EVENTS.bstack1l11l1111_opy_.value)
    logger.debug(bstack1l1lll1_opy_ (u"ࠪࡔࡪࡸࡦࡰࡴࡰ࡭ࡳ࡭ࠠࡴࡥࡤࡲࠥࡨࡥࡧࡱࡵࡩࠥࡹࡡࡷ࡫ࡱ࡫ࠥࡸࡥࡴࡷ࡯ࡸࡸ࠭ⁿ"))
    try:
      if (bstack1l1l1l1l_opy_(threading.current_thread(), bstack1l1lll1_opy_ (u"ࠫ࡮ࡹࡁࡱࡲࡄ࠵࠶ࡿࡔࡦࡵࡷࠫ₀"), None) and bstack1l1l1l1l_opy_(threading.current_thread(), bstack1l1lll1_opy_ (u"ࠬࡧࡰࡱࡃ࠴࠵ࡾࡖ࡬ࡢࡶࡩࡳࡷࡳࠧ₁"), None)):
        scripts = {bstack1l1lll1_opy_ (u"࠭ࡳࡤࡣࡱࠫ₂"): bstack1l11111ll_opy_.perform_scan}
        bstack1lllll11l1ll_opy_ = json.loads(scripts[bstack1l1lll1_opy_ (u"ࠢࡴࡥࡤࡲࠧ₃")].replace(bstack1l1lll1_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࠦ₄"), bstack1l1lll1_opy_ (u"ࠤࠥ₅")))
        bstack1lllll11l1ll_opy_[bstack1l1lll1_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭₆")][bstack1l1lll1_opy_ (u"ࠫࡲ࡫ࡴࡩࡱࡧࠫ₇")] = None
        scripts[bstack1l1lll1_opy_ (u"ࠧࡹࡣࡢࡰࠥ₈")] = bstack1l1lll1_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࠤ₉") + json.dumps(bstack1lllll11l1ll_opy_)
        bstack1l11111ll_opy_.bstack11l11l1ll_opy_(scripts)
        bstack1l11111ll_opy_.store()
        logger.debug(driver.execute_script(bstack1l11111ll_opy_.perform_scan))
      else:
        logger.debug(driver.execute_async_script(bstack1l11111ll_opy_.perform_scan, {bstack1l1lll1_opy_ (u"ࠢ࡮ࡧࡷ࡬ࡴࡪࠢ₊"): name}))
      bstack11l1l1111l_opy_.end(EVENTS.bstack1l11l1111_opy_.value, bstack1ll1l11l111_opy_ + bstack1l1lll1_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣ₋"), bstack1ll1l11l111_opy_ + bstack1l1lll1_opy_ (u"ࠤ࠽ࡩࡳࡪࠢ₌"), True, None)
    except Exception as error:
      bstack11l1l1111l_opy_.end(EVENTS.bstack1l11l1111_opy_.value, bstack1ll1l11l111_opy_ + bstack1l1lll1_opy_ (u"ࠥ࠾ࡸࡺࡡࡳࡶࠥ₍"), bstack1ll1l11l111_opy_ + bstack1l1lll1_opy_ (u"ࠦ࠿࡫࡮ࡥࠤ₎"), False, str(error))
    bstack1ll1l11l111_opy_ = bstack11l1l1111l_opy_.bstack11ll1ll1111_opy_(EVENTS.bstack1l111l1l1ll_opy_.value)
    bstack11l1l1111l_opy_.mark(bstack1ll1l11l111_opy_ + bstack1l1lll1_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧ₏"))
    try:
      if (bstack1l1l1l1l_opy_(threading.current_thread(), bstack1l1lll1_opy_ (u"࠭ࡩࡴࡃࡳࡴࡆ࠷࠱ࡺࡖࡨࡷࡹ࠭ₐ"), None) and bstack1l1l1l1l_opy_(threading.current_thread(), bstack1l1lll1_opy_ (u"ࠧࡢࡲࡳࡅ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩₑ"), None)):
        scripts = {bstack1l1lll1_opy_ (u"ࠨࡵࡦࡥࡳ࠭ₒ"): bstack1l11111ll_opy_.perform_scan}
        bstack1lllll11l1ll_opy_ = json.loads(scripts[bstack1l1lll1_opy_ (u"ࠤࡶࡧࡦࡴࠢₓ")].replace(bstack1l1lll1_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࠨₔ"), bstack1l1lll1_opy_ (u"ࠦࠧₕ")))
        bstack1lllll11l1ll_opy_[bstack1l1lll1_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨₖ")][bstack1l1lll1_opy_ (u"࠭࡭ࡦࡶ࡫ࡳࡩ࠭ₗ")] = None
        scripts[bstack1l1lll1_opy_ (u"ࠢࡴࡥࡤࡲࠧₘ")] = bstack1l1lll1_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࠦₙ") + json.dumps(bstack1lllll11l1ll_opy_)
        bstack1l11111ll_opy_.bstack11l11l1ll_opy_(scripts)
        bstack1l11111ll_opy_.store()
        logger.debug(driver.execute_script(bstack1l11111ll_opy_.perform_scan))
      else:
        logger.debug(driver.execute_async_script(bstack1l11111ll_opy_.bstack1lllll1l111l_opy_, bstack1l111l11111_opy_))
      bstack11l1l1111l_opy_.end(bstack1ll1l11l111_opy_, bstack1ll1l11l111_opy_ + bstack1l1lll1_opy_ (u"ࠤ࠽ࡷࡹࡧࡲࡵࠤₚ"), bstack1ll1l11l111_opy_ + bstack1l1lll1_opy_ (u"ࠥ࠾ࡪࡴࡤࠣₛ"),True, None)
    except Exception as error:
      bstack11l1l1111l_opy_.end(bstack1ll1l11l111_opy_, bstack1ll1l11l111_opy_ + bstack1l1lll1_opy_ (u"ࠦ࠿ࡹࡴࡢࡴࡷࠦₜ"), bstack1ll1l11l111_opy_ + bstack1l1lll1_opy_ (u"ࠧࡀࡥ࡯ࡦࠥ₝"),False, str(error))
    logger.info(bstack1l1lll1_opy_ (u"ࠨࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡴࡦࡵࡷ࡭ࡳ࡭ࠠࡧࡱࡵࠤࡹ࡮ࡩࡴࠢࡷࡩࡸࡺࠠࡤࡣࡶࡩࠥ࡮ࡡࡴࠢࡨࡲࡩ࡫ࡤ࠯ࠤ₞"))
  except Exception as bstack1l111ll11ll_opy_:
    logger.error(bstack1l1lll1_opy_ (u"ࠢࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡳࡧࡶࡹࡱࡺࡳࠡࡥࡲࡹࡱࡪࠠ࡯ࡱࡷࠤࡧ࡫ࠠࡱࡴࡲࡧࡪࡹࡳࡦࡦࠣࡪࡴࡸࠠࡵࡪࡨࠤࡹ࡫ࡳࡵࠢࡦࡥࡸ࡫࠺ࠡࠤ₟") + str(path) + bstack1l1lll1_opy_ (u"ࠣࠢࡈࡶࡷࡵࡲࠡ࠼ࠥ₠") + str(bstack1l111ll11ll_opy_))
def bstack1lllll1111l1_opy_(driver):
    caps = driver.capabilities
    if caps.get(bstack1l1lll1_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰࡒࡦࡳࡥࠣ₡")) and str(caps.get(bstack1l1lll1_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱࡓࡧ࡭ࡦࠤ₢"))).lower() == bstack1l1lll1_opy_ (u"ࠦࡦࡴࡤࡳࡱ࡬ࡨࠧ₣"):
        bstack1l111l1l111_opy_ = caps.get(bstack1l1lll1_opy_ (u"ࠧࡧࡰࡱ࡫ࡸࡱ࠿ࡶ࡬ࡢࡶࡩࡳࡷࡳࡖࡦࡴࡶ࡭ࡴࡴࠢ₤")) or caps.get(bstack1l1lll1_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠣ₥"))
        if bstack1l111l1l111_opy_ and int(str(bstack1l111l1l111_opy_)) < bstack11l11ll1l1l_opy_:
            return False
    return True
def bstack11ll1l1l1l_opy_(config):
  if bstack1l1lll1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ₦") in config:
        return config[bstack1l1lll1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ₧")]
  for platform in config.get(bstack1l1lll1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ₨"), []):
      if bstack1l1lll1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ₩") in platform:
          return platform[bstack1l1lll1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ₪")]
  return None
def bstack1ll1l1ll1_opy_(bstack1llll1l111_opy_):
  try:
    browser_name = bstack1llll1l111_opy_[bstack1l1lll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡥ࡮ࡢ࡯ࡨࠫ₫")]
    browser_version = bstack1llll1l111_opy_[bstack1l1lll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨ€")]
    chrome_options = bstack1llll1l111_opy_[bstack1l1lll1_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫࡟ࡰࡲࡷ࡭ࡴࡴࡳࠨ₭")]
    try:
        bstack1llll1ll11ll_opy_ = int(browser_version.split(bstack1l1lll1_opy_ (u"ࠨ࠰ࠪ₮"))[0])
    except ValueError as e:
        logger.error(bstack1l1lll1_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡹ࡫࡭ࡱ࡫ࠠࡤࡱࡱࡺࡪࡸࡴࡪࡰࡪࠤࡧࡸ࡯ࡸࡵࡨࡶࠥࡼࡥࡳࡵ࡬ࡳࡳࠨ₯") + str(e))
        return False
    if not (browser_name and browser_name.lower() == bstack1l1lll1_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧࠪ₰")):
        logger.warning(bstack1l1lll1_opy_ (u"ࠦࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡹ࡬ࡰࡱࠦࡲࡶࡰࠣࡳࡳࡲࡹࠡࡱࡱࠤࡈ࡮ࡲࡰ࡯ࡨࠤࡧࡸ࡯ࡸࡵࡨࡶࡸ࠴ࠢ₱"))
        return False
    if bstack1llll1ll11ll_opy_ < bstack1lllll111ll1_opy_.bstack1l111llll11_opy_:
        logger.warning(bstack1lll1ll1l11_opy_ (u"ࠬࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡵࡩࡶࡻࡩࡳࡧࡶࠤࡈ࡮ࡲࡰ࡯ࡨࠤࡻ࡫ࡲࡴ࡫ࡲࡲࠥࢁࡃࡐࡐࡖࡘࡆࡔࡔࡔ࠰ࡐࡍࡓࡏࡍࡖࡏࡢࡒࡔࡔ࡟ࡃࡕࡗࡅࡈࡑ࡟ࡊࡐࡉࡖࡆࡥࡁ࠲࠳࡜ࡣࡘ࡛ࡐࡑࡑࡕࡘࡊࡊ࡟ࡄࡊࡕࡓࡒࡋ࡟ࡗࡇࡕࡗࡎࡕࡎࡾࠢࡲࡶࠥ࡮ࡩࡨࡪࡨࡶ࠳࠭₲"))
        return False
    if chrome_options and any(bstack1l1lll1_opy_ (u"࠭࠭࠮ࡪࡨࡥࡩࡲࡥࡴࡵࠪ₳") in value for value in chrome_options.values() if isinstance(value, str)):
        logger.warning(bstack1l1lll1_opy_ (u"ࠢࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡼ࡯࡬࡭ࠢࡱࡳࡹࠦࡲࡶࡰࠣࡳࡳࠦ࡬ࡦࡩࡤࡧࡾࠦࡨࡦࡣࡧࡰࡪࡹࡳࠡ࡯ࡲࡨࡪ࠴ࠠࡔࡹ࡬ࡸࡨ࡮ࠠࡵࡱࠣࡲࡪࡽࠠࡩࡧࡤࡨࡱ࡫ࡳࡴࠢࡰࡳࡩ࡫ࠠࡰࡴࠣࡥࡻࡵࡩࡥࠢࡸࡷ࡮ࡴࡧࠡࡪࡨࡥࡩࡲࡥࡴࡵࠣࡱࡴࡪࡥ࠯ࠤ₴"))
        return False
    return True
  except Exception as e:
    logger.error(bstack1l1lll1_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡪࡰࠣࡧ࡭࡫ࡣ࡬࡫ࡱ࡫ࠥࡶ࡬ࡢࡶࡩࡳࡷࡳࠠࡴࡷࡳࡴࡴࡸࡴࠡࡨࡲࡶࠥࡲ࡯ࡤࡣ࡯ࠤࡈ࡮ࡲࡰ࡯ࡨ࠾ࠥࠨ₵") + str(e))
    return False
def bstack111lllll1l_opy_(bstack1111l1llll_opy_, config):
    try:
      bstack1l111lll1ll_opy_ = bstack1l1lll1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ₶") in config and config[bstack1l1lll1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ₷")] == True
      bstack1llll1ll111l_opy_ = bstack1l1lll1_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨ₸") in config and str(config[bstack1l1lll1_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩ₹")]).lower() != bstack1l1lll1_opy_ (u"࠭ࡦࡢ࡮ࡶࡩࠬ₺")
      if not (bstack1l111lll1ll_opy_ and (not bstack1l1l1l1l1_opy_(config) or bstack1llll1ll111l_opy_)):
        return bstack1111l1llll_opy_
      bstack1lllll11l11l_opy_ = bstack1l11111ll_opy_.bstack1lllll11llll_opy_
      if bstack1lllll11l11l_opy_ is None:
        logger.debug(bstack1l1lll1_opy_ (u"ࠢࡈࡱࡲ࡫ࡱ࡫ࠠࡤࡪࡵࡳࡲ࡫ࠠࡰࡲࡷ࡭ࡴࡴࡳࠡࡣࡵࡩࠥࡔ࡯࡯ࡧࠥ₻"))
        return bstack1111l1llll_opy_
      bstack1llll1lllll1_opy_ = int(str(bstack1111ll1l111_opy_()).split(bstack1l1lll1_opy_ (u"ࠨ࠰ࠪ₼"))[0])
      logger.debug(bstack1l1lll1_opy_ (u"ࠤࡖࡩࡱ࡫࡮ࡪࡷࡰࠤࡻ࡫ࡲࡴ࡫ࡲࡲࠥࡪࡥࡵࡧࡦࡸࡪࡪ࠺ࠡࠤ₽") + str(bstack1llll1lllll1_opy_) + bstack1l1lll1_opy_ (u"ࠥࠦ₾"))
      if bstack1llll1lllll1_opy_ == 3 and isinstance(bstack1111l1llll_opy_, dict) and bstack1l1lll1_opy_ (u"ࠫࡩ࡫ࡳࡪࡴࡨࡨࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠫ₿") in bstack1111l1llll_opy_ and bstack1lllll11l11l_opy_ is not None:
        if bstack1l1lll1_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ⃀") not in bstack1111l1llll_opy_[bstack1l1lll1_opy_ (u"࠭ࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠭⃁")]:
          bstack1111l1llll_opy_[bstack1l1lll1_opy_ (u"ࠧࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠧ⃂")][bstack1l1lll1_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭⃃")] = {}
        if bstack1l1lll1_opy_ (u"ࠩࡤࡶ࡬ࡹࠧ⃄") in bstack1lllll11l11l_opy_:
          if bstack1l1lll1_opy_ (u"ࠪࡥࡷ࡭ࡳࠨ⃅") not in bstack1111l1llll_opy_[bstack1l1lll1_opy_ (u"ࠫࡩ࡫ࡳࡪࡴࡨࡨࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠫ⃆")][bstack1l1lll1_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ⃇")]:
            bstack1111l1llll_opy_[bstack1l1lll1_opy_ (u"࠭ࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠭⃈")][bstack1l1lll1_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬ⃉")][bstack1l1lll1_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭⃊")] = []
          for arg in bstack1lllll11l11l_opy_[bstack1l1lll1_opy_ (u"ࠩࡤࡶ࡬ࡹࠧ⃋")]:
            if arg not in bstack1111l1llll_opy_[bstack1l1lll1_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪ⃌")][bstack1l1lll1_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩ⃍")][bstack1l1lll1_opy_ (u"ࠬࡧࡲࡨࡵࠪ⃎")]:
              bstack1111l1llll_opy_[bstack1l1lll1_opy_ (u"࠭ࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠭⃏")][bstack1l1lll1_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬ⃐")][bstack1l1lll1_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭⃑")].append(arg)
        if bstack1l1lll1_opy_ (u"ࠩࡨࡼࡹ࡫࡮ࡴ࡫ࡲࡲࡸ⃒࠭") in bstack1lllll11l11l_opy_:
          if bstack1l1lll1_opy_ (u"ࠪࡩࡽࡺࡥ࡯ࡵ࡬ࡳࡳࡹ⃓ࠧ") not in bstack1111l1llll_opy_[bstack1l1lll1_opy_ (u"ࠫࡩ࡫ࡳࡪࡴࡨࡨࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠫ⃔")][bstack1l1lll1_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ⃕")]:
            bstack1111l1llll_opy_[bstack1l1lll1_opy_ (u"࠭ࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠭⃖")][bstack1l1lll1_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬ⃗")][bstack1l1lll1_opy_ (u"ࠨࡧࡻࡸࡪࡴࡳࡪࡱࡱࡷ⃘ࠬ")] = []
          for ext in bstack1lllll11l11l_opy_[bstack1l1lll1_opy_ (u"ࠩࡨࡼࡹ࡫࡮ࡴ࡫ࡲࡲࡸ⃙࠭")]:
            if ext not in bstack1111l1llll_opy_[bstack1l1lll1_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵ⃚ࠪ")][bstack1l1lll1_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩ⃛")][bstack1l1lll1_opy_ (u"ࠬ࡫ࡸࡵࡧࡱࡷ࡮ࡵ࡮ࡴࠩ⃜")]:
              bstack1111l1llll_opy_[bstack1l1lll1_opy_ (u"࠭ࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠭⃝")][bstack1l1lll1_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬ⃞")][bstack1l1lll1_opy_ (u"ࠨࡧࡻࡸࡪࡴࡳࡪࡱࡱࡷࠬ⃟")].append(ext)
        if bstack1l1lll1_opy_ (u"ࠩࡳࡶࡪ࡬ࡳࠨ⃠") in bstack1lllll11l11l_opy_:
          if bstack1l1lll1_opy_ (u"ࠪࡴࡷ࡫ࡦࡴࠩ⃡") not in bstack1111l1llll_opy_[bstack1l1lll1_opy_ (u"ࠫࡩ࡫ࡳࡪࡴࡨࡨࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠫ⃢")][bstack1l1lll1_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ⃣")]:
            bstack1111l1llll_opy_[bstack1l1lll1_opy_ (u"࠭ࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠭⃤")][bstack1l1lll1_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷ⃥ࠬ")][bstack1l1lll1_opy_ (u"ࠨࡲࡵࡩ࡫ࡹ⃦ࠧ")] = {}
          bstack1111l1ll1ll_opy_(bstack1111l1llll_opy_[bstack1l1lll1_opy_ (u"ࠩࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩ⃧")][bstack1l1lll1_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨ⃨")][bstack1l1lll1_opy_ (u"ࠫࡵࡸࡥࡧࡵࠪ⃩")],
                    bstack1lllll11l11l_opy_[bstack1l1lll1_opy_ (u"ࠬࡶࡲࡦࡨࡶ⃪ࠫ")])
        os.environ[bstack1l1lll1_opy_ (u"࠭ࡉࡔࡡࡑࡓࡓࡥࡂࡔࡖࡄࡇࡐࡥࡉࡏࡈࡕࡅࡤࡇ࠱࠲࡛ࡢࡗࡊ࡙ࡓࡊࡑࡑ⃫ࠫ")] = bstack1l1lll1_opy_ (u"ࠧࡵࡴࡸࡩ⃬ࠬ")
        return bstack1111l1llll_opy_
      else:
        chrome_options = None
        if isinstance(bstack1111l1llll_opy_, ChromeOptions):
          chrome_options = bstack1111l1llll_opy_
        elif isinstance(bstack1111l1llll_opy_, dict):
          for value in bstack1111l1llll_opy_.values():
            if isinstance(value, ChromeOptions):
              chrome_options = value
              break
        if chrome_options is None:
          chrome_options = ChromeOptions()
          if isinstance(bstack1111l1llll_opy_, dict):
            bstack1111l1llll_opy_[bstack1l1lll1_opy_ (u"ࠨࡱࡳࡸ࡮ࡵ࡮ࡴ⃭ࠩ")] = chrome_options
          else:
            bstack1111l1llll_opy_ = chrome_options
        if bstack1lllll11l11l_opy_ is not None:
          if bstack1l1lll1_opy_ (u"ࠩࡤࡶ࡬ࡹ⃮ࠧ") in bstack1lllll11l11l_opy_:
                bstack1llll1lll1ll_opy_ = chrome_options.arguments or []
                new_args = bstack1lllll11l11l_opy_[bstack1l1lll1_opy_ (u"ࠪࡥࡷ࡭ࡳࠨ⃯")]
                for arg in new_args:
                    if arg not in bstack1llll1lll1ll_opy_:
                        chrome_options.add_argument(arg)
          if bstack1l1lll1_opy_ (u"ࠫࡪࡾࡴࡦࡰࡶ࡭ࡴࡴࡳࠨ⃰") in bstack1lllll11l11l_opy_:
                existing_extensions = chrome_options.experimental_options.get(bstack1l1lll1_opy_ (u"ࠬ࡫ࡸࡵࡧࡱࡷ࡮ࡵ࡮ࡴࠩ⃱"), [])
                bstack1lllll1111ll_opy_ = bstack1lllll11l11l_opy_[bstack1l1lll1_opy_ (u"࠭ࡥࡹࡶࡨࡲࡸ࡯࡯࡯ࡵࠪ⃲")]
                for extension in bstack1lllll1111ll_opy_:
                    if extension not in existing_extensions:
                        chrome_options.add_encoded_extension(extension)
          if bstack1l1lll1_opy_ (u"ࠧࡱࡴࡨࡪࡸ࠭⃳") in bstack1lllll11l11l_opy_:
                bstack1llll1lll11l_opy_ = chrome_options.experimental_options.get(bstack1l1lll1_opy_ (u"ࠨࡲࡵࡩ࡫ࡹࠧ⃴"), {})
                bstack1lllll111111_opy_ = bstack1lllll11l11l_opy_[bstack1l1lll1_opy_ (u"ࠩࡳࡶࡪ࡬ࡳࠨ⃵")]
                bstack1111l1ll1ll_opy_(bstack1llll1lll11l_opy_, bstack1lllll111111_opy_)
                chrome_options.add_experimental_option(bstack1l1lll1_opy_ (u"ࠪࡴࡷ࡫ࡦࡴࠩ⃶"), bstack1llll1lll11l_opy_)
        os.environ[bstack1l1lll1_opy_ (u"ࠫࡎ࡙࡟ࡏࡑࡑࡣࡇ࡙ࡔࡂࡅࡎࡣࡎࡔࡆࡓࡃࡢࡅ࠶࠷࡙ࡠࡕࡈࡗࡘࡏࡏࡏࠩ⃷")] = bstack1l1lll1_opy_ (u"ࠬࡺࡲࡶࡧࠪ⃸")
        return bstack1111l1llll_opy_
    except Exception as e:
      logger.error(bstack1l1lll1_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡽࡨࡪ࡮ࡨࠤࡦࡪࡤࡪࡰࡪࠤࡳࡵ࡮࠮ࡄࡖࠤ࡮ࡴࡦࡳࡣࠣࡥ࠶࠷ࡹࠡࡥ࡫ࡶࡴࡳࡥࠡࡱࡳࡸ࡮ࡵ࡮ࡴ࠼ࠣࠦ⃹") + str(e))
      return bstack1111l1llll_opy_