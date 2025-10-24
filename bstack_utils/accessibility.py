# coding: UTF-8
import sys
bstack1lll1_opy_ = sys.version_info [0] == 2
bstack11l11_opy_ = 2048
bstack1_opy_ = 7
def bstack1l1_opy_ (bstack1llllll_opy_):
    global bstack1l11111_opy_
    bstack1l111l_opy_ = ord (bstack1llllll_opy_ [-1])
    bstack11l1ll1_opy_ = bstack1llllll_opy_ [:-1]
    bstack11l1l1l_opy_ = bstack1l111l_opy_ % len (bstack11l1ll1_opy_)
    bstack11111l1_opy_ = bstack11l1ll1_opy_ [:bstack11l1l1l_opy_] + bstack11l1ll1_opy_ [bstack11l1l1l_opy_:]
    if bstack1lll1_opy_:
        bstack1lllll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11l11_opy_ - (bstack1l1ll11_opy_ + bstack1l111l_opy_) % bstack1_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11111l1_opy_)])
    else:
        bstack1lllll1_opy_ = str () .join ([chr (ord (char) - bstack11l11_opy_ - (bstack1l1ll11_opy_ + bstack1l111l_opy_) % bstack1_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11111l1_opy_)])
    return eval (bstack1lllll1_opy_)
import os
import json
import requests
import logging
import threading
import bstack_utils.constants as bstack1llll1l1ll11_opy_
from urllib.parse import urlparse
from bstack_utils.constants import bstack11l11l1ll11_opy_ as bstack1lllll1111l1_opy_, EVENTS
from bstack_utils.bstack11l1111ll_opy_ import bstack11l1111ll_opy_
from bstack_utils.helper import bstack1l1ll11l_opy_, bstack1llll1ll_opy_, bstack1lllllll11_opy_, bstack111l1ll1ll1_opy_, \
  bstack111l11l1111_opy_, bstack1ll11llll_opy_, get_host_info, bstack111l1ll1l11_opy_, bstack1lll1l1l11_opy_, error_handler, bstack111l1lll1l1_opy_, bstack111l1ll111l_opy_, bstack11lll111_opy_
from browserstack_sdk._version import __version__
from bstack_utils.bstack1ll1111l1_opy_ import get_logger
from bstack_utils.bstack111l11l11_opy_ import bstack1lllllll11l_opy_
from selenium.webdriver.chrome.options import Options as ChromeOptions
from browserstack_sdk.sdk_cli.cli import cli
from bstack_utils.constants import *
logger = get_logger(__name__)
bstack111l11l11_opy_ = bstack1lllllll11l_opy_()
@error_handler(class_method=False)
def _1llll1ll1l11_opy_(driver, bstack1lll1l1ll_opy_):
  response = {}
  try:
    caps = driver.capabilities
    response = {
        bstack1l1_opy_ (u"ࠪࡳࡸࡥ࡮ࡢ࡯ࡨࠫ῞"): caps.get(bstack1l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡔࡡ࡮ࡧࠪ῟"), None),
        bstack1l1_opy_ (u"ࠬࡵࡳࡠࡸࡨࡶࡸ࡯࡯࡯ࠩῠ"): bstack1lll1l1ll_opy_.get(bstack1l1_opy_ (u"࠭࡯ࡴࡘࡨࡶࡸ࡯࡯࡯ࠩῡ"), None),
        bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡰࡤࡱࡪ࠭ῢ"): caps.get(bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭ΰ"), None),
        bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡺࡪࡸࡳࡪࡱࡱࠫῤ"): caps.get(bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫῥ"), None)
    }
  except Exception as error:
    logger.debug(bstack1l1_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡪࡪࡺࡣࡩ࡫ࡱ࡫ࠥࡶ࡬ࡢࡶࡩࡳࡷࡳࠠࡥࡧࡷࡥ࡮ࡲࡳࠡࡹ࡬ࡸ࡭ࠦࡥࡳࡴࡲࡶࠥࡀࠠࠨῦ") + str(error))
  return response
def on():
    if os.environ.get(bstack1l1_opy_ (u"ࠬࡈࡓࡠࡃ࠴࠵࡞ࡥࡊࡘࡖࠪῧ"), None) is None or os.environ[bstack1l1_opy_ (u"࠭ࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗࠫῨ")] == bstack1l1_opy_ (u"ࠢ࡯ࡷ࡯ࡰࠧῩ"):
        return False
    return True
def bstack1l1l1llll_opy_(config):
  return config.get(bstack1l1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨῪ"), False) or any([p.get(bstack1l1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩΎ"), False) == True for p in config.get(bstack1l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭Ῥ"), [])])
def bstack1lll1l111l_opy_(config, bstack11111l1l1_opy_):
  try:
    bstack1llll1lllll1_opy_ = config.get(bstack1l1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ῭"), False)
    if int(bstack11111l1l1_opy_) < len(config.get(bstack1l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ΅"), [])) and config[bstack1l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ`")][bstack11111l1l1_opy_]:
      bstack1lllll111l1l_opy_ = config[bstack1l1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ῰")][bstack11111l1l1_opy_].get(bstack1l1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ῱"), None)
    else:
      bstack1lllll111l1l_opy_ = config.get(bstack1l1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩῲ"), None)
    if bstack1lllll111l1l_opy_ != None:
      bstack1llll1lllll1_opy_ = bstack1lllll111l1l_opy_
    bstack1llll1l1lll1_opy_ = os.getenv(bstack1l1_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨῳ")) is not None and len(os.getenv(bstack1l1_opy_ (u"ࠫࡇ࡙࡟ࡂ࠳࠴࡝ࡤࡐࡗࡕࠩῴ"))) > 0 and os.getenv(bstack1l1_opy_ (u"ࠬࡈࡓࡠࡃ࠴࠵࡞ࡥࡊࡘࡖࠪ῵")) != bstack1l1_opy_ (u"࠭࡮ࡶ࡮࡯ࠫῶ")
    return bstack1llll1lllll1_opy_ and bstack1llll1l1lll1_opy_
  except Exception as error:
    logger.debug(bstack1l1_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡶࡦࡴ࡬ࡪࡾ࡯࡮ࡨࠢࡷ࡬ࡪࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡳࡦࡵࡶ࡭ࡴࡴࠠࡸ࡫ࡷ࡬ࠥ࡫ࡲࡳࡱࡵࠤ࠿ࠦࠧῷ") + str(error))
  return False
def bstack1lll1111ll_opy_(test_tags):
  bstack1l111ll1l11_opy_ = os.getenv(bstack1l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡤࡇࡃࡄࡇࡖࡗࡎࡈࡉࡍࡋࡗ࡝ࡤࡉࡏࡏࡈࡌࡋ࡚ࡘࡁࡕࡋࡒࡒࡤ࡟ࡍࡍࠩῸ"))
  if bstack1l111ll1l11_opy_ is None:
    return True
  bstack1l111ll1l11_opy_ = json.loads(bstack1l111ll1l11_opy_)
  try:
    include_tags = bstack1l111ll1l11_opy_[bstack1l1_opy_ (u"ࠩ࡬ࡲࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧΌ")] if bstack1l1_opy_ (u"ࠪ࡭ࡳࡩ࡬ࡶࡦࡨࡘࡦ࡭ࡳࡊࡰࡗࡩࡸࡺࡩ࡯ࡩࡖࡧࡴࡶࡥࠨῺ") in bstack1l111ll1l11_opy_ and isinstance(bstack1l111ll1l11_opy_[bstack1l1_opy_ (u"ࠫ࡮ࡴࡣ࡭ࡷࡧࡩ࡙ࡧࡧࡴࡋࡱࡘࡪࡹࡴࡪࡰࡪࡗࡨࡵࡰࡦࠩΏ")], list) else []
    exclude_tags = bstack1l111ll1l11_opy_[bstack1l1_opy_ (u"ࠬ࡫ࡸࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪῼ")] if bstack1l1_opy_ (u"࠭ࡥࡹࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫ´") in bstack1l111ll1l11_opy_ and isinstance(bstack1l111ll1l11_opy_[bstack1l1_opy_ (u"ࠧࡦࡺࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩࠬ῾")], list) else []
    excluded = any(tag in exclude_tags for tag in test_tags)
    included = len(include_tags) == 0 or any(tag in include_tags for tag in test_tags)
    return not excluded and included
  except Exception as error:
    logger.debug(bstack1l1_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡸࡪ࡬ࡰࡪࠦࡶࡢ࡮࡬ࡨࡦࡺࡩ࡯ࡩࠣࡸࡪࡹࡴࠡࡥࡤࡷࡪࠦࡦࡰࡴࠣࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡦࡪ࡬࡯ࡳࡧࠣࡷࡨࡧ࡮࡯࡫ࡱ࡫࠳ࠦࡅࡳࡴࡲࡶࠥࡀࠠࠣ῿") + str(error))
  return False
def bstack1llll1ll1lll_opy_(config, frameworkName, bstack1llll1ll11l1_opy_, bstack1llll1l1ll1l_opy_):
  bstack1llll1lll111_opy_ = bstack111l1ll1ll1_opy_(config)
  bstack1llll1ll1l1l_opy_ = bstack111l11l1111_opy_(config)
  if bstack1llll1lll111_opy_ is None or bstack1llll1ll1l1l_opy_ is None:
    logger.error(bstack1l1_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡽࡨࡪ࡮ࡨࠤࡨࡸࡥࡢࡶ࡬ࡲ࡬ࠦࡴࡦࡵࡷࠤࡷࡻ࡮ࠡࡨࡲࡶࠥࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮࠻ࠢࡐ࡭ࡸࡹࡩ࡯ࡩࠣࡥࡺࡺࡨࡦࡰࡷ࡭ࡨࡧࡴࡪࡱࡱࠤࡹࡵ࡫ࡦࡰࠪ "))
    return [None, None]
  try:
    settings = json.loads(os.getenv(bstack1l1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚࡟ࡂࡅࡆࡉࡘ࡙ࡉࡃࡋࡏࡍ࡙࡟࡟ࡄࡑࡑࡊࡎࡍࡕࡓࡃࡗࡍࡔࡔ࡟࡚ࡏࡏࠫ "), bstack1l1_opy_ (u"ࠫࢀࢃࠧ ")))
    data = {
        bstack1l1_opy_ (u"ࠬࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࠪ "): config[bstack1l1_opy_ (u"࠭ࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠫ ")],
        bstack1l1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪ "): config.get(bstack1l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫ "), os.path.basename(os.getcwd())),
        bstack1l1_opy_ (u"ࠩࡶࡸࡦࡸࡴࡕ࡫ࡰࡩࠬ "): bstack1l1ll11l_opy_(),
        bstack1l1_opy_ (u"ࠪࡨࡪࡹࡣࡳ࡫ࡳࡸ࡮ࡵ࡮ࠨ "): config.get(bstack1l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡇࡩࡸࡩࡲࡪࡲࡷ࡭ࡴࡴࠧ "), bstack1l1_opy_ (u"ࠬ࠭ ")),
        bstack1l1_opy_ (u"࠭ࡳࡰࡷࡵࡧࡪ࠭​"): {
            bstack1l1_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡑࡥࡲ࡫ࠧ‌"): frameworkName,
            bstack1l1_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮࡚ࡪࡸࡳࡪࡱࡱࠫ‍"): bstack1llll1ll11l1_opy_,
            bstack1l1_opy_ (u"ࠩࡶࡨࡰ࡜ࡥࡳࡵ࡬ࡳࡳ࠭‎"): __version__,
            bstack1l1_opy_ (u"ࠪࡰࡦࡴࡧࡶࡣࡪࡩࠬ‏"): bstack1l1_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫ‐"),
            bstack1l1_opy_ (u"ࠬࡺࡥࡴࡶࡉࡶࡦࡳࡥࡸࡱࡵ࡯ࠬ‑"): bstack1l1_opy_ (u"࠭ࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࠨ‒"),
            bstack1l1_opy_ (u"ࠧࡵࡧࡶࡸࡋࡸࡡ࡮ࡧࡺࡳࡷࡱࡖࡦࡴࡶ࡭ࡴࡴࠧ–"): bstack1llll1l1ll1l_opy_
        },
        bstack1l1_opy_ (u"ࠨࡵࡨࡸࡹ࡯࡮ࡨࡵࠪ—"): settings,
        bstack1l1_opy_ (u"ࠩࡹࡩࡷࡹࡩࡰࡰࡆࡳࡳࡺࡲࡰ࡮ࠪ―"): bstack111l1ll1l11_opy_(),
        bstack1l1_opy_ (u"ࠪࡧ࡮ࡏ࡮ࡧࡱࠪ‖"): bstack1ll11llll_opy_(),
        bstack1l1_opy_ (u"ࠫ࡭ࡵࡳࡵࡋࡱࡪࡴ࠭‗"): get_host_info(),
        bstack1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠧ‘"): bstack1lllllll11_opy_(config)
    }
    headers = {
        bstack1l1_opy_ (u"࠭ࡃࡰࡰࡷࡩࡳࡺ࠭ࡕࡻࡳࡩࠬ’"): bstack1l1_opy_ (u"ࠧࡢࡲࡳࡰ࡮ࡩࡡࡵ࡫ࡲࡲ࠴ࡰࡳࡰࡰࠪ‚"),
    }
    config = {
        bstack1l1_opy_ (u"ࠨࡣࡸࡸ࡭࠭‛"): (bstack1llll1lll111_opy_, bstack1llll1ll1l1l_opy_),
        bstack1l1_opy_ (u"ࠩ࡫ࡩࡦࡪࡥࡳࡵࠪ“"): headers
    }
    response = bstack1lll1l1l11_opy_(bstack1l1_opy_ (u"ࠪࡔࡔ࡙ࡔࠨ”"), bstack1lllll1111l1_opy_ + bstack1l1_opy_ (u"ࠫ࠴ࡼ࠲࠰ࡶࡨࡷࡹࡥࡲࡶࡰࡶࠫ„"), data, config)
    bstack1llll1lll11l_opy_ = response.json()
    if bstack1llll1lll11l_opy_[bstack1l1_opy_ (u"ࠬࡹࡵࡤࡥࡨࡷࡸ࠭‟")]:
      parsed = json.loads(os.getenv(bstack1l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡢࡅࡈࡉࡅࡔࡕࡌࡆࡎࡒࡉࡕ࡛ࡢࡇࡔࡔࡆࡊࡉࡘࡖࡆ࡚ࡉࡐࡐࡢ࡝ࡒࡒࠧ†"), bstack1l1_opy_ (u"ࠧࡼࡿࠪ‡")))
      parsed[bstack1l1_opy_ (u"ࠨࡵࡦࡥࡳࡴࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩ•")] = bstack1llll1lll11l_opy_[bstack1l1_opy_ (u"ࠩࡧࡥࡹࡧࠧ‣")][bstack1l1_opy_ (u"ࠪࡷࡨࡧ࡮࡯ࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫ․")]
      os.environ[bstack1l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡠࡃࡆࡇࡊ࡙ࡓࡊࡄࡌࡐࡎ࡚࡙ࡠࡅࡒࡒࡋࡏࡇࡖࡔࡄࡘࡎࡕࡎࡠ࡛ࡐࡐࠬ‥")] = json.dumps(parsed)
      bstack11l1111ll_opy_.bstack1l1l1ll11_opy_(bstack1llll1lll11l_opy_[bstack1l1_opy_ (u"ࠬࡪࡡࡵࡣࠪ…")][bstack1l1_opy_ (u"࠭ࡳࡤࡴ࡬ࡴࡹࡹࠧ‧")])
      bstack11l1111ll_opy_.bstack1lllll11l111_opy_(bstack1llll1lll11l_opy_[bstack1l1_opy_ (u"ࠧࡥࡣࡷࡥࠬ ")][bstack1l1_opy_ (u"ࠨࡥࡲࡱࡲࡧ࡮ࡥࡵࠪ ")])
      bstack11l1111ll_opy_.store()
      return bstack1llll1lll11l_opy_[bstack1l1_opy_ (u"ࠩࡧࡥࡹࡧࠧ‪")][bstack1l1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡗࡳࡰ࡫࡮ࠨ‫")], bstack1llll1lll11l_opy_[bstack1l1_opy_ (u"ࠫࡩࡧࡴࡢࠩ‬")][bstack1l1_opy_ (u"ࠬ࡯ࡤࠨ‭")]
    else:
      logger.error(bstack1l1_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡺ࡬࡮ࡲࡥࠡࡴࡸࡲࡳ࡯࡮ࡨࠢࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲ࠿ࠦࠧ‮") + bstack1llll1lll11l_opy_[bstack1l1_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ ")])
      if bstack1llll1lll11l_opy_[bstack1l1_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ‰")] == bstack1l1_opy_ (u"ࠩࡌࡲࡻࡧ࡬ࡪࡦࠣࡧࡴࡴࡦࡪࡩࡸࡶࡦࡺࡩࡰࡰࠣࡴࡦࡹࡳࡦࡦ࠱ࠫ‱"):
        for bstack1llll1llll11_opy_ in bstack1llll1lll11l_opy_[bstack1l1_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࡵࠪ′")]:
          logger.error(bstack1llll1llll11_opy_[bstack1l1_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ″")])
      return None, None
  except Exception as error:
    logger.error(bstack1l1_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡹ࡫࡭ࡱ࡫ࠠࡤࡴࡨࡥࡹ࡯࡮ࡨࠢࡷࡩࡸࡺࠠࡳࡷࡱࠤ࡫ࡵࡲࠡࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱ࠾ࠥࠨ‴") +  str(error))
    return None, None
def bstack1llll1lll1ll_opy_():
  if os.getenv(bstack1l1_opy_ (u"࠭ࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗࠫ‵")) is None:
    return {
        bstack1l1_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧ‶"): bstack1l1_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧ‷"),
        bstack1l1_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ‸"): bstack1l1_opy_ (u"ࠪࡆࡺ࡯࡬ࡥࠢࡦࡶࡪࡧࡴࡪࡱࡱࠤ࡭ࡧࡤࠡࡨࡤ࡭ࡱ࡫ࡤ࠯ࠩ‹")
    }
  data = {bstack1l1_opy_ (u"ࠫࡪࡴࡤࡕ࡫ࡰࡩࠬ›"): bstack1l1ll11l_opy_()}
  headers = {
      bstack1l1_opy_ (u"ࠬࡇࡵࡵࡪࡲࡶ࡮ࢀࡡࡵ࡫ࡲࡲࠬ※"): bstack1l1_opy_ (u"࠭ࡂࡦࡣࡵࡩࡷࠦࠧ‼") + os.getenv(bstack1l1_opy_ (u"ࠢࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠧ‽")),
      bstack1l1_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡗࡽࡵ࡫ࠧ‾"): bstack1l1_opy_ (u"ࠩࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯࡫ࡵࡲࡲࠬ‿")
  }
  response = bstack1lll1l1l11_opy_(bstack1l1_opy_ (u"ࠪࡔ࡚࡚ࠧ⁀"), bstack1lllll1111l1_opy_ + bstack1l1_opy_ (u"ࠫ࠴ࡺࡥࡴࡶࡢࡶࡺࡴࡳ࠰ࡵࡷࡳࡵ࠭⁁"), data, { bstack1l1_opy_ (u"ࠬ࡮ࡥࡢࡦࡨࡶࡸ࠭⁂"): headers })
  try:
    if response.status_code == 200:
      logger.info(bstack1l1_opy_ (u"ࠨࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡗࡩࡸࡺࠠࡓࡷࡱࠤࡲࡧࡲ࡬ࡧࡧࠤࡦࡹࠠࡤࡱࡰࡴࡱ࡫ࡴࡦࡦࠣࡥࡹࠦࠢ⁃") + bstack1llll1ll_opy_().isoformat() + bstack1l1_opy_ (u"࡛ࠧࠩ⁄"))
      return {bstack1l1_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨ⁅"): bstack1l1_opy_ (u"ࠩࡶࡹࡨࡩࡥࡴࡵࠪ⁆"), bstack1l1_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ⁇"): bstack1l1_opy_ (u"ࠫࠬ⁈")}
    else:
      response.raise_for_status()
  except requests.RequestException as error:
    logger.error(bstack1l1_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡹ࡫࡭ࡱ࡫ࠠ࡮ࡣࡵ࡯࡮ࡴࡧࠡࡥࡲࡱࡵࡲࡥࡵ࡫ࡲࡲࠥࡵࡦࠡࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤ࡙࡫ࡳࡵࠢࡕࡹࡳࡀࠠࠣ⁉") + str(error))
    return {
        bstack1l1_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭⁊"): bstack1l1_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭⁋"),
        bstack1l1_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ⁌"): str(error)
    }
def bstack1lllll11111l_opy_(bstack1llll1lll1l1_opy_):
    return re.match(bstack1l1_opy_ (u"ࡴࠪࡢࡡࡪࠫࠩ࡞࠱ࡠࡩ࠱ࠩࡀࠦࠪ⁍"), bstack1llll1lll1l1_opy_.strip()) is not None
def bstack1l111l1l11_opy_(caps, options, desired_capabilities={}, config=None):
    try:
        if options:
          bstack1llll1ll11ll_opy_ = options.to_capabilities()
        elif desired_capabilities:
          bstack1llll1ll11ll_opy_ = desired_capabilities
        else:
          bstack1llll1ll11ll_opy_ = {}
        bstack1l111ll1lll_opy_ = (bstack1llll1ll11ll_opy_.get(bstack1l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡓࡧ࡭ࡦࠩ⁎"), bstack1l1_opy_ (u"ࠫࠬ⁏")).lower() or caps.get(bstack1l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡎࡢ࡯ࡨࠫ⁐"), bstack1l1_opy_ (u"࠭ࠧ⁑")).lower())
        if bstack1l111ll1lll_opy_ == bstack1l1_opy_ (u"ࠧࡪࡱࡶࠫ⁒"):
            return True
        if bstack1l111ll1lll_opy_ == bstack1l1_opy_ (u"ࠨࡣࡱࡨࡷࡵࡩࡥࠩ⁓"):
            bstack1l111l1lll1_opy_ = str(float(caps.get(bstack1l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰ࡚ࡪࡸࡳࡪࡱࡱࠫ⁔")) or bstack1llll1ll11ll_opy_.get(bstack1l1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫ⁕"), {}).get(bstack1l1_opy_ (u"ࠫࡴࡹࡖࡦࡴࡶ࡭ࡴࡴࠧ⁖"),bstack1l1_opy_ (u"ࠬ࠭⁗"))))
            if bstack1l111ll1lll_opy_ == bstack1l1_opy_ (u"࠭ࡡ࡯ࡦࡵࡳ࡮ࡪࠧ⁘") and int(bstack1l111l1lll1_opy_.split(bstack1l1_opy_ (u"ࠧ࠯ࠩ⁙"))[0]) < float(bstack11l11l1lll1_opy_):
                logger.warning(str(bstack11l11lll1ll_opy_))
                return False
            return True
        bstack1l111l11111_opy_ = caps.get(bstack1l1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩ⁚"), {}).get(bstack1l1_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࡐࡤࡱࡪ࠭⁛"), caps.get(bstack1l1_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࠪ⁜"), bstack1l1_opy_ (u"ࠫࠬ⁝")))
        if bstack1l111l11111_opy_:
            logger.warning(bstack1l1_opy_ (u"ࠧࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡺ࡭ࡱࡲࠠࡳࡷࡱࠤࡴࡴ࡬ࡺࠢࡲࡲࠥࡊࡥࡴ࡭ࡷࡳࡵࠦࡢࡳࡱࡺࡷࡪࡸࡳ࠯ࠤ⁞"))
            return False
        browser = caps.get(bstack1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫ "), bstack1l1_opy_ (u"ࠧࠨ⁠")).lower() or bstack1llll1ll11ll_opy_.get(bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭⁡"), bstack1l1_opy_ (u"ࠩࠪ⁢")).lower()
        if browser != bstack1l1_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧࠪ⁣"):
            logger.warning(bstack1l1_opy_ (u"ࠦࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡹ࡬ࡰࡱࠦࡲࡶࡰࠣࡳࡳࡲࡹࠡࡱࡱࠤࡈ࡮ࡲࡰ࡯ࡨࠤࡧࡸ࡯ࡸࡵࡨࡶࡸ࠴ࠢ⁤"))
            return False
        browser_version = caps.get(bstack1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭⁥")) or caps.get(bstack1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨ⁦")) or bstack1llll1ll11ll_opy_.get(bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨ⁧")) or bstack1llll1ll11ll_opy_.get(bstack1l1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩ⁨"), {}).get(bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪ⁩")) or bstack1llll1ll11ll_opy_.get(bstack1l1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫ⁪"), {}).get(bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭⁫"))
        bstack1l111l111ll_opy_ = bstack1llll1l1ll11_opy_.bstack1l111l1l11l_opy_
        bstack1lllll1111ll_opy_ = False
        if config is not None:
          bstack1lllll1111ll_opy_ = bstack1l1_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩ⁬") in config and str(config[bstack1l1_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪ⁭")]).lower() != bstack1l1_opy_ (u"ࠧࡧࡣ࡯ࡷࡪ࠭⁮")
        if os.environ.get(bstack1l1_opy_ (u"ࠨࡋࡖࡣࡓࡕࡎࡠࡄࡖࡘࡆࡉࡋࡠࡋࡑࡊࡗࡇ࡟ࡂ࠳࠴࡝ࡤ࡙ࡅࡔࡕࡌࡓࡓ࠭⁯"), bstack1l1_opy_ (u"ࠩࠪ⁰")).lower() == bstack1l1_opy_ (u"ࠪࡸࡷࡻࡥࠨⁱ") or bstack1lllll1111ll_opy_:
          bstack1l111l111ll_opy_ = bstack1llll1l1ll11_opy_.bstack1l1111l1ll1_opy_
        if browser_version and browser_version != bstack1l1_opy_ (u"ࠫࡱࡧࡴࡦࡵࡷࠫ⁲") and int(browser_version.split(bstack1l1_opy_ (u"ࠬ࠴ࠧ⁳"))[0]) <= bstack1l111l111ll_opy_:
          logger.warning(bstack1lll1llll11_opy_ (u"࠭ࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡻ࡮ࡲ࡬ࠡࡴࡸࡲࠥࡵ࡮࡭ࡻࠣࡳࡳࠦࡃࡩࡴࡲࡱࡪࠦࡢࡳࡱࡺࡷࡪࡸࠠࡷࡧࡵࡷ࡮ࡵ࡮ࠡࡩࡵࡩࡦࡺࡥࡳࠢࡷ࡬ࡦࡴࠠࡼ࡯࡬ࡲࡤࡧ࠱࠲ࡻࡢࡷࡺࡶࡰࡰࡴࡷࡩࡩࡥࡣࡩࡴࡲࡱࡪࡥࡶࡦࡴࡶ࡭ࡴࡴࡽ࠯ࠩ⁴"))
          return False
        if not options:
          bstack1l111l1llll_opy_ = caps.get(bstack1l1_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬ⁵")) or bstack1llll1ll11ll_opy_.get(bstack1l1_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭⁶"), {})
          if bstack1l1_opy_ (u"ࠩ࠰࠱࡭࡫ࡡࡥ࡮ࡨࡷࡸ࠭⁷") in bstack1l111l1llll_opy_.get(bstack1l1_opy_ (u"ࠪࡥࡷ࡭ࡳࠨ⁸"), []):
              logger.warning(bstack1l1_opy_ (u"ࠦࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡹ࡬ࡰࡱࠦ࡮ࡰࡶࠣࡶࡺࡴࠠࡰࡰࠣࡰࡪ࡭ࡡࡤࡻࠣ࡬ࡪࡧࡤ࡭ࡧࡶࡷࠥࡳ࡯ࡥࡧ࠱ࠤࡘࡽࡩࡵࡥ࡫ࠤࡹࡵࠠ࡯ࡧࡺࠤ࡭࡫ࡡࡥ࡮ࡨࡷࡸࠦ࡭ࡰࡦࡨࠤࡴࡸࠠࡢࡸࡲ࡭ࡩࠦࡵࡴ࡫ࡱ࡫ࠥ࡮ࡥࡢࡦ࡯ࡩࡸࡹࠠ࡮ࡱࡧࡩ࠳ࠨ⁹"))
              return False
        return True
    except Exception as error:
        logger.debug(bstack1l1_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡻࡧ࡬ࡪࡦࡤࡸࡪࠦࡡ࠲࠳ࡼࠤࡸࡻࡰࡱࡱࡵࡸࠥࡀࠢ⁺") + str(error))
        return False
def set_capabilities(caps, config):
  try:
    bstack1l1l1l1l11l_opy_ = config.get(bstack1l1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭⁻"), {})
    bstack1l1l1l1l11l_opy_[bstack1l1_opy_ (u"ࠧࡢࡷࡷ࡬࡙ࡵ࡫ࡦࡰࠪ⁼")] = os.getenv(bstack1l1_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭⁽"))
    bstack111l1111l11_opy_ = json.loads(os.getenv(bstack1l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡥࡁࡄࡅࡈࡗࡘࡏࡂࡊࡎࡌࡘ࡞ࡥࡃࡐࡐࡉࡍࡌ࡛ࡒࡂࡖࡌࡓࡓࡥ࡙ࡎࡎࠪ⁾"), bstack1l1_opy_ (u"ࠪࡿࢂ࠭ⁿ"))).get(bstack1l1_opy_ (u"ࠫࡸࡩࡡ࡯ࡰࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬ₀"))
    if not config[bstack1l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡔࡷࡵࡤࡶࡥࡷࡑࡦࡶࠧ₁")].get(bstack1l1_opy_ (u"ࠨࡡࡱࡲࡢࡥࡺࡺ࡯࡮ࡣࡷࡩࠧ₂")):
      if bstack1l1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨ₃") in caps:
        caps[bstack1l1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩ₄")][bstack1l1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩ₅")] = bstack1l1l1l1l11l_opy_
        caps[bstack1l1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫ₆")][bstack1l1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫ₇")][bstack1l1_opy_ (u"ࠬࡹࡣࡢࡰࡱࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭₈")] = bstack111l1111l11_opy_
      else:
        caps[bstack1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬ₉")] = bstack1l1l1l1l11l_opy_
        caps[bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭₊")][bstack1l1_opy_ (u"ࠨࡵࡦࡥࡳࡴࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩ₋")] = bstack111l1111l11_opy_
  except Exception as error:
    logger.debug(bstack1l1_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡽࡨࡪ࡮ࡨࠤࡸ࡫ࡴࡵ࡫ࡱ࡫ࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳ࠯ࠢࡈࡶࡷࡵࡲ࠻ࠢࠥ₌") +  str(error))
def bstack1l111111l_opy_(driver, bstack1llll1l1l1ll_opy_):
  try:
    setattr(driver, bstack1l1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡄ࠵࠶ࡿࡓࡩࡱࡸࡰࡩ࡙ࡣࡢࡰࠪ₍"), True)
    session = driver.session_id
    if session:
      bstack1lllll111ll1_opy_ = True
      current_url = driver.current_url
      try:
        url = urlparse(current_url)
      except Exception as e:
        bstack1lllll111ll1_opy_ = False
      bstack1lllll111ll1_opy_ = url.scheme in [bstack1l1_opy_ (u"ࠦ࡭ࡺࡴࡱࠤ₎"), bstack1l1_opy_ (u"ࠧ࡮ࡴࡵࡲࡶࠦ₏")]
      if bstack1lllll111ll1_opy_:
        if bstack1llll1l1l1ll_opy_:
          logger.info(bstack1l1_opy_ (u"ࠨࡓࡦࡶࡸࡴࠥ࡬࡯ࡳࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡷࡩࡸࡺࡩ࡯ࡩࠣ࡬ࡦࡹࠠࡴࡶࡤࡶࡹ࡫ࡤ࠯ࠢࡄࡹࡹࡵ࡭ࡢࡶࡨࠤࡹ࡫ࡳࡵࠢࡦࡥࡸ࡫ࠠࡦࡺࡨࡧࡺࡺࡩࡰࡰࠣࡻ࡮ࡲ࡬ࠡࡤࡨ࡫࡮ࡴࠠ࡮ࡱࡰࡩࡳࡺࡡࡳ࡫࡯ࡽ࠳ࠨₐ"))
      return bstack1llll1l1l1ll_opy_
  except Exception as e:
    logger.error(bstack1l1_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡳࡵࡣࡵࡸ࡮ࡴࡧࠡࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡹࡣࡢࡰࠣࡪࡴࡸࠠࡵࡪ࡬ࡷࠥࡺࡥࡴࡶࠣࡧࡦࡹࡥ࠻ࠢࠥₑ") + str(e))
    return False
def bstack111ll11l_opy_(driver, name, path):
  try:
    bstack1l1111l1111_opy_ = {
        bstack1l1_opy_ (u"ࠨࡶ࡫ࡘࡪࡹࡴࡓࡷࡱ࡙ࡺ࡯ࡤࠨₒ"): threading.current_thread().current_test_uuid,
        bstack1l1_opy_ (u"ࠩࡷ࡬ࡇࡻࡩ࡭ࡦࡘࡹ࡮ࡪࠧₓ"): os.environ.get(bstack1l1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨₔ"), bstack1l1_opy_ (u"ࠫࠬₕ")),
        bstack1l1_opy_ (u"ࠬࡺࡨࡋࡹࡷࡘࡴࡱࡥ࡯ࠩₖ"): os.environ.get(bstack1l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪₗ"), bstack1l1_opy_ (u"ࠧࠨₘ"))
    }
    bstack1ll11ll1lll_opy_ = bstack111l11l11_opy_.bstack1ll1l1l1lll_opy_(EVENTS.bstack1111l1l1ll_opy_.value)
    logger.debug(bstack1l1_opy_ (u"ࠨࡒࡨࡶ࡫ࡵࡲ࡮࡫ࡱ࡫ࠥࡹࡣࡢࡰࠣࡦࡪ࡬࡯ࡳࡧࠣࡷࡦࡼࡩ࡯ࡩࠣࡶࡪࡹࡵ࡭ࡶࡶࠫₙ"))
    try:
      if (bstack11lll111_opy_(threading.current_thread(), bstack1l1_opy_ (u"ࠩ࡬ࡷࡆࡶࡰࡂ࠳࠴ࡽ࡙࡫ࡳࡵࠩₚ"), None) and bstack11lll111_opy_(threading.current_thread(), bstack1l1_opy_ (u"ࠪࡥࡵࡶࡁ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬₛ"), None)):
        scripts = {bstack1l1_opy_ (u"ࠫࡸࡩࡡ࡯ࠩₜ"): bstack11l1111ll_opy_.perform_scan}
        bstack1lllll111l11_opy_ = json.loads(scripts[bstack1l1_opy_ (u"ࠧࡹࡣࡢࡰࠥ₝")].replace(bstack1l1_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࠤ₞"), bstack1l1_opy_ (u"ࠢࠣ₟")))
        bstack1lllll111l11_opy_[bstack1l1_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫ₠")][bstack1l1_opy_ (u"ࠩࡰࡩࡹ࡮࡯ࡥࠩ₡")] = None
        scripts[bstack1l1_opy_ (u"ࠥࡷࡨࡧ࡮ࠣ₢")] = bstack1l1_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࠢ₣") + json.dumps(bstack1lllll111l11_opy_)
        bstack11l1111ll_opy_.bstack1l1l1ll11_opy_(scripts)
        bstack11l1111ll_opy_.store()
        logger.debug(driver.execute_script(bstack11l1111ll_opy_.perform_scan))
      else:
        logger.debug(driver.execute_async_script(bstack11l1111ll_opy_.perform_scan, {bstack1l1_opy_ (u"ࠧࡳࡥࡵࡪࡲࡨࠧ₤"): name}))
      bstack111l11l11_opy_.end(EVENTS.bstack1111l1l1ll_opy_.value, bstack1ll11ll1lll_opy_ + bstack1l1_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨ₥"), bstack1ll11ll1lll_opy_ + bstack1l1_opy_ (u"ࠢ࠻ࡧࡱࡨࠧ₦"), True, None)
    except Exception as error:
      bstack111l11l11_opy_.end(EVENTS.bstack1111l1l1ll_opy_.value, bstack1ll11ll1lll_opy_ + bstack1l1_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣ₧"), bstack1ll11ll1lll_opy_ + bstack1l1_opy_ (u"ࠤ࠽ࡩࡳࡪࠢ₨"), False, str(error))
    bstack1ll11ll1lll_opy_ = bstack111l11l11_opy_.bstack11ll1l1l1l1_opy_(EVENTS.bstack1l1111lllll_opy_.value)
    bstack111l11l11_opy_.mark(bstack1ll11ll1lll_opy_ + bstack1l1_opy_ (u"ࠥ࠾ࡸࡺࡡࡳࡶࠥ₩"))
    try:
      if (bstack11lll111_opy_(threading.current_thread(), bstack1l1_opy_ (u"ࠫ࡮ࡹࡁࡱࡲࡄ࠵࠶ࡿࡔࡦࡵࡷࠫ₪"), None) and bstack11lll111_opy_(threading.current_thread(), bstack1l1_opy_ (u"ࠬࡧࡰࡱࡃ࠴࠵ࡾࡖ࡬ࡢࡶࡩࡳࡷࡳࠧ₫"), None)):
        scripts = {bstack1l1_opy_ (u"࠭ࡳࡤࡣࡱࠫ€"): bstack11l1111ll_opy_.perform_scan}
        bstack1lllll111l11_opy_ = json.loads(scripts[bstack1l1_opy_ (u"ࠢࡴࡥࡤࡲࠧ₭")].replace(bstack1l1_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࠦ₮"), bstack1l1_opy_ (u"ࠤࠥ₯")))
        bstack1lllll111l11_opy_[bstack1l1_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭₰")][bstack1l1_opy_ (u"ࠫࡲ࡫ࡴࡩࡱࡧࠫ₱")] = None
        scripts[bstack1l1_opy_ (u"ࠧࡹࡣࡢࡰࠥ₲")] = bstack1l1_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࠤ₳") + json.dumps(bstack1lllll111l11_opy_)
        bstack11l1111ll_opy_.bstack1l1l1ll11_opy_(scripts)
        bstack11l1111ll_opy_.store()
        logger.debug(driver.execute_script(bstack11l1111ll_opy_.perform_scan))
      else:
        logger.debug(driver.execute_async_script(bstack11l1111ll_opy_.bstack1lllll11ll1l_opy_, bstack1l1111l1111_opy_))
      bstack111l11l11_opy_.end(bstack1ll11ll1lll_opy_, bstack1ll11ll1lll_opy_ + bstack1l1_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢ₴"), bstack1ll11ll1lll_opy_ + bstack1l1_opy_ (u"ࠣ࠼ࡨࡲࡩࠨ₵"),True, None)
    except Exception as error:
      bstack111l11l11_opy_.end(bstack1ll11ll1lll_opy_, bstack1ll11ll1lll_opy_ + bstack1l1_opy_ (u"ࠤ࠽ࡷࡹࡧࡲࡵࠤ₶"), bstack1ll11ll1lll_opy_ + bstack1l1_opy_ (u"ࠥ࠾ࡪࡴࡤࠣ₷"),False, str(error))
    logger.info(bstack1l1_opy_ (u"ࠦࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡹ࡫ࡳࡵ࡫ࡱ࡫ࠥ࡬࡯ࡳࠢࡷ࡬࡮ࡹࠠࡵࡧࡶࡸࠥࡩࡡࡴࡧࠣ࡬ࡦࡹࠠࡦࡰࡧࡩࡩ࠴ࠢ₸"))
  except Exception as bstack1l111ll111l_opy_:
    logger.error(bstack1l1_opy_ (u"ࠧࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡸࡥࡴࡷ࡯ࡸࡸࠦࡣࡰࡷ࡯ࡨࠥࡴ࡯ࡵࠢࡥࡩࠥࡶࡲࡰࡥࡨࡷࡸ࡫ࡤࠡࡨࡲࡶࠥࡺࡨࡦࠢࡷࡩࡸࡺࠠࡤࡣࡶࡩ࠿ࠦࠢ₹") + str(path) + bstack1l1_opy_ (u"ࠨࠠࡆࡴࡵࡳࡷࠦ࠺ࠣ₺") + str(bstack1l111ll111l_opy_))
def bstack1llll1llll1l_opy_(driver):
    caps = driver.capabilities
    if caps.get(bstack1l1_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡐࡤࡱࡪࠨ₻")) and str(caps.get(bstack1l1_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡑࡥࡲ࡫ࠢ₼"))).lower() == bstack1l1_opy_ (u"ࠤࡤࡲࡩࡸ࡯ࡪࡦࠥ₽"):
        bstack1l111l1lll1_opy_ = caps.get(bstack1l1_opy_ (u"ࠥࡥࡵࡶࡩࡶ࡯࠽ࡴࡱࡧࡴࡧࡱࡵࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠧ₾")) or caps.get(bstack1l1_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲ࡜ࡥࡳࡵ࡬ࡳࡳࠨ₿"))
        if bstack1l111l1lll1_opy_ and int(str(bstack1l111l1lll1_opy_)) < bstack11l11l1lll1_opy_:
            return False
    return True
def bstack11111llll_opy_(config):
  if bstack1l1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ⃀") in config:
        return config[bstack1l1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭⃁")]
  for platform in config.get(bstack1l1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ⃂"), []):
      if bstack1l1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ⃃") in platform:
          return platform[bstack1l1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ⃄")]
  return None
def bstack111111l11_opy_(bstack11111l111l_opy_):
  try:
    browser_name = bstack11111l111l_opy_[bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡳࡧ࡭ࡦࠩ⃅")]
    browser_version = bstack11111l111l_opy_[bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭⃆")]
    chrome_options = bstack11111l111l_opy_[bstack1l1_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࡤࡵࡰࡵ࡫ࡲࡲࡸ࠭⃇")]
    try:
        bstack1llll1l1l1l1_opy_ = int(browser_version.split(bstack1l1_opy_ (u"࠭࠮ࠨ⃈"))[0])
    except ValueError as e:
        logger.error(bstack1l1_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡷࡩ࡫࡯ࡩࠥࡩ࡯࡯ࡸࡨࡶࡹ࡯࡮ࡨࠢࡥࡶࡴࡽࡳࡦࡴࠣࡺࡪࡸࡳࡪࡱࡱࠦ⃉") + str(e))
        return False
    if not (browser_name and browser_name.lower() == bstack1l1_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࠨ⃊")):
        logger.warning(bstack1l1_opy_ (u"ࠤࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡷࡪ࡮࡯ࠤࡷࡻ࡮ࠡࡱࡱࡰࡾࠦ࡯࡯ࠢࡆ࡬ࡷࡵ࡭ࡦࠢࡥࡶࡴࡽࡳࡦࡴࡶ࠲ࠧ⃋"))
        return False
    if bstack1llll1l1l1l1_opy_ < bstack1llll1l1ll11_opy_.bstack1l1111l1ll1_opy_:
        logger.warning(bstack1lll1llll11_opy_ (u"ࠪࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡳࡧࡴࡹ࡮ࡸࡥࡴࠢࡆ࡬ࡷࡵ࡭ࡦࠢࡹࡩࡷࡹࡩࡰࡰࠣࡿࡈࡕࡎࡔࡖࡄࡒ࡙࡙࠮ࡎࡋࡑࡍࡒ࡛ࡍࡠࡐࡒࡒࡤࡈࡓࡕࡃࡆࡏࡤࡏࡎࡇࡔࡄࡣࡆ࠷࠱࡚ࡡࡖ࡙ࡕࡖࡏࡓࡖࡈࡈࡤࡉࡈࡓࡑࡐࡉࡤ࡜ࡅࡓࡕࡌࡓࡓࢃࠠࡰࡴࠣ࡬࡮࡭ࡨࡦࡴ࠱ࠫ⃌"))
        return False
    if chrome_options and any(bstack1l1_opy_ (u"ࠫ࠲࠳ࡨࡦࡣࡧࡰࡪࡹࡳࠨ⃍") in value for value in chrome_options.values() if isinstance(value, str)):
        logger.warning(bstack1l1_opy_ (u"ࠧࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡺ࡭ࡱࡲࠠ࡯ࡱࡷࠤࡷࡻ࡮ࠡࡱࡱࠤࡱ࡫ࡧࡢࡥࡼࠤ࡭࡫ࡡࡥ࡮ࡨࡷࡸࠦ࡭ࡰࡦࡨ࠲࡙ࠥࡷࡪࡶࡦ࡬ࠥࡺ࡯ࠡࡰࡨࡻࠥ࡮ࡥࡢࡦ࡯ࡩࡸࡹࠠ࡮ࡱࡧࡩࠥࡵࡲࠡࡣࡹࡳ࡮ࡪࠠࡶࡵ࡬ࡲ࡬ࠦࡨࡦࡣࡧࡰࡪࡹࡳࠡ࡯ࡲࡨࡪ࠴ࠢ⃎"))
        return False
    return True
  except Exception as e:
    logger.error(bstack1l1_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡥ࡫ࡩࡨࡱࡩ࡯ࡩࠣࡴࡱࡧࡴࡧࡱࡵࡱࠥࡹࡵࡱࡲࡲࡶࡹࠦࡦࡰࡴࠣࡰࡴࡩࡡ࡭ࠢࡆ࡬ࡷࡵ࡭ࡦ࠼ࠣࠦ⃏") + str(e))
    return False
def bstack111ll1l1ll_opy_(bstack111ll1lll1_opy_, config):
    try:
      bstack1l1111ll1ll_opy_ = bstack1l1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ⃐") in config and config[bstack1l1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ⃑")] == True
      bstack1lllll1111ll_opy_ = bstack1l1_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ⃒࠭") in config and str(config[bstack1l1_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫⃓ࠧ")]).lower() != bstack1l1_opy_ (u"ࠫ࡫ࡧ࡬ࡴࡧࠪ⃔")
      if not (bstack1l1111ll1ll_opy_ and (not bstack1lllllll11_opy_(config) or bstack1lllll1111ll_opy_)):
        return bstack111ll1lll1_opy_
      bstack1llll1llllll_opy_ = bstack11l1111ll_opy_.bstack1lllll11l1l1_opy_
      if bstack1llll1llllll_opy_ is None:
        logger.debug(bstack1l1_opy_ (u"ࠧࡍ࡯ࡰࡩ࡯ࡩࠥࡩࡨࡳࡱࡰࡩࠥࡵࡰࡵ࡫ࡲࡲࡸࠦࡡࡳࡧࠣࡒࡴࡴࡥࠣ⃕"))
        return bstack111ll1lll1_opy_
      bstack1lllll111111_opy_ = int(str(bstack111l1ll111l_opy_()).split(bstack1l1_opy_ (u"࠭࠮ࠨ⃖"))[0])
      logger.debug(bstack1l1_opy_ (u"ࠢࡔࡧ࡯ࡩࡳ࡯ࡵ࡮ࠢࡹࡩࡷࡹࡩࡰࡰࠣࡨࡪࡺࡥࡤࡶࡨࡨ࠿ࠦࠢ⃗") + str(bstack1lllll111111_opy_) + bstack1l1_opy_ (u"ࠣࠤ⃘"))
      if bstack1lllll111111_opy_ == 3 and isinstance(bstack111ll1lll1_opy_, dict) and bstack1l1_opy_ (u"ࠩࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴ⃙ࠩ") in bstack111ll1lll1_opy_ and bstack1llll1llllll_opy_ is not None:
        if bstack1l1_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨ⃚") not in bstack111ll1lll1_opy_[bstack1l1_opy_ (u"ࠫࡩ࡫ࡳࡪࡴࡨࡨࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠫ⃛")]:
          bstack111ll1lll1_opy_[bstack1l1_opy_ (u"ࠬࡪࡥࡴ࡫ࡵࡩࡩࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠬ⃜")][bstack1l1_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫ⃝")] = {}
        if bstack1l1_opy_ (u"ࠧࡢࡴࡪࡷࠬ⃞") in bstack1llll1llllll_opy_:
          if bstack1l1_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭⃟") not in bstack111ll1lll1_opy_[bstack1l1_opy_ (u"ࠩࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩ⃠")][bstack1l1_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨ⃡")]:
            bstack111ll1lll1_opy_[bstack1l1_opy_ (u"ࠫࡩ࡫ࡳࡪࡴࡨࡨࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠫ⃢")][bstack1l1_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ⃣")][bstack1l1_opy_ (u"࠭ࡡࡳࡩࡶࠫ⃤")] = []
          for arg in bstack1llll1llllll_opy_[bstack1l1_opy_ (u"ࠧࡢࡴࡪࡷ⃥ࠬ")]:
            if arg not in bstack111ll1lll1_opy_[bstack1l1_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨ⃦")][bstack1l1_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ⃧")][bstack1l1_opy_ (u"ࠪࡥࡷ࡭ࡳࠨ⃨")]:
              bstack111ll1lll1_opy_[bstack1l1_opy_ (u"ࠫࡩ࡫ࡳࡪࡴࡨࡨࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠫ⃩")][bstack1l1_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵ⃪ࠪ")][bstack1l1_opy_ (u"࠭ࡡࡳࡩࡶ⃫ࠫ")].append(arg)
        if bstack1l1_opy_ (u"ࠧࡦࡺࡷࡩࡳࡹࡩࡰࡰࡶ⃬ࠫ") in bstack1llll1llllll_opy_:
          if bstack1l1_opy_ (u"ࠨࡧࡻࡸࡪࡴࡳࡪࡱࡱࡷ⃭ࠬ") not in bstack111ll1lll1_opy_[bstack1l1_opy_ (u"ࠩࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴ⃮ࠩ")][bstack1l1_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨ⃯")]:
            bstack111ll1lll1_opy_[bstack1l1_opy_ (u"ࠫࡩ࡫ࡳࡪࡴࡨࡨࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠫ⃰")][bstack1l1_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ⃱")][bstack1l1_opy_ (u"࠭ࡥࡹࡶࡨࡲࡸ࡯࡯࡯ࡵࠪ⃲")] = []
          for ext in bstack1llll1llllll_opy_[bstack1l1_opy_ (u"ࠧࡦࡺࡷࡩࡳࡹࡩࡰࡰࡶࠫ⃳")]:
            if ext not in bstack111ll1lll1_opy_[bstack1l1_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨ⃴")][bstack1l1_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ⃵")][bstack1l1_opy_ (u"ࠪࡩࡽࡺࡥ࡯ࡵ࡬ࡳࡳࡹࠧ⃶")]:
              bstack111ll1lll1_opy_[bstack1l1_opy_ (u"ࠫࡩ࡫ࡳࡪࡴࡨࡨࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠫ⃷")][bstack1l1_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ⃸")][bstack1l1_opy_ (u"࠭ࡥࡹࡶࡨࡲࡸ࡯࡯࡯ࡵࠪ⃹")].append(ext)
        if bstack1l1_opy_ (u"ࠧࡱࡴࡨࡪࡸ࠭⃺") in bstack1llll1llllll_opy_:
          if bstack1l1_opy_ (u"ࠨࡲࡵࡩ࡫ࡹࠧ⃻") not in bstack111ll1lll1_opy_[bstack1l1_opy_ (u"ࠩࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩ⃼")][bstack1l1_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨ⃽")]:
            bstack111ll1lll1_opy_[bstack1l1_opy_ (u"ࠫࡩ࡫ࡳࡪࡴࡨࡨࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠫ⃾")][bstack1l1_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ⃿")][bstack1l1_opy_ (u"࠭ࡰࡳࡧࡩࡷࠬ℀")] = {}
          bstack111l1lll1l1_opy_(bstack111ll1lll1_opy_[bstack1l1_opy_ (u"ࠧࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠧ℁")][bstack1l1_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ℂ")][bstack1l1_opy_ (u"ࠩࡳࡶࡪ࡬ࡳࠨ℃")],
                    bstack1llll1llllll_opy_[bstack1l1_opy_ (u"ࠪࡴࡷ࡫ࡦࡴࠩ℄")])
        os.environ[bstack1l1_opy_ (u"ࠫࡎ࡙࡟ࡏࡑࡑࡣࡇ࡙ࡔࡂࡅࡎࡣࡎࡔࡆࡓࡃࡢࡅ࠶࠷࡙ࡠࡕࡈࡗࡘࡏࡏࡏࠩ℅")] = bstack1l1_opy_ (u"ࠬࡺࡲࡶࡧࠪ℆")
        return bstack111ll1lll1_opy_
      else:
        chrome_options = None
        if isinstance(bstack111ll1lll1_opy_, ChromeOptions):
          chrome_options = bstack111ll1lll1_opy_
        elif isinstance(bstack111ll1lll1_opy_, dict):
          for value in bstack111ll1lll1_opy_.values():
            if isinstance(value, ChromeOptions):
              chrome_options = value
              break
        if chrome_options is None:
          chrome_options = ChromeOptions()
          if isinstance(bstack111ll1lll1_opy_, dict):
            bstack111ll1lll1_opy_[bstack1l1_opy_ (u"࠭࡯ࡱࡶ࡬ࡳࡳࡹࠧℇ")] = chrome_options
          else:
            bstack111ll1lll1_opy_ = chrome_options
        if bstack1llll1llllll_opy_ is not None:
          if bstack1l1_opy_ (u"ࠧࡢࡴࡪࡷࠬ℈") in bstack1llll1llllll_opy_:
                bstack1llll1ll1ll1_opy_ = chrome_options.arguments or []
                new_args = bstack1llll1llllll_opy_[bstack1l1_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭℉")]
                for arg in new_args:
                    if arg not in bstack1llll1ll1ll1_opy_:
                        chrome_options.add_argument(arg)
          if bstack1l1_opy_ (u"ࠩࡨࡼࡹ࡫࡮ࡴ࡫ࡲࡲࡸ࠭ℊ") in bstack1llll1llllll_opy_:
                existing_extensions = chrome_options.experimental_options.get(bstack1l1_opy_ (u"ࠪࡩࡽࡺࡥ࡯ࡵ࡬ࡳࡳࡹࠧℋ"), [])
                bstack1llll1ll111l_opy_ = bstack1llll1llllll_opy_[bstack1l1_opy_ (u"ࠫࡪࡾࡴࡦࡰࡶ࡭ࡴࡴࡳࠨℌ")]
                for extension in bstack1llll1ll111l_opy_:
                    if extension not in existing_extensions:
                        chrome_options.add_encoded_extension(extension)
          if bstack1l1_opy_ (u"ࠬࡶࡲࡦࡨࡶࠫℍ") in bstack1llll1llllll_opy_:
                bstack1llll1ll1111_opy_ = chrome_options.experimental_options.get(bstack1l1_opy_ (u"࠭ࡰࡳࡧࡩࡷࠬℎ"), {})
                bstack1llll1l1llll_opy_ = bstack1llll1llllll_opy_[bstack1l1_opy_ (u"ࠧࡱࡴࡨࡪࡸ࠭ℏ")]
                bstack111l1lll1l1_opy_(bstack1llll1ll1111_opy_, bstack1llll1l1llll_opy_)
                chrome_options.add_experimental_option(bstack1l1_opy_ (u"ࠨࡲࡵࡩ࡫ࡹࠧℐ"), bstack1llll1ll1111_opy_)
        os.environ[bstack1l1_opy_ (u"ࠩࡌࡗࡤࡔࡏࡏࡡࡅࡗ࡙ࡇࡃࡌࡡࡌࡒࡋࡘࡁࡠࡃ࠴࠵࡞ࡥࡓࡆࡕࡖࡍࡔࡔࠧℑ")] = bstack1l1_opy_ (u"ࠪࡸࡷࡻࡥࠨℒ")
        return bstack111ll1lll1_opy_
    except Exception as e:
      logger.error(bstack1l1_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡯࡬ࡦࠢࡤࡨࡩ࡯࡮ࡨࠢࡱࡳࡳ࠳ࡂࡔࠢ࡬ࡲ࡫ࡸࡡࠡࡣ࠴࠵ࡾࠦࡣࡩࡴࡲࡱࡪࠦ࡯ࡱࡶ࡬ࡳࡳࡹ࠺ࠡࠤℓ") + str(e))
      return bstack111ll1lll1_opy_