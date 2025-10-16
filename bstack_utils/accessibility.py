# coding: UTF-8
import sys
bstack11llll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1l1l1l1_opy_ = 7
def bstack1ll11_opy_ (bstack11l11ll_opy_):
    global bstack11l1lll_opy_
    bstack1l1l111_opy_ = ord (bstack11l11ll_opy_ [-1])
    bstack11_opy_ = bstack11l11ll_opy_ [:-1]
    bstack1l1llll_opy_ = bstack1l1l111_opy_ % len (bstack11_opy_)
    bstack11111_opy_ = bstack11_opy_ [:bstack1l1llll_opy_] + bstack11_opy_ [bstack1l1llll_opy_:]
    if bstack11llll1_opy_:
        bstack111_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    else:
        bstack111_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    return eval (bstack111_opy_)
import os
import json
import requests
import logging
import threading
import bstack_utils.constants as bstack1lllll111ll1_opy_
from urllib.parse import urlparse
from bstack_utils.constants import bstack11l1l11l111_opy_ as bstack1lllll11111l_opy_, EVENTS
from bstack_utils.bstack11111lll11_opy_ import bstack11111lll11_opy_
from bstack_utils.helper import bstack1lll1111_opy_, bstack1ll111ll_opy_, bstack111lll111l_opy_, bstack1111lll1ll1_opy_, \
  bstack1111llll1l1_opy_, bstack1l11l1l11l_opy_, get_host_info, bstack1111ll111ll_opy_, bstack11ll1llll_opy_, error_handler, bstack1111l1l1lll_opy_, bstack111l11ll1l1_opy_, bstack1ll1ll11_opy_
from browserstack_sdk._version import __version__
from bstack_utils.bstack1l1l1l1111_opy_ import get_logger
from bstack_utils.bstack11l111l1l_opy_ import bstack1llll1lllll_opy_
from selenium.webdriver.chrome.options import Options as ChromeOptions
from browserstack_sdk.sdk_cli.cli import cli
from bstack_utils.constants import *
logger = get_logger(__name__)
bstack11l111l1l_opy_ = bstack1llll1lllll_opy_()
@error_handler(class_method=False)
def _1lllll11l111_opy_(driver, bstack111lll1l_opy_):
  response = {}
  try:
    caps = driver.capabilities
    response = {
        bstack1ll11_opy_ (u"ࠧࡰࡵࡢࡲࡦࡳࡥࠨῆ"): caps.get(bstack1ll11_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡑࡥࡲ࡫ࠧῇ"), None),
        bstack1ll11_opy_ (u"ࠩࡲࡷࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭Ὲ"): bstack111lll1l_opy_.get(bstack1ll11_opy_ (u"ࠪࡳࡸ࡜ࡥࡳࡵ࡬ࡳࡳ࠭Έ"), None),
        bstack1ll11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡤࡴࡡ࡮ࡧࠪῊ"): caps.get(bstack1ll11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪΉ"), None),
        bstack1ll11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨῌ"): caps.get(bstack1ll11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨ῍"), None)
    }
  except Exception as error:
    logger.debug(bstack1ll11_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡧࡧࡷࡧ࡭࡯࡮ࡨࠢࡳࡰࡦࡺࡦࡰࡴࡰࠤࡩ࡫ࡴࡢ࡫࡯ࡷࠥࡽࡩࡵࡪࠣࡩࡷࡸ࡯ࡳࠢ࠽ࠤࠬ῎") + str(error))
  return response
def on():
    if os.environ.get(bstack1ll11_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧ῏"), None) is None or os.environ[bstack1ll11_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨῐ")] == bstack1ll11_opy_ (u"ࠦࡳࡻ࡬࡭ࠤῑ"):
        return False
    return True
def bstack1ll1llll11_opy_(config):
  return config.get(bstack1ll11_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬῒ"), False) or any([p.get(bstack1ll11_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ΐ"), False) == True for p in config.get(bstack1ll11_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ῔"), [])])
def bstack1111l1l1ll_opy_(config, bstack111l111lll_opy_):
  try:
    bstack1lllll11ll11_opy_ = config.get(bstack1ll11_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ῕"), False)
    if int(bstack111l111lll_opy_) < len(config.get(bstack1ll11_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬῖ"), [])) and config[bstack1ll11_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ῗ")][bstack111l111lll_opy_]:
      bstack1lllll111111_opy_ = config[bstack1ll11_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧῘ")][bstack111l111lll_opy_].get(bstack1ll11_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬῙ"), None)
    else:
      bstack1lllll111111_opy_ = config.get(bstack1ll11_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭Ὶ"), None)
    if bstack1lllll111111_opy_ != None:
      bstack1lllll11ll11_opy_ = bstack1lllll111111_opy_
    bstack1lllll111l1l_opy_ = os.getenv(bstack1ll11_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠬΊ")) is not None and len(os.getenv(bstack1ll11_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭῜"))) > 0 and os.getenv(bstack1ll11_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧ῝")) != bstack1ll11_opy_ (u"ࠪࡲࡺࡲ࡬ࠨ῞")
    return bstack1lllll11ll11_opy_ and bstack1lllll111l1l_opy_
  except Exception as error:
    logger.debug(bstack1ll11_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡺࡪࡸࡩࡧࡻ࡬ࡲ࡬ࠦࡴࡩࡧࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡷࡪࡹࡳࡪࡱࡱࠤࡼ࡯ࡴࡩࠢࡨࡶࡷࡵࡲࠡ࠼ࠣࠫ῟") + str(error))
  return False
def bstack1llllll1l1_opy_(test_tags):
  bstack1l111l1111l_opy_ = os.getenv(bstack1ll11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡡࡄࡇࡈࡋࡓࡔࡋࡅࡍࡑࡏࡔ࡚ࡡࡆࡓࡓࡌࡉࡈࡗࡕࡅ࡙ࡏࡏࡏࡡ࡜ࡑࡑ࠭ῠ"))
  if bstack1l111l1111l_opy_ is None:
    return True
  bstack1l111l1111l_opy_ = json.loads(bstack1l111l1111l_opy_)
  try:
    include_tags = bstack1l111l1111l_opy_[bstack1ll11_opy_ (u"࠭ࡩ࡯ࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫῡ")] if bstack1ll11_opy_ (u"ࠧࡪࡰࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩࠬῢ") in bstack1l111l1111l_opy_ and isinstance(bstack1l111l1111l_opy_[bstack1ll11_opy_ (u"ࠨ࡫ࡱࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ࠭ΰ")], list) else []
    exclude_tags = bstack1l111l1111l_opy_[bstack1ll11_opy_ (u"ࠩࡨࡼࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧῤ")] if bstack1ll11_opy_ (u"ࠪࡩࡽࡩ࡬ࡶࡦࡨࡘࡦ࡭ࡳࡊࡰࡗࡩࡸࡺࡩ࡯ࡩࡖࡧࡴࡶࡥࠨῥ") in bstack1l111l1111l_opy_ and isinstance(bstack1l111l1111l_opy_[bstack1ll11_opy_ (u"ࠫࡪࡾࡣ࡭ࡷࡧࡩ࡙ࡧࡧࡴࡋࡱࡘࡪࡹࡴࡪࡰࡪࡗࡨࡵࡰࡦࠩῦ")], list) else []
    excluded = any(tag in exclude_tags for tag in test_tags)
    included = len(include_tags) == 0 or any(tag in include_tags for tag in test_tags)
    return not excluded and included
  except Exception as error:
    logger.debug(bstack1ll11_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡺࡦࡲࡩࡥࡣࡷ࡭ࡳ࡭ࠠࡵࡧࡶࡸࠥࡩࡡࡴࡧࠣࡪࡴࡸࠠࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡣࡧࡩࡳࡷ࡫ࠠࡴࡥࡤࡲࡳ࡯࡮ࡨ࠰ࠣࡉࡷࡸ࡯ࡳࠢ࠽ࠤࠧῧ") + str(error))
  return False
def bstack1llll1lll111_opy_(config, frameworkName, bstack1lllll11l11l_opy_, bstack1llll1ll1l11_opy_):
  bstack1llll1lllll1_opy_ = bstack1111lll1ll1_opy_(config)
  bstack1llll1llll11_opy_ = bstack1111llll1l1_opy_(config)
  if bstack1llll1lllll1_opy_ is None or bstack1llll1llll11_opy_ is None:
    logger.error(bstack1ll11_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡺ࡬࡮ࡲࡥࠡࡥࡵࡩࡦࡺࡩ࡯ࡩࠣࡸࡪࡹࡴࠡࡴࡸࡲࠥ࡬࡯ࡳࠢࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲ࠿ࠦࡍࡪࡵࡶ࡭ࡳ࡭ࠠࡢࡷࡷ࡬ࡪࡴࡴࡪࡥࡤࡸ࡮ࡵ࡮ࠡࡶࡲ࡯ࡪࡴࠧῨ"))
    return [None, None]
  try:
    settings = json.loads(os.getenv(bstack1ll11_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡣࡆࡉࡃࡆࡕࡖࡍࡇࡏࡌࡊࡖ࡜ࡣࡈࡕࡎࡇࡋࡊ࡙ࡗࡇࡔࡊࡑࡑࡣ࡞ࡓࡌࠨῩ"), bstack1ll11_opy_ (u"ࠨࡽࢀࠫῪ")))
    data = {
        bstack1ll11_opy_ (u"ࠩࡳࡶࡴࡰࡥࡤࡶࡑࡥࡲ࡫ࠧΎ"): config[bstack1ll11_opy_ (u"ࠪࡴࡷࡵࡪࡦࡥࡷࡒࡦࡳࡥࠨῬ")],
        bstack1ll11_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧ῭"): config.get(bstack1ll11_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ΅"), os.path.basename(os.getcwd())),
        bstack1ll11_opy_ (u"࠭ࡳࡵࡣࡵࡸ࡙࡯࡭ࡦࠩ`"): bstack1lll1111_opy_(),
        bstack1ll11_opy_ (u"ࠧࡥࡧࡶࡧࡷ࡯ࡰࡵ࡫ࡲࡲࠬ῰"): config.get(bstack1ll11_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡄࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࠫ῱"), bstack1ll11_opy_ (u"ࠩࠪῲ")),
        bstack1ll11_opy_ (u"ࠪࡷࡴࡻࡲࡤࡧࠪῳ"): {
            bstack1ll11_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࡎࡢ࡯ࡨࠫῴ"): frameworkName,
            bstack1ll11_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡗࡧࡵࡷ࡮ࡵ࡮ࠨ῵"): bstack1lllll11l11l_opy_,
            bstack1ll11_opy_ (u"࠭ࡳࡥ࡭࡙ࡩࡷࡹࡩࡰࡰࠪῶ"): __version__,
            bstack1ll11_opy_ (u"ࠧ࡭ࡣࡱ࡫ࡺࡧࡧࡦࠩῷ"): bstack1ll11_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨῸ"),
            bstack1ll11_opy_ (u"ࠩࡷࡩࡸࡺࡆࡳࡣࡰࡩࡼࡵࡲ࡬ࠩΌ"): bstack1ll11_opy_ (u"ࠪࡷࡪࡲࡥ࡯࡫ࡸࡱࠬῺ"),
            bstack1ll11_opy_ (u"ࠫࡹ࡫ࡳࡵࡈࡵࡥࡲ࡫ࡷࡰࡴ࡮࡚ࡪࡸࡳࡪࡱࡱࠫΏ"): bstack1llll1ll1l11_opy_
        },
        bstack1ll11_opy_ (u"ࠬࡹࡥࡵࡶ࡬ࡲ࡬ࡹࠧῼ"): settings,
        bstack1ll11_opy_ (u"࠭ࡶࡦࡴࡶ࡭ࡴࡴࡃࡰࡰࡷࡶࡴࡲࠧ´"): bstack1111ll111ll_opy_(),
        bstack1ll11_opy_ (u"ࠧࡤ࡫ࡌࡲ࡫ࡵࠧ῾"): bstack1l11l1l11l_opy_(),
        bstack1ll11_opy_ (u"ࠨࡪࡲࡷࡹࡏ࡮ࡧࡱࠪ῿"): get_host_info(),
        bstack1ll11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫ "): bstack111lll111l_opy_(config)
    }
    headers = {
        bstack1ll11_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱࡙ࡿࡰࡦࠩ "): bstack1ll11_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧ "),
    }
    config = {
        bstack1ll11_opy_ (u"ࠬࡧࡵࡵࡪࠪ "): (bstack1llll1lllll1_opy_, bstack1llll1llll11_opy_),
        bstack1ll11_opy_ (u"࠭ࡨࡦࡣࡧࡩࡷࡹࠧ "): headers
    }
    response = bstack11ll1llll_opy_(bstack1ll11_opy_ (u"ࠧࡑࡑࡖࡘࠬ "), bstack1lllll11111l_opy_ + bstack1ll11_opy_ (u"ࠨ࠱ࡹ࠶࠴ࡺࡥࡴࡶࡢࡶࡺࡴࡳࠨ "), data, config)
    bstack1lllll1111l1_opy_ = response.json()
    if bstack1lllll1111l1_opy_[bstack1ll11_opy_ (u"ࠩࡶࡹࡨࡩࡥࡴࡵࠪ ")]:
      parsed = json.loads(os.getenv(bstack1ll11_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚࡟ࡂࡅࡆࡉࡘ࡙ࡉࡃࡋࡏࡍ࡙࡟࡟ࡄࡑࡑࡊࡎࡍࡕࡓࡃࡗࡍࡔࡔ࡟࡚ࡏࡏࠫ "), bstack1ll11_opy_ (u"ࠫࢀࢃࠧ ")))
      parsed[bstack1ll11_opy_ (u"ࠬࡹࡣࡢࡰࡱࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ ")] = bstack1lllll1111l1_opy_[bstack1ll11_opy_ (u"࠭ࡤࡢࡶࡤࠫ​")][bstack1ll11_opy_ (u"ࠧࡴࡥࡤࡲࡳ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨ‌")]
      os.environ[bstack1ll11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡤࡇࡃࡄࡇࡖࡗࡎࡈࡉࡍࡋࡗ࡝ࡤࡉࡏࡏࡈࡌࡋ࡚ࡘࡁࡕࡋࡒࡒࡤ࡟ࡍࡍࠩ‍")] = json.dumps(parsed)
      bstack11111lll11_opy_.bstack1l11l1llll_opy_(bstack1lllll1111l1_opy_[bstack1ll11_opy_ (u"ࠩࡧࡥࡹࡧࠧ‎")][bstack1ll11_opy_ (u"ࠪࡷࡨࡸࡩࡱࡶࡶࠫ‏")])
      bstack11111lll11_opy_.bstack1lllll1l1l1l_opy_(bstack1lllll1111l1_opy_[bstack1ll11_opy_ (u"ࠫࡩࡧࡴࡢࠩ‐")][bstack1ll11_opy_ (u"ࠬࡩ࡯࡮࡯ࡤࡲࡩࡹࠧ‑")])
      bstack11111lll11_opy_.store()
      return bstack1lllll1111l1_opy_[bstack1ll11_opy_ (u"࠭ࡤࡢࡶࡤࠫ‒")][bstack1ll11_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡔࡰ࡭ࡨࡲࠬ–")], bstack1lllll1111l1_opy_[bstack1ll11_opy_ (u"ࠨࡦࡤࡸࡦ࠭—")][bstack1ll11_opy_ (u"ࠩ࡬ࡨࠬ―")]
    else:
      logger.error(bstack1ll11_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡷࡩ࡫࡯ࡩࠥࡸࡵ࡯ࡰ࡬ࡲ࡬ࠦࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯࠼ࠣࠫ‖") + bstack1lllll1111l1_opy_[bstack1ll11_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ‗")])
      if bstack1lllll1111l1_opy_[bstack1ll11_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭‘")] == bstack1ll11_opy_ (u"࠭ࡉ࡯ࡸࡤࡰ࡮ࡪࠠࡤࡱࡱࡪ࡮࡭ࡵࡳࡣࡷ࡭ࡴࡴࠠࡱࡣࡶࡷࡪࡪ࠮ࠨ’"):
        for bstack1llll1lll1ll_opy_ in bstack1lllll1111l1_opy_[bstack1ll11_opy_ (u"ࠧࡦࡴࡵࡳࡷࡹࠧ‚")]:
          logger.error(bstack1llll1lll1ll_opy_[bstack1ll11_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ‛")])
      return None, None
  except Exception as error:
    logger.error(bstack1ll11_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡽࡨࡪ࡮ࡨࠤࡨࡸࡥࡢࡶ࡬ࡲ࡬ࠦࡴࡦࡵࡷࠤࡷࡻ࡮ࠡࡨࡲࡶࠥࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮࠻ࠢࠥ“") +  str(error))
    return None, None
def bstack1lllll111lll_opy_():
  if os.getenv(bstack1ll11_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨ”")) is None:
    return {
        bstack1ll11_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫ„"): bstack1ll11_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫ‟"),
        bstack1ll11_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ†"): bstack1ll11_opy_ (u"ࠧࡃࡷ࡬ࡰࡩࠦࡣࡳࡧࡤࡸ࡮ࡵ࡮ࠡࡪࡤࡨࠥ࡬ࡡࡪ࡮ࡨࡨ࠳࠭‡")
    }
  data = {bstack1ll11_opy_ (u"ࠨࡧࡱࡨ࡙࡯࡭ࡦࠩ•"): bstack1lll1111_opy_()}
  headers = {
      bstack1ll11_opy_ (u"ࠩࡄࡹࡹ࡮࡯ࡳ࡫ࡽࡥࡹ࡯࡯࡯ࠩ‣"): bstack1ll11_opy_ (u"ࠪࡆࡪࡧࡲࡦࡴࠣࠫ․") + os.getenv(bstack1ll11_opy_ (u"ࠦࡇ࡙࡟ࡂ࠳࠴࡝ࡤࡐࡗࡕࠤ‥")),
      bstack1ll11_opy_ (u"ࠬࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡔࡺࡲࡨࠫ…"): bstack1ll11_opy_ (u"࠭ࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳࡯ࡹ࡯࡯ࠩ‧")
  }
  response = bstack11ll1llll_opy_(bstack1ll11_opy_ (u"ࠧࡑࡗࡗࠫ "), bstack1lllll11111l_opy_ + bstack1ll11_opy_ (u"ࠨ࠱ࡷࡩࡸࡺ࡟ࡳࡷࡱࡷ࠴ࡹࡴࡰࡲࠪ "), data, { bstack1ll11_opy_ (u"ࠩ࡫ࡩࡦࡪࡥࡳࡵࠪ‪"): headers })
  try:
    if response.status_code == 200:
      logger.info(bstack1ll11_opy_ (u"ࠥࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡔࡦࡵࡷࠤࡗࡻ࡮ࠡ࡯ࡤࡶࡰ࡫ࡤࠡࡣࡶࠤࡨࡵ࡭ࡱ࡮ࡨࡸࡪࡪࠠࡢࡶࠣࠦ‫") + bstack1ll111ll_opy_().isoformat() + bstack1ll11_opy_ (u"ࠫ࡟࠭‬"))
      return {bstack1ll11_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬ‭"): bstack1ll11_opy_ (u"࠭ࡳࡶࡥࡦࡩࡸࡹࠧ‮"), bstack1ll11_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ "): bstack1ll11_opy_ (u"ࠨࠩ‰")}
    else:
      response.raise_for_status()
  except requests.RequestException as error:
    logger.error(bstack1ll11_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡽࡨࡪ࡮ࡨࠤࡲࡧࡲ࡬࡫ࡱ࡫ࠥࡩ࡯࡮ࡲ࡯ࡩࡹ࡯࡯࡯ࠢࡲࡪࠥࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡖࡨࡷࡹࠦࡒࡶࡰ࠽ࠤࠧ‱") + str(error))
    return {
        bstack1ll11_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪ′"): bstack1ll11_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪ″"),
        bstack1ll11_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭‴"): str(error)
    }
def bstack1lllll11llll_opy_(bstack1llll1lll11l_opy_):
    return re.match(bstack1ll11_opy_ (u"ࡸࠧ࡟࡞ࡧ࠯࠭ࡢ࠮࡝ࡦ࠮࠭ࡄࠪࠧ‵"), bstack1llll1lll11l_opy_.strip()) is not None
def bstack1ll1llll1l_opy_(caps, options, desired_capabilities={}, config=None):
    try:
        if options:
          bstack1lllll11l1l1_opy_ = options.to_capabilities()
        elif desired_capabilities:
          bstack1lllll11l1l1_opy_ = desired_capabilities
        else:
          bstack1lllll11l1l1_opy_ = {}
        bstack1l111l111ll_opy_ = (bstack1lllll11l1l1_opy_.get(bstack1ll11_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡐࡤࡱࡪ࠭‶"), bstack1ll11_opy_ (u"ࠨࠩ‷")).lower() or caps.get(bstack1ll11_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡒࡦࡳࡥࠨ‸"), bstack1ll11_opy_ (u"ࠪࠫ‹")).lower())
        if bstack1l111l111ll_opy_ == bstack1ll11_opy_ (u"ࠫ࡮ࡵࡳࠨ›"):
            return True
        if bstack1l111l111ll_opy_ == bstack1ll11_opy_ (u"ࠬࡧ࡮ࡥࡴࡲ࡭ࡩ࠭※"):
            bstack1l111l1llll_opy_ = str(float(caps.get(bstack1ll11_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠨ‼")) or bstack1lllll11l1l1_opy_.get(bstack1ll11_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨ‽"), {}).get(bstack1ll11_opy_ (u"ࠨࡱࡶ࡚ࡪࡸࡳࡪࡱࡱࠫ‾"),bstack1ll11_opy_ (u"ࠩࠪ‿"))))
            if bstack1l111l111ll_opy_ == bstack1ll11_opy_ (u"ࠪࡥࡳࡪࡲࡰ࡫ࡧࠫ⁀") and int(bstack1l111l1llll_opy_.split(bstack1ll11_opy_ (u"ࠫ࠳࠭⁁"))[0]) < float(bstack11l1l111lll_opy_):
                logger.warning(str(bstack11l11lll11l_opy_))
                return False
            return True
        bstack1l111l111l1_opy_ = caps.get(bstack1ll11_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭⁂"), {}).get(bstack1ll11_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪࡔࡡ࡮ࡧࠪ⁃"), caps.get(bstack1ll11_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࠧ⁄"), bstack1ll11_opy_ (u"ࠨࠩ⁅")))
        if bstack1l111l111l1_opy_:
            logger.warning(bstack1ll11_opy_ (u"ࠤࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡷࡪ࡮࡯ࠤࡷࡻ࡮ࠡࡱࡱࡰࡾࠦ࡯࡯ࠢࡇࡩࡸࡱࡴࡰࡲࠣࡦࡷࡵࡷࡴࡧࡵࡷ࠳ࠨ⁆"))
            return False
        browser = caps.get(bstack1ll11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨ⁇"), bstack1ll11_opy_ (u"ࠫࠬ⁈")).lower() or bstack1lllll11l1l1_opy_.get(bstack1ll11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪ⁉"), bstack1ll11_opy_ (u"࠭ࠧ⁊")).lower()
        if browser != bstack1ll11_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࠧ⁋"):
            logger.warning(bstack1ll11_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡽࡩ࡭࡮ࠣࡶࡺࡴࠠࡰࡰ࡯ࡽࠥࡵ࡮ࠡࡅ࡫ࡶࡴࡳࡥࠡࡤࡵࡳࡼࡹࡥࡳࡵ࠱ࠦ⁌"))
            return False
        browser_version = caps.get(bstack1ll11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪ⁍")) or caps.get(bstack1ll11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬ⁎")) or bstack1lllll11l1l1_opy_.get(bstack1ll11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬ⁏")) or bstack1lllll11l1l1_opy_.get(bstack1ll11_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭⁐"), {}).get(bstack1ll11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧ⁑")) or bstack1lllll11l1l1_opy_.get(bstack1ll11_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨ⁒"), {}).get(bstack1ll11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡹࡩࡷࡹࡩࡰࡰࠪ⁓"))
        bstack1l111l11l11_opy_ = bstack1lllll111ll1_opy_.bstack1l111l1l1l1_opy_
        bstack1llll1llll1l_opy_ = False
        if config is not None:
          bstack1llll1llll1l_opy_ = bstack1ll11_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭⁔") in config and str(config[bstack1ll11_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧ⁕")]).lower() != bstack1ll11_opy_ (u"ࠫ࡫ࡧ࡬ࡴࡧࠪ⁖")
        if os.environ.get(bstack1ll11_opy_ (u"ࠬࡏࡓࡠࡐࡒࡒࡤࡈࡓࡕࡃࡆࡏࡤࡏࡎࡇࡔࡄࡣࡆ࠷࠱࡚ࡡࡖࡉࡘ࡙ࡉࡐࡐࠪ⁗"), bstack1ll11_opy_ (u"࠭ࠧ⁘")).lower() == bstack1ll11_opy_ (u"ࠧࡵࡴࡸࡩࠬ⁙") or bstack1llll1llll1l_opy_:
          bstack1l111l11l11_opy_ = bstack1lllll111ll1_opy_.bstack1l11l111111_opy_
        if browser_version and browser_version != bstack1ll11_opy_ (u"ࠨ࡮ࡤࡸࡪࡹࡴࠨ⁚") and int(browser_version.split(bstack1ll11_opy_ (u"ࠩ࠱ࠫ⁛"))[0]) <= bstack1l111l11l11_opy_:
          logger.warning(bstack1lll1llllll_opy_ (u"ࠪࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡸ࡫࡯ࡰࠥࡸࡵ࡯ࠢࡲࡲࡱࡿࠠࡰࡰࠣࡇ࡭ࡸ࡯࡮ࡧࠣࡦࡷࡵࡷࡴࡧࡵࠤࡻ࡫ࡲࡴ࡫ࡲࡲࠥ࡭ࡲࡦࡣࡷࡩࡷࠦࡴࡩࡣࡱࠤࢀࡳࡩ࡯ࡡࡤ࠵࠶ࡿ࡟ࡴࡷࡳࡴࡴࡸࡴࡦࡦࡢࡧ࡭ࡸ࡯࡮ࡧࡢࡺࡪࡸࡳࡪࡱࡱࢁ࠳࠭⁜"))
          return False
        if not options:
          bstack1l111lll111_opy_ = caps.get(bstack1ll11_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩ⁝")) or bstack1lllll11l1l1_opy_.get(bstack1ll11_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ⁞"), {})
          if bstack1ll11_opy_ (u"࠭࠭࠮ࡪࡨࡥࡩࡲࡥࡴࡵࠪ ") in bstack1l111lll111_opy_.get(bstack1ll11_opy_ (u"ࠧࡢࡴࡪࡷࠬ⁠"), []):
              logger.warning(bstack1ll11_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡽࡩ࡭࡮ࠣࡲࡴࡺࠠࡳࡷࡱࠤࡴࡴࠠ࡭ࡧࡪࡥࡨࡿࠠࡩࡧࡤࡨࡱ࡫ࡳࡴࠢࡰࡳࡩ࡫࠮ࠡࡕࡺ࡭ࡹࡩࡨࠡࡶࡲࠤࡳ࡫ࡷࠡࡪࡨࡥࡩࡲࡥࡴࡵࠣࡱࡴࡪࡥࠡࡱࡵࠤࡦࡼ࡯ࡪࡦࠣࡹࡸ࡯࡮ࡨࠢ࡫ࡩࡦࡪ࡬ࡦࡵࡶࠤࡲࡵࡤࡦ࠰ࠥ⁡"))
              return False
        return True
    except Exception as error:
        logger.debug(bstack1ll11_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡸࡤࡰ࡮ࡪࡡࡵࡧࠣࡥ࠶࠷ࡹࠡࡵࡸࡴࡵࡵࡲࡵࠢ࠽ࠦ⁢") + str(error))
        return False
def set_capabilities(caps, config):
  try:
    bstack1l1l1l111ll_opy_ = config.get(bstack1ll11_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪ⁣"), {})
    bstack1l1l1l111ll_opy_[bstack1ll11_opy_ (u"ࠫࡦࡻࡴࡩࡖࡲ࡯ࡪࡴࠧ⁤")] = os.getenv(bstack1ll11_opy_ (u"ࠬࡈࡓࡠࡃ࠴࠵࡞ࡥࡊࡘࡖࠪ⁥"))
    bstack1111lll111l_opy_ = json.loads(os.getenv(bstack1ll11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡢࡅࡈࡉࡅࡔࡕࡌࡆࡎࡒࡉࡕ࡛ࡢࡇࡔࡔࡆࡊࡉࡘࡖࡆ࡚ࡉࡐࡐࡢ࡝ࡒࡒࠧ⁦"), bstack1ll11_opy_ (u"ࠧࡼࡿࠪ⁧"))).get(bstack1ll11_opy_ (u"ࠨࡵࡦࡥࡳࡴࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩ⁨"))
    if not config[bstack1ll11_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡑࡴࡲࡨࡺࡩࡴࡎࡣࡳࠫ⁩")].get(bstack1ll11_opy_ (u"ࠥࡥࡵࡶ࡟ࡢࡷࡷࡳࡲࡧࡴࡦࠤ⁪")):
      if bstack1ll11_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬ⁫") in caps:
        caps[bstack1ll11_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭⁬")][bstack1ll11_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭⁭")] = bstack1l1l1l111ll_opy_
        caps[bstack1ll11_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨ⁮")][bstack1ll11_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨ⁯")][bstack1ll11_opy_ (u"ࠩࡶࡧࡦࡴ࡮ࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪ⁰")] = bstack1111lll111l_opy_
      else:
        caps[bstack1ll11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩⁱ")] = bstack1l1l1l111ll_opy_
        caps[bstack1ll11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪ⁲")][bstack1ll11_opy_ (u"ࠬࡹࡣࡢࡰࡱࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭⁳")] = bstack1111lll111l_opy_
  except Exception as error:
    logger.debug(bstack1ll11_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡺ࡬࡮ࡲࡥࠡࡵࡨࡸࡹ࡯࡮ࡨࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷ࠳ࠦࡅࡳࡴࡲࡶ࠿ࠦࠢ⁴") +  str(error))
def bstack111l1lll1l_opy_(driver, bstack1llll1ll1ll1_opy_):
  try:
    setattr(driver, bstack1ll11_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡁ࠲࠳ࡼࡗ࡭ࡵࡵ࡭ࡦࡖࡧࡦࡴࠧ⁵"), True)
    session = driver.session_id
    if session:
      bstack1lllll111l11_opy_ = True
      current_url = driver.current_url
      try:
        url = urlparse(current_url)
      except Exception as e:
        bstack1lllll111l11_opy_ = False
      bstack1lllll111l11_opy_ = url.scheme in [bstack1ll11_opy_ (u"ࠣࡪࡷࡸࡵࠨ⁶"), bstack1ll11_opy_ (u"ࠤ࡫ࡸࡹࡶࡳࠣ⁷")]
      if bstack1lllll111l11_opy_:
        if bstack1llll1ll1ll1_opy_:
          logger.info(bstack1ll11_opy_ (u"ࠥࡗࡪࡺࡵࡱࠢࡩࡳࡷࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡴࡦࡵࡷ࡭ࡳ࡭ࠠࡩࡣࡶࠤࡸࡺࡡࡳࡶࡨࡨ࠳ࠦࡁࡶࡶࡲࡱࡦࡺࡥࠡࡶࡨࡷࡹࠦࡣࡢࡵࡨࠤࡪࡾࡥࡤࡷࡷ࡭ࡴࡴࠠࡸ࡫࡯ࡰࠥࡨࡥࡨ࡫ࡱࠤࡲࡵ࡭ࡦࡰࡷࡥࡷ࡯࡬ࡺ࠰ࠥ⁸"))
      return bstack1llll1ll1ll1_opy_
  except Exception as e:
    logger.error(bstack1ll11_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡷࡹࡧࡲࡵ࡫ࡱ࡫ࠥࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡶࡧࡦࡴࠠࡧࡱࡵࠤࡹ࡮ࡩࡴࠢࡷࡩࡸࡺࠠࡤࡣࡶࡩ࠿ࠦࠢ⁹") + str(e))
    return False
def bstack1lllll1ll_opy_(driver, name, path):
  try:
    bstack1l111lll1ll_opy_ = {
        bstack1ll11_opy_ (u"ࠬࡺࡨࡕࡧࡶࡸࡗࡻ࡮ࡖࡷ࡬ࡨࠬ⁺"): threading.current_thread().current_test_uuid,
        bstack1ll11_opy_ (u"࠭ࡴࡩࡄࡸ࡭ࡱࡪࡕࡶ࡫ࡧࠫ⁻"): os.environ.get(bstack1ll11_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬ⁼"), bstack1ll11_opy_ (u"ࠨࠩ⁽")),
        bstack1ll11_opy_ (u"ࠩࡷ࡬ࡏࡽࡴࡕࡱ࡮ࡩࡳ࠭⁾"): os.environ.get(bstack1ll11_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢࡎ࡜࡚ࠧⁿ"), bstack1ll11_opy_ (u"ࠫࠬ₀"))
    }
    bstack1ll1l1ll1l1_opy_ = bstack11l111l1l_opy_.bstack1ll111lll1l_opy_(EVENTS.bstack1l1l1l11l1_opy_.value)
    logger.debug(bstack1ll11_opy_ (u"ࠬࡖࡥࡳࡨࡲࡶࡲ࡯࡮ࡨࠢࡶࡧࡦࡴࠠࡣࡧࡩࡳࡷ࡫ࠠࡴࡣࡹ࡭ࡳ࡭ࠠࡳࡧࡶࡹࡱࡺࡳࠨ₁"))
    try:
      if (bstack1ll1ll11_opy_(threading.current_thread(), bstack1ll11_opy_ (u"࠭ࡩࡴࡃࡳࡴࡆ࠷࠱ࡺࡖࡨࡷࡹ࠭₂"), None) and bstack1ll1ll11_opy_(threading.current_thread(), bstack1ll11_opy_ (u"ࠧࡢࡲࡳࡅ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩ₃"), None)):
        scripts = {bstack1ll11_opy_ (u"ࠨࡵࡦࡥࡳ࠭₄"): bstack11111lll11_opy_.perform_scan}
        bstack1lllll11lll1_opy_ = json.loads(scripts[bstack1ll11_opy_ (u"ࠤࡶࡧࡦࡴࠢ₅")].replace(bstack1ll11_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࠨ₆"), bstack1ll11_opy_ (u"ࠦࠧ₇")))
        bstack1lllll11lll1_opy_[bstack1ll11_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨ₈")][bstack1ll11_opy_ (u"࠭࡭ࡦࡶ࡫ࡳࡩ࠭₉")] = None
        scripts[bstack1ll11_opy_ (u"ࠢࡴࡥࡤࡲࠧ₊")] = bstack1ll11_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࠦ₋") + json.dumps(bstack1lllll11lll1_opy_)
        bstack11111lll11_opy_.bstack1l11l1llll_opy_(scripts)
        bstack11111lll11_opy_.store()
        logger.debug(driver.execute_script(bstack11111lll11_opy_.perform_scan))
      else:
        logger.debug(driver.execute_async_script(bstack11111lll11_opy_.perform_scan, {bstack1ll11_opy_ (u"ࠤࡰࡩࡹ࡮࡯ࡥࠤ₌"): name}))
      bstack11l111l1l_opy_.end(EVENTS.bstack1l1l1l11l1_opy_.value, bstack1ll1l1ll1l1_opy_ + bstack1ll11_opy_ (u"ࠥ࠾ࡸࡺࡡࡳࡶࠥ₍"), bstack1ll1l1ll1l1_opy_ + bstack1ll11_opy_ (u"ࠦ࠿࡫࡮ࡥࠤ₎"), True, None)
    except Exception as error:
      bstack11l111l1l_opy_.end(EVENTS.bstack1l1l1l11l1_opy_.value, bstack1ll1l1ll1l1_opy_ + bstack1ll11_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧ₏"), bstack1ll1l1ll1l1_opy_ + bstack1ll11_opy_ (u"ࠨ࠺ࡦࡰࡧࠦₐ"), False, str(error))
    bstack1ll1l1ll1l1_opy_ = bstack11l111l1l_opy_.bstack11ll1ll11ll_opy_(EVENTS.bstack1l111lll11l_opy_.value)
    bstack11l111l1l_opy_.mark(bstack1ll1l1ll1l1_opy_ + bstack1ll11_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢₑ"))
    try:
      if (bstack1ll1ll11_opy_(threading.current_thread(), bstack1ll11_opy_ (u"ࠨ࡫ࡶࡅࡵࡶࡁ࠲࠳ࡼࡘࡪࡹࡴࠨₒ"), None) and bstack1ll1ll11_opy_(threading.current_thread(), bstack1ll11_opy_ (u"ࠩࡤࡴࡵࡇ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫₓ"), None)):
        scripts = {bstack1ll11_opy_ (u"ࠪࡷࡨࡧ࡮ࠨₔ"): bstack11111lll11_opy_.perform_scan}
        bstack1lllll11lll1_opy_ = json.loads(scripts[bstack1ll11_opy_ (u"ࠦࡸࡩࡡ࡯ࠤₕ")].replace(bstack1ll11_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࠣₖ"), bstack1ll11_opy_ (u"ࠨࠢₗ")))
        bstack1lllll11lll1_opy_[bstack1ll11_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪₘ")][bstack1ll11_opy_ (u"ࠨ࡯ࡨࡸ࡭ࡵࡤࠨₙ")] = None
        scripts[bstack1ll11_opy_ (u"ࠤࡶࡧࡦࡴࠢₚ")] = bstack1ll11_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࠨₛ") + json.dumps(bstack1lllll11lll1_opy_)
        bstack11111lll11_opy_.bstack1l11l1llll_opy_(scripts)
        bstack11111lll11_opy_.store()
        logger.debug(driver.execute_script(bstack11111lll11_opy_.perform_scan))
      else:
        logger.debug(driver.execute_async_script(bstack11111lll11_opy_.bstack1lllll1l11ll_opy_, bstack1l111lll1ll_opy_))
      bstack11l111l1l_opy_.end(bstack1ll1l1ll1l1_opy_, bstack1ll1l1ll1l1_opy_ + bstack1ll11_opy_ (u"ࠦ࠿ࡹࡴࡢࡴࡷࠦₜ"), bstack1ll1l1ll1l1_opy_ + bstack1ll11_opy_ (u"ࠧࡀࡥ࡯ࡦࠥ₝"),True, None)
    except Exception as error:
      bstack11l111l1l_opy_.end(bstack1ll1l1ll1l1_opy_, bstack1ll1l1ll1l1_opy_ + bstack1ll11_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨ₞"), bstack1ll1l1ll1l1_opy_ + bstack1ll11_opy_ (u"ࠢ࠻ࡧࡱࡨࠧ₟"),False, str(error))
    logger.info(bstack1ll11_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡶࡨࡷࡹ࡯࡮ࡨࠢࡩࡳࡷࠦࡴࡩ࡫ࡶࠤࡹ࡫ࡳࡵࠢࡦࡥࡸ࡫ࠠࡩࡣࡶࠤࡪࡴࡤࡦࡦ࠱ࠦ₠"))
  except Exception as bstack1l1111llll1_opy_:
    logger.error(bstack1ll11_opy_ (u"ࠤࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡵࡩࡸࡻ࡬ࡵࡵࠣࡧࡴࡻ࡬ࡥࠢࡱࡳࡹࠦࡢࡦࠢࡳࡶࡴࡩࡥࡴࡵࡨࡨࠥ࡬࡯ࡳࠢࡷ࡬ࡪࠦࡴࡦࡵࡷࠤࡨࡧࡳࡦ࠼ࠣࠦ₡") + str(path) + bstack1ll11_opy_ (u"ࠥࠤࡊࡸࡲࡰࡴࠣ࠾ࠧ₢") + str(bstack1l1111llll1_opy_))
def bstack1llll1ll11ll_opy_(driver):
    caps = driver.capabilities
    if caps.get(bstack1ll11_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲࡔࡡ࡮ࡧࠥ₣")) and str(caps.get(bstack1ll11_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࡎࡢ࡯ࡨࠦ₤"))).lower() == bstack1ll11_opy_ (u"ࠨࡡ࡯ࡦࡵࡳ࡮ࡪࠢ₥"):
        bstack1l111l1llll_opy_ = caps.get(bstack1ll11_opy_ (u"ࠢࡢࡲࡳ࡭ࡺࡳ࠺ࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠤ₦")) or caps.get(bstack1ll11_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࡙ࡩࡷࡹࡩࡰࡰࠥ₧"))
        if bstack1l111l1llll_opy_ and int(str(bstack1l111l1llll_opy_)) < bstack11l1l111lll_opy_:
            return False
    return True
def bstack11l11ll11_opy_(config):
  if bstack1ll11_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ₨") in config:
        return config[bstack1ll11_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ₩")]
  for platform in config.get(bstack1ll11_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ₪"), []):
      if bstack1ll11_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ₫") in platform:
          return platform[bstack1ll11_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭€")]
  return None
def bstack1l11l1lll_opy_(bstack1l11l11lll_opy_):
  try:
    browser_name = bstack1l11l11lll_opy_[bstack1ll11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡰࡤࡱࡪ࠭₭")]
    browser_version = bstack1l11l11lll_opy_[bstack1ll11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡹࡩࡷࡹࡩࡰࡰࠪ₮")]
    chrome_options = bstack1l11l11lll_opy_[bstack1ll11_opy_ (u"ࠩࡦ࡬ࡷࡵ࡭ࡦࡡࡲࡴࡹ࡯࡯࡯ࡵࠪ₯")]
    try:
        bstack1llll1llllll_opy_ = int(browser_version.split(bstack1ll11_opy_ (u"ࠪ࠲ࠬ₰"))[0])
    except ValueError as e:
        logger.error(bstack1ll11_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡯࡬ࡦࠢࡦࡳࡳࡼࡥࡳࡶ࡬ࡲ࡬ࠦࡢࡳࡱࡺࡷࡪࡸࠠࡷࡧࡵࡷ࡮ࡵ࡮ࠣ₱") + str(e))
        return False
    if not (browser_name and browser_name.lower() == bstack1ll11_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࠬ₲")):
        logger.warning(bstack1ll11_opy_ (u"ࠨࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡻ࡮ࡲ࡬ࠡࡴࡸࡲࠥࡵ࡮࡭ࡻࠣࡳࡳࠦࡃࡩࡴࡲࡱࡪࠦࡢࡳࡱࡺࡷࡪࡸࡳ࠯ࠤ₳"))
        return False
    if bstack1llll1llllll_opy_ < bstack1lllll111ll1_opy_.bstack1l11l111111_opy_:
        logger.warning(bstack1lll1llllll_opy_ (u"ࠧࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡷ࡫ࡱࡶ࡫ࡵࡩࡸࠦࡃࡩࡴࡲࡱࡪࠦࡶࡦࡴࡶ࡭ࡴࡴࠠࡼࡅࡒࡒࡘ࡚ࡁࡏࡖࡖ࠲ࡒࡏࡎࡊࡏࡘࡑࡤࡔࡏࡏࡡࡅࡗ࡙ࡇࡃࡌࡡࡌࡒࡋࡘࡁࡠࡃ࠴࠵࡞ࡥࡓࡖࡒࡓࡓࡗ࡚ࡅࡅࡡࡆࡌࡗࡕࡍࡆࡡ࡙ࡉࡗ࡙ࡉࡐࡐࢀࠤࡴࡸࠠࡩ࡫ࡪ࡬ࡪࡸ࠮ࠨ₴"))
        return False
    if chrome_options and any(bstack1ll11_opy_ (u"ࠨ࠯࠰࡬ࡪࡧࡤ࡭ࡧࡶࡷࠬ₵") in value for value in chrome_options.values() if isinstance(value, str)):
        logger.warning(bstack1ll11_opy_ (u"ࠤࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡷࡪ࡮࡯ࠤࡳࡵࡴࠡࡴࡸࡲࠥࡵ࡮ࠡ࡮ࡨ࡫ࡦࡩࡹࠡࡪࡨࡥࡩࡲࡥࡴࡵࠣࡱࡴࡪࡥ࠯ࠢࡖࡻ࡮ࡺࡣࡩࠢࡷࡳࠥࡴࡥࡸࠢ࡫ࡩࡦࡪ࡬ࡦࡵࡶࠤࡲࡵࡤࡦࠢࡲࡶࠥࡧࡶࡰ࡫ࡧࠤࡺࡹࡩ࡯ࡩࠣ࡬ࡪࡧࡤ࡭ࡧࡶࡷࠥࡳ࡯ࡥࡧ࠱ࠦ₶"))
        return False
    return True
  except Exception as e:
    logger.error(bstack1ll11_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡩࡨࡦࡥ࡮࡭ࡳ࡭ࠠࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࠢࡶࡹࡵࡶ࡯ࡳࡶࠣࡪࡴࡸࠠ࡭ࡱࡦࡥࡱࠦࡃࡩࡴࡲࡱࡪࡀࠠࠣ₷") + str(e))
    return False
def bstack1l1111l11_opy_(bstack111l11l1l1_opy_, config):
    try:
      bstack1l1111ll11l_opy_ = bstack1ll11_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ₸") in config and config[bstack1ll11_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ₹")] == True
      bstack1llll1llll1l_opy_ = bstack1ll11_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪ₺") in config and str(config[bstack1ll11_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫ₻")]).lower() != bstack1ll11_opy_ (u"ࠨࡨࡤࡰࡸ࡫ࠧ₼")
      if not (bstack1l1111ll11l_opy_ and (not bstack111lll111l_opy_(config) or bstack1llll1llll1l_opy_)):
        return bstack111l11l1l1_opy_
      bstack1lllll11l1ll_opy_ = bstack11111lll11_opy_.bstack1lllll1l1l11_opy_
      if bstack1lllll11l1ll_opy_ is None:
        logger.debug(bstack1ll11_opy_ (u"ࠤࡊࡳࡴ࡭࡬ࡦࠢࡦ࡬ࡷࡵ࡭ࡦࠢࡲࡴࡹ࡯࡯࡯ࡵࠣࡥࡷ࡫ࠠࡏࡱࡱࡩࠧ₽"))
        return bstack111l11l1l1_opy_
      bstack1lllll1111ll_opy_ = int(str(bstack111l11ll1l1_opy_()).split(bstack1ll11_opy_ (u"ࠪ࠲ࠬ₾"))[0])
      logger.debug(bstack1ll11_opy_ (u"ࠦࡘ࡫࡬ࡦࡰ࡬ࡹࡲࠦࡶࡦࡴࡶ࡭ࡴࡴࠠࡥࡧࡷࡩࡨࡺࡥࡥ࠼ࠣࠦ₿") + str(bstack1lllll1111ll_opy_) + bstack1ll11_opy_ (u"ࠧࠨ⃀"))
      if bstack1lllll1111ll_opy_ == 3 and isinstance(bstack111l11l1l1_opy_, dict) and bstack1ll11_opy_ (u"࠭ࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠭⃁") in bstack111l11l1l1_opy_ and bstack1lllll11l1ll_opy_ is not None:
        if bstack1ll11_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬ⃂") not in bstack111l11l1l1_opy_[bstack1ll11_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨ⃃")]:
          bstack111l11l1l1_opy_[bstack1ll11_opy_ (u"ࠩࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩ⃄")][bstack1ll11_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨ⃅")] = {}
        if bstack1ll11_opy_ (u"ࠫࡦࡸࡧࡴࠩ⃆") in bstack1lllll11l1ll_opy_:
          if bstack1ll11_opy_ (u"ࠬࡧࡲࡨࡵࠪ⃇") not in bstack111l11l1l1_opy_[bstack1ll11_opy_ (u"࠭ࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠭⃈")][bstack1ll11_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬ⃉")]:
            bstack111l11l1l1_opy_[bstack1ll11_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨ⃊")][bstack1ll11_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ⃋")][bstack1ll11_opy_ (u"ࠪࡥࡷ࡭ࡳࠨ⃌")] = []
          for arg in bstack1lllll11l1ll_opy_[bstack1ll11_opy_ (u"ࠫࡦࡸࡧࡴࠩ⃍")]:
            if arg not in bstack111l11l1l1_opy_[bstack1ll11_opy_ (u"ࠬࡪࡥࡴ࡫ࡵࡩࡩࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠬ⃎")][bstack1ll11_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫ⃏")][bstack1ll11_opy_ (u"ࠧࡢࡴࡪࡷࠬ⃐")]:
              bstack111l11l1l1_opy_[bstack1ll11_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨ⃑")][bstack1ll11_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹ⃒ࠧ")][bstack1ll11_opy_ (u"ࠪࡥࡷ࡭ࡳࠨ⃓")].append(arg)
        if bstack1ll11_opy_ (u"ࠫࡪࡾࡴࡦࡰࡶ࡭ࡴࡴࡳࠨ⃔") in bstack1lllll11l1ll_opy_:
          if bstack1ll11_opy_ (u"ࠬ࡫ࡸࡵࡧࡱࡷ࡮ࡵ࡮ࡴࠩ⃕") not in bstack111l11l1l1_opy_[bstack1ll11_opy_ (u"࠭ࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠭⃖")][bstack1ll11_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬ⃗")]:
            bstack111l11l1l1_opy_[bstack1ll11_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨ⃘")][bstack1ll11_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹ⃙ࠧ")][bstack1ll11_opy_ (u"ࠪࡩࡽࡺࡥ࡯ࡵ࡬ࡳࡳࡹ⃚ࠧ")] = []
          for ext in bstack1lllll11l1ll_opy_[bstack1ll11_opy_ (u"ࠫࡪࡾࡴࡦࡰࡶ࡭ࡴࡴࡳࠨ⃛")]:
            if ext not in bstack111l11l1l1_opy_[bstack1ll11_opy_ (u"ࠬࡪࡥࡴ࡫ࡵࡩࡩࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠬ⃜")][bstack1ll11_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫ⃝")][bstack1ll11_opy_ (u"ࠧࡦࡺࡷࡩࡳࡹࡩࡰࡰࡶࠫ⃞")]:
              bstack111l11l1l1_opy_[bstack1ll11_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨ⃟")][bstack1ll11_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ⃠")][bstack1ll11_opy_ (u"ࠪࡩࡽࡺࡥ࡯ࡵ࡬ࡳࡳࡹࠧ⃡")].append(ext)
        if bstack1ll11_opy_ (u"ࠫࡵࡸࡥࡧࡵࠪ⃢") in bstack1lllll11l1ll_opy_:
          if bstack1ll11_opy_ (u"ࠬࡶࡲࡦࡨࡶࠫ⃣") not in bstack111l11l1l1_opy_[bstack1ll11_opy_ (u"࠭ࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠭⃤")][bstack1ll11_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷ⃥ࠬ")]:
            bstack111l11l1l1_opy_[bstack1ll11_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨ⃦")][bstack1ll11_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ⃧")][bstack1ll11_opy_ (u"ࠪࡴࡷ࡫ࡦࡴ⃨ࠩ")] = {}
          bstack1111l1l1lll_opy_(bstack111l11l1l1_opy_[bstack1ll11_opy_ (u"ࠫࡩ࡫ࡳࡪࡴࡨࡨࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠫ⃩")][bstack1ll11_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵ⃪ࠪ")][bstack1ll11_opy_ (u"࠭ࡰࡳࡧࡩࡷ⃫ࠬ")],
                    bstack1lllll11l1ll_opy_[bstack1ll11_opy_ (u"ࠧࡱࡴࡨࡪࡸ⃬࠭")])
        os.environ[bstack1ll11_opy_ (u"ࠨࡋࡖࡣࡓࡕࡎࡠࡄࡖࡘࡆࡉࡋࡠࡋࡑࡊࡗࡇ࡟ࡂ࠳࠴࡝ࡤ࡙ࡅࡔࡕࡌࡓࡓ⃭࠭")] = bstack1ll11_opy_ (u"ࠩࡷࡶࡺ࡫⃮ࠧ")
        return bstack111l11l1l1_opy_
      else:
        chrome_options = None
        if isinstance(bstack111l11l1l1_opy_, ChromeOptions):
          chrome_options = bstack111l11l1l1_opy_
        elif isinstance(bstack111l11l1l1_opy_, dict):
          for value in bstack111l11l1l1_opy_.values():
            if isinstance(value, ChromeOptions):
              chrome_options = value
              break
        if chrome_options is None:
          chrome_options = ChromeOptions()
          if isinstance(bstack111l11l1l1_opy_, dict):
            bstack111l11l1l1_opy_[bstack1ll11_opy_ (u"ࠪࡳࡵࡺࡩࡰࡰࡶ⃯ࠫ")] = chrome_options
          else:
            bstack111l11l1l1_opy_ = chrome_options
        if bstack1lllll11l1ll_opy_ is not None:
          if bstack1ll11_opy_ (u"ࠫࡦࡸࡧࡴࠩ⃰") in bstack1lllll11l1ll_opy_:
                bstack1llll1ll1lll_opy_ = chrome_options.arguments or []
                new_args = bstack1lllll11l1ll_opy_[bstack1ll11_opy_ (u"ࠬࡧࡲࡨࡵࠪ⃱")]
                for arg in new_args:
                    if arg not in bstack1llll1ll1lll_opy_:
                        chrome_options.add_argument(arg)
          if bstack1ll11_opy_ (u"࠭ࡥࡹࡶࡨࡲࡸ࡯࡯࡯ࡵࠪ⃲") in bstack1lllll11l1ll_opy_:
                existing_extensions = chrome_options.experimental_options.get(bstack1ll11_opy_ (u"ࠧࡦࡺࡷࡩࡳࡹࡩࡰࡰࡶࠫ⃳"), [])
                bstack1llll1ll1l1l_opy_ = bstack1lllll11l1ll_opy_[bstack1ll11_opy_ (u"ࠨࡧࡻࡸࡪࡴࡳࡪࡱࡱࡷࠬ⃴")]
                for extension in bstack1llll1ll1l1l_opy_:
                    if extension not in existing_extensions:
                        chrome_options.add_encoded_extension(extension)
          if bstack1ll11_opy_ (u"ࠩࡳࡶࡪ࡬ࡳࠨ⃵") in bstack1lllll11l1ll_opy_:
                bstack1lllll11ll1l_opy_ = chrome_options.experimental_options.get(bstack1ll11_opy_ (u"ࠪࡴࡷ࡫ࡦࡴࠩ⃶"), {})
                bstack1llll1lll1l1_opy_ = bstack1lllll11l1ll_opy_[bstack1ll11_opy_ (u"ࠫࡵࡸࡥࡧࡵࠪ⃷")]
                bstack1111l1l1lll_opy_(bstack1lllll11ll1l_opy_, bstack1llll1lll1l1_opy_)
                chrome_options.add_experimental_option(bstack1ll11_opy_ (u"ࠬࡶࡲࡦࡨࡶࠫ⃸"), bstack1lllll11ll1l_opy_)
        os.environ[bstack1ll11_opy_ (u"࠭ࡉࡔࡡࡑࡓࡓࡥࡂࡔࡖࡄࡇࡐࡥࡉࡏࡈࡕࡅࡤࡇ࠱࠲࡛ࡢࡗࡊ࡙ࡓࡊࡑࡑࠫ⃹")] = bstack1ll11_opy_ (u"ࠧࡵࡴࡸࡩࠬ⃺")
        return bstack111l11l1l1_opy_
    except Exception as e:
      logger.error(bstack1ll11_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡸࡪ࡬ࡰࡪࠦࡡࡥࡦ࡬ࡲ࡬ࠦ࡮ࡰࡰ࠰ࡆࡘࠦࡩ࡯ࡨࡵࡥࠥࡧ࠱࠲ࡻࠣࡧ࡭ࡸ࡯࡮ࡧࠣࡳࡵࡺࡩࡰࡰࡶ࠾ࠥࠨ⃻") + str(e))
      return bstack111l11l1l1_opy_