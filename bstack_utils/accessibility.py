# coding: UTF-8
import sys
bstack1lllll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1lll1l_opy_ = 7
def bstack11l11l1_opy_ (bstack111l1ll_opy_):
    global bstack1ll1l_opy_
    bstack1l1l1ll_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack1l11l_opy_ = bstack111l1ll_opy_ [:-1]
    bstack1lllll1l_opy_ = bstack1l1l1ll_opy_ % len (bstack1l11l_opy_)
    bstack11ll1l1_opy_ = bstack1l11l_opy_ [:bstack1lllll1l_opy_] + bstack1l11l_opy_ [bstack1lllll1l_opy_:]
    if bstack1lllll1_opy_:
        bstack1lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1l1ll11_opy_ + bstack1l1l1ll_opy_) % bstack1lll1l_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11ll1l1_opy_)])
    else:
        bstack1lll_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1l1ll11_opy_ + bstack1l1l1ll_opy_) % bstack1lll1l_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11ll1l1_opy_)])
    return eval (bstack1lll_opy_)
import os
import json
import requests
import logging
import threading
import bstack_utils.constants as bstack1llll1lll111_opy_
from urllib.parse import urlparse
from bstack_utils.constants import bstack11l11ll1l11_opy_ as bstack1llll1ll1lll_opy_, EVENTS
from bstack_utils.bstack1lllll111l_opy_ import bstack1lllll111l_opy_
from bstack_utils.helper import bstack1l11ll1l_opy_, bstack1l1l1ll1_opy_, bstack1ll11lll11_opy_, bstack1111ll11111_opy_, \
  bstack1111ll1l111_opy_, bstack11lll11l1_opy_, get_host_info, bstack1111l11ll11_opy_, bstack1ll1l1l11l_opy_, error_handler, bstack111l1111111_opy_, bstack1111lllll1l_opy_, bstack1ll11l1l_opy_
from browserstack_sdk._version import __version__
from bstack_utils.bstack11111l1l1_opy_ import get_logger
from bstack_utils.bstack11ll111ll1_opy_ import bstack1lllll1l111_opy_
from selenium.webdriver.chrome.options import Options as ChromeOptions
from browserstack_sdk.sdk_cli.cli import cli
from bstack_utils.constants import *
logger = get_logger(__name__)
bstack11ll111ll1_opy_ = bstack1lllll1l111_opy_()
@error_handler(class_method=False)
def _1llll1ll1ll1_opy_(driver, bstack1lll11lll_opy_):
  response = {}
  try:
    caps = driver.capabilities
    response = {
        bstack11l11l1_opy_ (u"ࠩࡲࡷࡤࡴࡡ࡮ࡧࠪ῝"): caps.get(bstack11l11l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡓࡧ࡭ࡦࠩ῞"), None),
        bstack11l11l1_opy_ (u"ࠫࡴࡹ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨ῟"): bstack1lll11lll_opy_.get(bstack11l11l1_opy_ (u"ࠬࡵࡳࡗࡧࡵࡷ࡮ࡵ࡮ࠨῠ"), None),
        bstack11l11l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸ࡟࡯ࡣࡰࡩࠬῡ"): caps.get(bstack11l11l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬῢ"), None),
        bstack11l11l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡹࡩࡷࡹࡩࡰࡰࠪΰ"): caps.get(bstack11l11l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪῤ"), None)
    }
  except Exception as error:
    logger.debug(bstack11l11l1_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡩࡩࡹࡩࡨࡪࡰࡪࠤࡵࡲࡡࡵࡨࡲࡶࡲࠦࡤࡦࡶࡤ࡭ࡱࡹࠠࡸ࡫ࡷ࡬ࠥ࡫ࡲࡳࡱࡵࠤ࠿ࠦࠧῥ") + str(error))
  return response
def on():
    if os.environ.get(bstack11l11l1_opy_ (u"ࠫࡇ࡙࡟ࡂ࠳࠴࡝ࡤࡐࡗࡕࠩῦ"), None) is None or os.environ[bstack11l11l1_opy_ (u"ࠬࡈࡓࡠࡃ࠴࠵࡞ࡥࡊࡘࡖࠪῧ")] == bstack11l11l1_opy_ (u"ࠨ࡮ࡶ࡮࡯ࠦῨ"):
        return False
    return True
def bstack111l1ll11l_opy_(config):
  return config.get(bstack11l11l1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧῩ"), False) or any([p.get(bstack11l11l1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨῪ"), False) == True for p in config.get(bstack11l11l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬΎ"), [])])
def bstack1l1l1llll_opy_(config, bstack111111ll11_opy_):
  try:
    bstack1llll1l1l1l1_opy_ = config.get(bstack11l11l1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪῬ"), False)
    if int(bstack111111ll11_opy_) < len(config.get(bstack11l11l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ῭"), [])) and config[bstack11l11l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ΅")][bstack111111ll11_opy_]:
      bstack1llll1l1lll1_opy_ = config[bstack11l11l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ`")][bstack111111ll11_opy_].get(bstack11l11l1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ῰"), None)
    else:
      bstack1llll1l1lll1_opy_ = config.get(bstack11l11l1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ῱"), None)
    if bstack1llll1l1lll1_opy_ != None:
      bstack1llll1l1l1l1_opy_ = bstack1llll1l1lll1_opy_
    bstack1llll1l1ll1l_opy_ = os.getenv(bstack11l11l1_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧῲ")) is not None and len(os.getenv(bstack11l11l1_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨῳ"))) > 0 and os.getenv(bstack11l11l1_opy_ (u"ࠫࡇ࡙࡟ࡂ࠳࠴࡝ࡤࡐࡗࡕࠩῴ")) != bstack11l11l1_opy_ (u"ࠬࡴࡵ࡭࡮ࠪ῵")
    return bstack1llll1l1l1l1_opy_ and bstack1llll1l1ll1l_opy_
  except Exception as error:
    logger.debug(bstack11l11l1_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡼࡥࡳ࡫ࡩࡽ࡮ࡴࡧࠡࡶ࡫ࡩࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡷࡪࡶ࡫ࠤࡪࡸࡲࡰࡴࠣ࠾ࠥ࠭ῶ") + str(error))
  return False
def bstack11l1l1l1l_opy_(test_tags):
  bstack1l111l1l11l_opy_ = os.getenv(bstack11l11l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡣࡆࡉࡃࡆࡕࡖࡍࡇࡏࡌࡊࡖ࡜ࡣࡈࡕࡎࡇࡋࡊ࡙ࡗࡇࡔࡊࡑࡑࡣ࡞ࡓࡌࠨῷ"))
  if bstack1l111l1l11l_opy_ is None:
    return True
  bstack1l111l1l11l_opy_ = json.loads(bstack1l111l1l11l_opy_)
  try:
    include_tags = bstack1l111l1l11l_opy_[bstack11l11l1_opy_ (u"ࠨ࡫ࡱࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ࠭Ὸ")] if bstack11l11l1_opy_ (u"ࠩ࡬ࡲࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧΌ") in bstack1l111l1l11l_opy_ and isinstance(bstack1l111l1l11l_opy_[bstack11l11l1_opy_ (u"ࠪ࡭ࡳࡩ࡬ࡶࡦࡨࡘࡦ࡭ࡳࡊࡰࡗࡩࡸࡺࡩ࡯ࡩࡖࡧࡴࡶࡥࠨῺ")], list) else []
    exclude_tags = bstack1l111l1l11l_opy_[bstack11l11l1_opy_ (u"ࠫࡪࡾࡣ࡭ࡷࡧࡩ࡙ࡧࡧࡴࡋࡱࡘࡪࡹࡴࡪࡰࡪࡗࡨࡵࡰࡦࠩΏ")] if bstack11l11l1_opy_ (u"ࠬ࡫ࡸࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪῼ") in bstack1l111l1l11l_opy_ and isinstance(bstack1l111l1l11l_opy_[bstack11l11l1_opy_ (u"࠭ࡥࡹࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫ´")], list) else []
    excluded = any(tag in exclude_tags for tag in test_tags)
    included = len(include_tags) == 0 or any(tag in include_tags for tag in test_tags)
    return not excluded and included
  except Exception as error:
    logger.debug(bstack11l11l1_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡷࡩ࡫࡯ࡩࠥࡼࡡ࡭࡫ࡧࡥࡹ࡯࡮ࡨࠢࡷࡩࡸࡺࠠࡤࡣࡶࡩࠥ࡬࡯ࡳࠢࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡥࡩ࡫ࡵࡲࡦࠢࡶࡧࡦࡴ࡮ࡪࡰࡪ࠲ࠥࡋࡲࡳࡱࡵࠤ࠿ࠦࠢ῾") + str(error))
  return False
def bstack1llll1llllll_opy_(config, frameworkName, bstack1llll1ll1l11_opy_, bstack1llll1ll1l1l_opy_):
  bstack1lllll111l1l_opy_ = bstack1111ll11111_opy_(config)
  bstack1llll1llll11_opy_ = bstack1111ll1l111_opy_(config)
  if bstack1lllll111l1l_opy_ is None or bstack1llll1llll11_opy_ is None:
    logger.error(bstack11l11l1_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡼ࡮ࡩ࡭ࡧࠣࡧࡷ࡫ࡡࡵ࡫ࡱ࡫ࠥࡺࡥࡴࡶࠣࡶࡺࡴࠠࡧࡱࡵࠤࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࠺ࠡࡏ࡬ࡷࡸ࡯࡮ࡨࠢࡤࡹࡹ࡮ࡥ࡯ࡶ࡬ࡧࡦࡺࡩࡰࡰࠣࡸࡴࡱࡥ࡯ࠩ῿"))
    return [None, None]
  try:
    settings = json.loads(os.getenv(bstack11l11l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡥࡁࡄࡅࡈࡗࡘࡏࡂࡊࡎࡌࡘ࡞ࡥࡃࡐࡐࡉࡍࡌ࡛ࡒࡂࡖࡌࡓࡓࡥ࡙ࡎࡎࠪ "), bstack11l11l1_opy_ (u"ࠪࡿࢂ࠭ ")))
    data = {
        bstack11l11l1_opy_ (u"ࠫࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠩ "): config[bstack11l11l1_opy_ (u"ࠬࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࠪ ")],
        bstack11l11l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩ "): config.get(bstack11l11l1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪ "), os.path.basename(os.getcwd())),
        bstack11l11l1_opy_ (u"ࠨࡵࡷࡥࡷࡺࡔࡪ࡯ࡨࠫ "): bstack1l11ll1l_opy_(),
        bstack11l11l1_opy_ (u"ࠩࡧࡩࡸࡩࡲࡪࡲࡷ࡭ࡴࡴࠧ "): config.get(bstack11l11l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡆࡨࡷࡨࡸࡩࡱࡶ࡬ࡳࡳ࠭ "), bstack11l11l1_opy_ (u"ࠫࠬ ")),
        bstack11l11l1_opy_ (u"ࠬࡹ࡯ࡶࡴࡦࡩࠬ "): {
            bstack11l11l1_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡐࡤࡱࡪ࠭​"): frameworkName,
            bstack11l11l1_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭࡙ࡩࡷࡹࡩࡰࡰࠪ‌"): bstack1llll1ll1l11_opy_,
            bstack11l11l1_opy_ (u"ࠨࡵࡧ࡯࡛࡫ࡲࡴ࡫ࡲࡲࠬ‍"): __version__,
            bstack11l11l1_opy_ (u"ࠩ࡯ࡥࡳ࡭ࡵࡢࡩࡨࠫ‎"): bstack11l11l1_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪ‏"),
            bstack11l11l1_opy_ (u"ࠫࡹ࡫ࡳࡵࡈࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫ‐"): bstack11l11l1_opy_ (u"ࠬࡹࡥ࡭ࡧࡱ࡭ࡺࡳࠧ‑"),
            bstack11l11l1_opy_ (u"࠭ࡴࡦࡵࡷࡊࡷࡧ࡭ࡦࡹࡲࡶࡰ࡜ࡥࡳࡵ࡬ࡳࡳ࠭‒"): bstack1llll1ll1l1l_opy_
        },
        bstack11l11l1_opy_ (u"ࠧࡴࡧࡷࡸ࡮ࡴࡧࡴࠩ–"): settings,
        bstack11l11l1_opy_ (u"ࠨࡸࡨࡶࡸ࡯࡯࡯ࡅࡲࡲࡹࡸ࡯࡭ࠩ—"): bstack1111l11ll11_opy_(),
        bstack11l11l1_opy_ (u"ࠩࡦ࡭ࡎࡴࡦࡰࠩ―"): bstack11lll11l1_opy_(),
        bstack11l11l1_opy_ (u"ࠪ࡬ࡴࡹࡴࡊࡰࡩࡳࠬ‖"): get_host_info(),
        bstack11l11l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭‗"): bstack1ll11lll11_opy_(config)
    }
    headers = {
        bstack11l11l1_opy_ (u"ࠬࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡔࡺࡲࡨࠫ‘"): bstack11l11l1_opy_ (u"࠭ࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳࡯ࡹ࡯࡯ࠩ’"),
    }
    config = {
        bstack11l11l1_opy_ (u"ࠧࡢࡷࡷ࡬ࠬ‚"): (bstack1lllll111l1l_opy_, bstack1llll1llll11_opy_),
        bstack11l11l1_opy_ (u"ࠨࡪࡨࡥࡩ࡫ࡲࡴࠩ‛"): headers
    }
    response = bstack1ll1l1l11l_opy_(bstack11l11l1_opy_ (u"ࠩࡓࡓࡘ࡚ࠧ“"), bstack1llll1ll1lll_opy_ + bstack11l11l1_opy_ (u"ࠪ࠳ࡻ࠸࠯ࡵࡧࡶࡸࡤࡸࡵ࡯ࡵࠪ”"), data, config)
    bstack1llll1ll11ll_opy_ = response.json()
    if bstack1llll1ll11ll_opy_[bstack11l11l1_opy_ (u"ࠫࡸࡻࡣࡤࡧࡶࡷࠬ„")]:
      parsed = json.loads(os.getenv(bstack11l11l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡡࡄࡇࡈࡋࡓࡔࡋࡅࡍࡑࡏࡔ࡚ࡡࡆࡓࡓࡌࡉࡈࡗࡕࡅ࡙ࡏࡏࡏࡡ࡜ࡑࡑ࠭‟"), bstack11l11l1_opy_ (u"࠭ࡻࡾࠩ†")))
      parsed[bstack11l11l1_opy_ (u"ࠧࡴࡥࡤࡲࡳ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨ‡")] = bstack1llll1ll11ll_opy_[bstack11l11l1_opy_ (u"ࠨࡦࡤࡸࡦ࠭•")][bstack11l11l1_opy_ (u"ࠩࡶࡧࡦࡴ࡮ࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪ‣")]
      os.environ[bstack11l11l1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚࡟ࡂࡅࡆࡉࡘ࡙ࡉࡃࡋࡏࡍ࡙࡟࡟ࡄࡑࡑࡊࡎࡍࡕࡓࡃࡗࡍࡔࡔ࡟࡚ࡏࡏࠫ․")] = json.dumps(parsed)
      bstack1lllll111l_opy_.bstack1ll111ll1_opy_(bstack1llll1ll11ll_opy_[bstack11l11l1_opy_ (u"ࠫࡩࡧࡴࡢࠩ‥")][bstack11l11l1_opy_ (u"ࠬࡹࡣࡳ࡫ࡳࡸࡸ࠭…")])
      bstack1lllll111l_opy_.bstack1lllll111lll_opy_(bstack1llll1ll11ll_opy_[bstack11l11l1_opy_ (u"࠭ࡤࡢࡶࡤࠫ‧")][bstack11l11l1_opy_ (u"ࠧࡤࡱࡰࡱࡦࡴࡤࡴࠩ ")])
      bstack1lllll111l_opy_.store()
      return bstack1llll1ll11ll_opy_[bstack11l11l1_opy_ (u"ࠨࡦࡤࡸࡦ࠭ ")][bstack11l11l1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡖࡲ࡯ࡪࡴࠧ‪")], bstack1llll1ll11ll_opy_[bstack11l11l1_opy_ (u"ࠪࡨࡦࡺࡡࠨ‫")][bstack11l11l1_opy_ (u"ࠫ࡮ࡪࠧ‬")]
    else:
      logger.error(bstack11l11l1_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡹ࡫࡭ࡱ࡫ࠠࡳࡷࡱࡲ࡮ࡴࡧࠡࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱ࠾ࠥ࠭‭") + bstack1llll1ll11ll_opy_[bstack11l11l1_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ‮")])
      if bstack1llll1ll11ll_opy_[bstack11l11l1_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ ")] == bstack11l11l1_opy_ (u"ࠨࡋࡱࡺࡦࡲࡩࡥࠢࡦࡳࡳ࡬ࡩࡨࡷࡵࡥࡹ࡯࡯࡯ࠢࡳࡥࡸࡹࡥࡥ࠰ࠪ‰"):
        for bstack1llll1ll111l_opy_ in bstack1llll1ll11ll_opy_[bstack11l11l1_opy_ (u"ࠩࡨࡶࡷࡵࡲࡴࠩ‱")]:
          logger.error(bstack1llll1ll111l_opy_[bstack11l11l1_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ′")])
      return None, None
  except Exception as error:
    logger.error(bstack11l11l1_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡸࡪ࡬ࡰࡪࠦࡣࡳࡧࡤࡸ࡮ࡴࡧࠡࡶࡨࡷࡹࠦࡲࡶࡰࠣࡪࡴࡸࠠࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰ࠽ࠤࠧ″") +  str(error))
    return None, None
def bstack1llll1ll11l1_opy_():
  if os.getenv(bstack11l11l1_opy_ (u"ࠬࡈࡓࡠࡃ࠴࠵࡞ࡥࡊࡘࡖࠪ‴")) is None:
    return {
        bstack11l11l1_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭‵"): bstack11l11l1_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭‶"),
        bstack11l11l1_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ‷"): bstack11l11l1_opy_ (u"ࠩࡅࡹ࡮ࡲࡤࠡࡥࡵࡩࡦࡺࡩࡰࡰࠣ࡬ࡦࡪࠠࡧࡣ࡬ࡰࡪࡪ࠮ࠨ‸")
    }
  data = {bstack11l11l1_opy_ (u"ࠪࡩࡳࡪࡔࡪ࡯ࡨࠫ‹"): bstack1l11ll1l_opy_()}
  headers = {
      bstack11l11l1_opy_ (u"ࠫࡆࡻࡴࡩࡱࡵ࡭ࡿࡧࡴࡪࡱࡱࠫ›"): bstack11l11l1_opy_ (u"ࠬࡈࡥࡢࡴࡨࡶࠥ࠭※") + os.getenv(bstack11l11l1_opy_ (u"ࠨࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗࠦ‼")),
      bstack11l11l1_opy_ (u"ࠧࡄࡱࡱࡸࡪࡴࡴ࠮ࡖࡼࡴࡪ࠭‽"): bstack11l11l1_opy_ (u"ࠨࡣࡳࡴࡱ࡯ࡣࡢࡶ࡬ࡳࡳ࠵ࡪࡴࡱࡱࠫ‾")
  }
  response = bstack1ll1l1l11l_opy_(bstack11l11l1_opy_ (u"ࠩࡓ࡙࡙࠭‿"), bstack1llll1ll1lll_opy_ + bstack11l11l1_opy_ (u"ࠪ࠳ࡹ࡫ࡳࡵࡡࡵࡹࡳࡹ࠯ࡴࡶࡲࡴࠬ⁀"), data, { bstack11l11l1_opy_ (u"ࠫ࡭࡫ࡡࡥࡧࡵࡷࠬ⁁"): headers })
  try:
    if response.status_code == 200:
      logger.info(bstack11l11l1_opy_ (u"ࠧࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡖࡨࡷࡹࠦࡒࡶࡰࠣࡱࡦࡸ࡫ࡦࡦࠣࡥࡸࠦࡣࡰ࡯ࡳࡰࡪࡺࡥࡥࠢࡤࡸࠥࠨ⁂") + bstack1l1l1ll1_opy_().isoformat() + bstack11l11l1_opy_ (u"࡚࠭ࠨ⁃"))
      return {bstack11l11l1_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧ⁄"): bstack11l11l1_opy_ (u"ࠨࡵࡸࡧࡨ࡫ࡳࡴࠩ⁅"), bstack11l11l1_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ⁆"): bstack11l11l1_opy_ (u"ࠪࠫ⁇")}
    else:
      response.raise_for_status()
  except requests.RequestException as error:
    logger.error(bstack11l11l1_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡸࡪ࡬ࡰࡪࠦ࡭ࡢࡴ࡮࡭ࡳ࡭ࠠࡤࡱࡰࡴࡱ࡫ࡴࡪࡱࡱࠤࡴ࡬ࠠࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡘࡪࡹࡴࠡࡔࡸࡲ࠿ࠦࠢ⁈") + str(error))
    return {
        bstack11l11l1_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬ⁉"): bstack11l11l1_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬ⁊"),
        bstack11l11l1_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ⁋"): str(error)
    }
def bstack1llll1ll1111_opy_(bstack1lllll11111l_opy_):
    return re.match(bstack11l11l1_opy_ (u"ࡳࠩࡡࡠࡩ࠱ࠨ࡝࠰࡟ࡨ࠰࠯࠿ࠥࠩ⁌"), bstack1lllll11111l_opy_.strip()) is not None
def bstack111l11111_opy_(caps, options, desired_capabilities={}, config=None):
    try:
        if options:
          bstack1lllll111ll1_opy_ = options.to_capabilities()
        elif desired_capabilities:
          bstack1lllll111ll1_opy_ = desired_capabilities
        else:
          bstack1lllll111ll1_opy_ = {}
        bstack1l1111lll11_opy_ = (bstack1lllll111ll1_opy_.get(bstack11l11l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡒࡦࡳࡥࠨ⁍"), bstack11l11l1_opy_ (u"ࠪࠫ⁎")).lower() or caps.get(bstack11l11l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡔࡡ࡮ࡧࠪ⁏"), bstack11l11l1_opy_ (u"ࠬ࠭⁐")).lower())
        if bstack1l1111lll11_opy_ == bstack11l11l1_opy_ (u"࠭ࡩࡰࡵࠪ⁑"):
            return True
        if bstack1l1111lll11_opy_ == bstack11l11l1_opy_ (u"ࠧࡢࡰࡧࡶࡴ࡯ࡤࠨ⁒"):
            bstack1l111ll1l11_opy_ = str(float(caps.get(bstack11l11l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࡙ࡩࡷࡹࡩࡰࡰࠪ⁓")) or bstack1lllll111ll1_opy_.get(bstack11l11l1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪ⁔"), {}).get(bstack11l11l1_opy_ (u"ࠪࡳࡸ࡜ࡥࡳࡵ࡬ࡳࡳ࠭⁕"),bstack11l11l1_opy_ (u"ࠫࠬ⁖"))))
            if bstack1l1111lll11_opy_ == bstack11l11l1_opy_ (u"ࠬࡧ࡮ࡥࡴࡲ࡭ࡩ࠭⁗") and int(bstack1l111ll1l11_opy_.split(bstack11l11l1_opy_ (u"࠭࠮ࠨ⁘"))[0]) < float(bstack11l1l1l1ll1_opy_):
                logger.warning(str(bstack11l11llll1l_opy_))
                return False
            return True
        bstack1l111l1lll1_opy_ = caps.get(bstack11l11l1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨ⁙"), {}).get(bstack11l11l1_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࡏࡣࡰࡩࠬ⁚"), caps.get(bstack11l11l1_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࠩ⁛"), bstack11l11l1_opy_ (u"ࠪࠫ⁜")))
        if bstack1l111l1lll1_opy_:
            logger.warning(bstack11l11l1_opy_ (u"ࠦࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡹ࡬ࡰࡱࠦࡲࡶࡰࠣࡳࡳࡲࡹࠡࡱࡱࠤࡉ࡫ࡳ࡬ࡶࡲࡴࠥࡨࡲࡰࡹࡶࡩࡷࡹ࠮ࠣ⁝"))
            return False
        browser = caps.get(bstack11l11l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪ⁞"), bstack11l11l1_opy_ (u"࠭ࠧ ")).lower() or bstack1lllll111ll1_opy_.get(bstack11l11l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬ⁠"), bstack11l11l1_opy_ (u"ࠨࠩ⁡")).lower()
        if browser != bstack11l11l1_opy_ (u"ࠩࡦ࡬ࡷࡵ࡭ࡦࠩ⁢"):
            logger.warning(bstack11l11l1_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡸ࡫࡯ࡰࠥࡸࡵ࡯ࠢࡲࡲࡱࡿࠠࡰࡰࠣࡇ࡭ࡸ࡯࡮ࡧࠣࡦࡷࡵࡷࡴࡧࡵࡷ࠳ࠨ⁣"))
            return False
        browser_version = caps.get(bstack11l11l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬ⁤")) or caps.get(bstack11l11l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡥࡶࡦࡴࡶ࡭ࡴࡴࠧ⁥")) or bstack1lllll111ll1_opy_.get(bstack11l11l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧ⁦")) or bstack1lllll111ll1_opy_.get(bstack11l11l1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨ⁧"), {}).get(bstack11l11l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩ⁨")) or bstack1lllll111ll1_opy_.get(bstack11l11l1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪ⁩"), {}).get(bstack11l11l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬ⁪"))
        bstack1l111l1l111_opy_ = bstack1llll1lll111_opy_.bstack1l1111l1ll1_opy_
        bstack1llll1l1llll_opy_ = False
        if config is not None:
          bstack1llll1l1llll_opy_ = bstack11l11l1_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨ⁫") in config and str(config[bstack11l11l1_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩ⁬")]).lower() != bstack11l11l1_opy_ (u"࠭ࡦࡢ࡮ࡶࡩࠬ⁭")
        if os.environ.get(bstack11l11l1_opy_ (u"ࠧࡊࡕࡢࡒࡔࡔ࡟ࡃࡕࡗࡅࡈࡑ࡟ࡊࡐࡉࡖࡆࡥࡁ࠲࠳࡜ࡣࡘࡋࡓࡔࡋࡒࡒࠬ⁮"), bstack11l11l1_opy_ (u"ࠨࠩ⁯")).lower() == bstack11l11l1_opy_ (u"ࠩࡷࡶࡺ࡫ࠧ⁰") or bstack1llll1l1llll_opy_:
          bstack1l111l1l111_opy_ = bstack1llll1lll111_opy_.bstack1l111l1l1ll_opy_
        if browser_version and browser_version != bstack11l11l1_opy_ (u"ࠪࡰࡦࡺࡥࡴࡶࠪⁱ") and int(browser_version.split(bstack11l11l1_opy_ (u"ࠫ࠳࠭⁲"))[0]) <= bstack1l111l1l111_opy_:
          logger.warning(bstack1llll11l1ll_opy_ (u"ࠬࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡺ࡭ࡱࡲࠠࡳࡷࡱࠤࡴࡴ࡬ࡺࠢࡲࡲࠥࡉࡨࡳࡱࡰࡩࠥࡨࡲࡰࡹࡶࡩࡷࠦࡶࡦࡴࡶ࡭ࡴࡴࠠࡨࡴࡨࡥࡹ࡫ࡲࠡࡶ࡫ࡥࡳࠦࡻ࡮࡫ࡱࡣࡦ࠷࠱ࡺࡡࡶࡹࡵࡶ࡯ࡳࡶࡨࡨࡤࡩࡨࡳࡱࡰࡩࡤࡼࡥࡳࡵ࡬ࡳࡳࢃ࠮ࠨ⁳"))
          return False
        if not options:
          bstack1l1111llll1_opy_ = caps.get(bstack11l11l1_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫ⁴")) or bstack1lllll111ll1_opy_.get(bstack11l11l1_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬ⁵"), {})
          if bstack11l11l1_opy_ (u"ࠨ࠯࠰࡬ࡪࡧࡤ࡭ࡧࡶࡷࠬ⁶") in bstack1l1111llll1_opy_.get(bstack11l11l1_opy_ (u"ࠩࡤࡶ࡬ࡹࠧ⁷"), []):
              logger.warning(bstack11l11l1_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡸ࡫࡯ࡰࠥࡴ࡯ࡵࠢࡵࡹࡳࠦ࡯࡯ࠢ࡯ࡩ࡬ࡧࡣࡺࠢ࡫ࡩࡦࡪ࡬ࡦࡵࡶࠤࡲࡵࡤࡦ࠰ࠣࡗࡼ࡯ࡴࡤࡪࠣࡸࡴࠦ࡮ࡦࡹࠣ࡬ࡪࡧࡤ࡭ࡧࡶࡷࠥࡳ࡯ࡥࡧࠣࡳࡷࠦࡡࡷࡱ࡬ࡨࠥࡻࡳࡪࡰࡪࠤ࡭࡫ࡡࡥ࡮ࡨࡷࡸࠦ࡭ࡰࡦࡨ࠲ࠧ⁸"))
              return False
        return True
    except Exception as error:
        logger.debug(bstack11l11l1_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡺࡦࡲࡩࡥࡣࡷࡩࠥࡧ࠱࠲ࡻࠣࡷࡺࡶࡰࡰࡴࡷࠤ࠿ࠨ⁹") + str(error))
        return False
def set_capabilities(caps, config):
  try:
    bstack1l11lllll1l_opy_ = config.get(bstack11l11l1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬ⁺"), {})
    bstack1l11lllll1l_opy_[bstack11l11l1_opy_ (u"࠭ࡡࡶࡶ࡫ࡘࡴࡱࡥ࡯ࠩ⁻")] = os.getenv(bstack11l11l1_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠬ⁼"))
    bstack111l111l11l_opy_ = json.loads(os.getenv(bstack11l11l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡤࡇࡃࡄࡇࡖࡗࡎࡈࡉࡍࡋࡗ࡝ࡤࡉࡏࡏࡈࡌࡋ࡚ࡘࡁࡕࡋࡒࡒࡤ࡟ࡍࡍࠩ⁽"), bstack11l11l1_opy_ (u"ࠩࡾࢁࠬ⁾"))).get(bstack11l11l1_opy_ (u"ࠪࡷࡨࡧ࡮࡯ࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫⁿ"))
    if not config[bstack11l11l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡓࡶࡴࡪࡵࡤࡶࡐࡥࡵ࠭₀")].get(bstack11l11l1_opy_ (u"ࠧࡧࡰࡱࡡࡤࡹࡹࡵ࡭ࡢࡶࡨࠦ₁")):
      if bstack11l11l1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧ₂") in caps:
        caps[bstack11l11l1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨ₃")][bstack11l11l1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨ₄")] = bstack1l11lllll1l_opy_
        caps[bstack11l11l1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪ₅")][bstack11l11l1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪ₆")][bstack11l11l1_opy_ (u"ࠫࡸࡩࡡ࡯ࡰࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬ₇")] = bstack111l111l11l_opy_
      else:
        caps[bstack11l11l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫ₈")] = bstack1l11lllll1l_opy_
        caps[bstack11l11l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬ₉")][bstack11l11l1_opy_ (u"ࠧࡴࡥࡤࡲࡳ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨ₊")] = bstack111l111l11l_opy_
  except Exception as error:
    logger.debug(bstack11l11l1_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡼ࡮ࡩ࡭ࡧࠣࡷࡪࡺࡴࡪࡰࡪࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹ࠮ࠡࡇࡵࡶࡴࡸ࠺ࠡࠤ₋") +  str(error))
def bstack11l111ll1l_opy_(driver, bstack1llll1llll1l_opy_):
  try:
    setattr(driver, bstack11l11l1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡃ࠴࠵ࡾ࡙ࡨࡰࡷ࡯ࡨࡘࡩࡡ࡯ࠩ₌"), True)
    session = driver.session_id
    if session:
      bstack1lllll111111_opy_ = True
      current_url = driver.current_url
      try:
        url = urlparse(current_url)
      except Exception as e:
        bstack1lllll111111_opy_ = False
      bstack1lllll111111_opy_ = url.scheme in [bstack11l11l1_opy_ (u"ࠥ࡬ࡹࡺࡰࠣ₍"), bstack11l11l1_opy_ (u"ࠦ࡭ࡺࡴࡱࡵࠥ₎")]
      if bstack1lllll111111_opy_:
        if bstack1llll1llll1l_opy_:
          logger.info(bstack11l11l1_opy_ (u"࡙ࠧࡥࡵࡷࡳࠤ࡫ࡵࡲࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡶࡨࡷࡹ࡯࡮ࡨࠢ࡫ࡥࡸࠦࡳࡵࡣࡵࡸࡪࡪ࠮ࠡࡃࡸࡸࡴࡳࡡࡵࡧࠣࡸࡪࡹࡴࠡࡥࡤࡷࡪࠦࡥࡹࡧࡦࡹࡹ࡯࡯࡯ࠢࡺ࡭ࡱࡲࠠࡣࡧࡪ࡭ࡳࠦ࡭ࡰ࡯ࡨࡲࡹࡧࡲࡪ࡮ࡼ࠲ࠧ₏"))
      return bstack1llll1llll1l_opy_
  except Exception as e:
    logger.error(bstack11l11l1_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡹࡴࡢࡴࡷ࡭ࡳ࡭ࠠࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡸࡩࡡ࡯ࠢࡩࡳࡷࠦࡴࡩ࡫ࡶࠤࡹ࡫ࡳࡵࠢࡦࡥࡸ࡫࠺ࠡࠤₐ") + str(e))
    return False
def bstack111ll11l_opy_(driver, name, path):
  try:
    bstack1l111l111l1_opy_ = {
        bstack11l11l1_opy_ (u"ࠧࡵࡪࡗࡩࡸࡺࡒࡶࡰࡘࡹ࡮ࡪࠧₑ"): threading.current_thread().current_test_uuid,
        bstack11l11l1_opy_ (u"ࠨࡶ࡫ࡆࡺ࡯࡬ࡥࡗࡸ࡭ࡩ࠭ₒ"): os.environ.get(bstack11l11l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧₓ"), bstack11l11l1_opy_ (u"ࠪࠫₔ")),
        bstack11l11l1_opy_ (u"ࠫࡹ࡮ࡊࡸࡶࡗࡳࡰ࡫࡮ࠨₕ"): os.environ.get(bstack11l11l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩₖ"), bstack11l11l1_opy_ (u"࠭ࠧₗ"))
    }
    bstack1ll11llllll_opy_ = bstack11ll111ll1_opy_.bstack1ll11111ll1_opy_(EVENTS.bstack11l1111l11_opy_.value)
    logger.debug(bstack11l11l1_opy_ (u"ࠧࡑࡧࡵࡪࡴࡸ࡭ࡪࡰࡪࠤࡸࡩࡡ࡯ࠢࡥࡩ࡫ࡵࡲࡦࠢࡶࡥࡻ࡯࡮ࡨࠢࡵࡩࡸࡻ࡬ࡵࡵࠪₘ"))
    try:
      if (bstack1ll11l1l_opy_(threading.current_thread(), bstack11l11l1_opy_ (u"ࠨ࡫ࡶࡅࡵࡶࡁ࠲࠳ࡼࡘࡪࡹࡴࠨₙ"), None) and bstack1ll11l1l_opy_(threading.current_thread(), bstack11l11l1_opy_ (u"ࠩࡤࡴࡵࡇ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫₚ"), None)):
        scripts = {bstack11l11l1_opy_ (u"ࠪࡷࡨࡧ࡮ࠨₛ"): bstack1lllll111l_opy_.perform_scan}
        bstack1lllll1111ll_opy_ = json.loads(scripts[bstack11l11l1_opy_ (u"ࠦࡸࡩࡡ࡯ࠤₜ")].replace(bstack11l11l1_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࠣ₝"), bstack11l11l1_opy_ (u"ࠨࠢ₞")))
        bstack1lllll1111ll_opy_[bstack11l11l1_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪ₟")][bstack11l11l1_opy_ (u"ࠨ࡯ࡨࡸ࡭ࡵࡤࠨ₠")] = None
        scripts[bstack11l11l1_opy_ (u"ࠤࡶࡧࡦࡴࠢ₡")] = bstack11l11l1_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࠨ₢") + json.dumps(bstack1lllll1111ll_opy_)
        bstack1lllll111l_opy_.bstack1ll111ll1_opy_(scripts)
        bstack1lllll111l_opy_.store()
        logger.debug(driver.execute_script(bstack1lllll111l_opy_.perform_scan))
      else:
        logger.debug(driver.execute_async_script(bstack1lllll111l_opy_.perform_scan, {bstack11l11l1_opy_ (u"ࠦࡲ࡫ࡴࡩࡱࡧࠦ₣"): name}))
      bstack11ll111ll1_opy_.end(EVENTS.bstack11l1111l11_opy_.value, bstack1ll11llllll_opy_ + bstack11l11l1_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧ₤"), bstack1ll11llllll_opy_ + bstack11l11l1_opy_ (u"ࠨ࠺ࡦࡰࡧࠦ₥"), True, None)
    except Exception as error:
      bstack11ll111ll1_opy_.end(EVENTS.bstack11l1111l11_opy_.value, bstack1ll11llllll_opy_ + bstack11l11l1_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢ₦"), bstack1ll11llllll_opy_ + bstack11l11l1_opy_ (u"ࠣ࠼ࡨࡲࡩࠨ₧"), False, str(error))
    bstack1ll11llllll_opy_ = bstack11ll111ll1_opy_.bstack11ll1l1l1l1_opy_(EVENTS.bstack1l1111l1111_opy_.value)
    bstack11ll111ll1_opy_.mark(bstack1ll11llllll_opy_ + bstack11l11l1_opy_ (u"ࠤ࠽ࡷࡹࡧࡲࡵࠤ₨"))
    try:
      if (bstack1ll11l1l_opy_(threading.current_thread(), bstack11l11l1_opy_ (u"ࠪ࡭ࡸࡇࡰࡱࡃ࠴࠵ࡾ࡚ࡥࡴࡶࠪ₩"), None) and bstack1ll11l1l_opy_(threading.current_thread(), bstack11l11l1_opy_ (u"ࠫࡦࡶࡰࡂ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭₪"), None)):
        scripts = {bstack11l11l1_opy_ (u"ࠬࡹࡣࡢࡰࠪ₫"): bstack1lllll111l_opy_.perform_scan}
        bstack1lllll1111ll_opy_ = json.loads(scripts[bstack11l11l1_opy_ (u"ࠨࡳࡤࡣࡱࠦ€")].replace(bstack11l11l1_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࠥ₭"), bstack11l11l1_opy_ (u"ࠣࠤ₮")))
        bstack1lllll1111ll_opy_[bstack11l11l1_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬ₯")][bstack11l11l1_opy_ (u"ࠪࡱࡪࡺࡨࡰࡦࠪ₰")] = None
        scripts[bstack11l11l1_opy_ (u"ࠦࡸࡩࡡ࡯ࠤ₱")] = bstack11l11l1_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࠣ₲") + json.dumps(bstack1lllll1111ll_opy_)
        bstack1lllll111l_opy_.bstack1ll111ll1_opy_(scripts)
        bstack1lllll111l_opy_.store()
        logger.debug(driver.execute_script(bstack1lllll111l_opy_.perform_scan))
      else:
        logger.debug(driver.execute_async_script(bstack1lllll111l_opy_.bstack1lllll11l11l_opy_, bstack1l111l111l1_opy_))
      bstack11ll111ll1_opy_.end(bstack1ll11llllll_opy_, bstack1ll11llllll_opy_ + bstack11l11l1_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨ₳"), bstack1ll11llllll_opy_ + bstack11l11l1_opy_ (u"ࠢ࠻ࡧࡱࡨࠧ₴"),True, None)
    except Exception as error:
      bstack11ll111ll1_opy_.end(bstack1ll11llllll_opy_, bstack1ll11llllll_opy_ + bstack11l11l1_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣ₵"), bstack1ll11llllll_opy_ + bstack11l11l1_opy_ (u"ࠤ࠽ࡩࡳࡪࠢ₶"),False, str(error))
    logger.info(bstack11l11l1_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡸࡪࡹࡴࡪࡰࡪࠤ࡫ࡵࡲࠡࡶ࡫࡭ࡸࠦࡴࡦࡵࡷࠤࡨࡧࡳࡦࠢ࡫ࡥࡸࠦࡥ࡯ࡦࡨࡨ࠳ࠨ₷"))
  except Exception as bstack1l1111l1lll_opy_:
    logger.error(bstack11l11l1_opy_ (u"ࠦࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡷ࡫ࡳࡶ࡮ࡷࡷࠥࡩ࡯ࡶ࡮ࡧࠤࡳࡵࡴࠡࡤࡨࠤࡵࡸ࡯ࡤࡧࡶࡷࡪࡪࠠࡧࡱࡵࠤࡹ࡮ࡥࠡࡶࡨࡷࡹࠦࡣࡢࡵࡨ࠾ࠥࠨ₸") + str(path) + bstack11l11l1_opy_ (u"ࠧࠦࡅࡳࡴࡲࡶࠥࡀࠢ₹") + str(bstack1l1111l1lll_opy_))
def bstack1llll1l1ll11_opy_(driver):
    caps = driver.capabilities
    if caps.get(bstack11l11l1_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡏࡣࡰࡩࠧ₺")) and str(caps.get(bstack11l11l1_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡐࡤࡱࡪࠨ₻"))).lower() == bstack11l11l1_opy_ (u"ࠣࡣࡱࡨࡷࡵࡩࡥࠤ₼"):
        bstack1l111ll1l11_opy_ = caps.get(bstack11l11l1_opy_ (u"ࠤࡤࡴࡵ࡯ࡵ࡮࠼ࡳࡰࡦࡺࡦࡰࡴࡰ࡚ࡪࡸࡳࡪࡱࡱࠦ₽")) or caps.get(bstack11l11l1_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠧ₾"))
        if bstack1l111ll1l11_opy_ and int(str(bstack1l111ll1l11_opy_)) < bstack11l1l1l1ll1_opy_:
            return False
    return True
def bstack111l1l1l11_opy_(config):
  if bstack11l11l1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ₿") in config:
        return config[bstack11l11l1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ⃀")]
  for platform in config.get(bstack11l11l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ⃁"), []):
      if bstack11l11l1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ⃂") in platform:
          return platform[bstack11l11l1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ⃃")]
  return None
def bstack1l1llllll_opy_(bstack1l11l1l1l_opy_):
  try:
    browser_name = bstack1l11l1l1l_opy_[bstack11l11l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡲࡦࡳࡥࠨ⃄")]
    browser_version = bstack1l11l1l1l_opy_[bstack11l11l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬ⃅")]
    chrome_options = bstack1l11l1l1l_opy_[bstack11l11l1_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࡣࡴࡶࡴࡪࡱࡱࡷࠬ⃆")]
    try:
        bstack1llll1lll1ll_opy_ = int(browser_version.split(bstack11l11l1_opy_ (u"ࠬ࠴ࠧ⃇"))[0])
    except ValueError as e:
        logger.error(bstack11l11l1_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡽࡨࡪ࡮ࡨࠤࡨࡵ࡮ࡷࡧࡵࡸ࡮ࡴࡧࠡࡤࡵࡳࡼࡹࡥࡳࠢࡹࡩࡷࡹࡩࡰࡰࠥ⃈") + str(e))
        return False
    if not (browser_name and browser_name.lower() == bstack11l11l1_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࠧ⃉")):
        logger.warning(bstack11l11l1_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡽࡩ࡭࡮ࠣࡶࡺࡴࠠࡰࡰ࡯ࡽࠥࡵ࡮ࠡࡅ࡫ࡶࡴࡳࡥࠡࡤࡵࡳࡼࡹࡥࡳࡵ࠱ࠦ⃊"))
        return False
    if bstack1llll1lll1ll_opy_ < bstack1llll1lll111_opy_.bstack1l111l1l1ll_opy_:
        logger.warning(bstack1llll11l1ll_opy_ (u"ࠩࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡲࡦࡳࡸ࡭ࡷ࡫ࡳࠡࡅ࡫ࡶࡴࡳࡥࠡࡸࡨࡶࡸ࡯࡯࡯ࠢࡾࡇࡔࡔࡓࡕࡃࡑࡘࡘ࠴ࡍࡊࡐࡌࡑ࡚ࡓ࡟ࡏࡑࡑࡣࡇ࡙ࡔࡂࡅࡎࡣࡎࡔࡆࡓࡃࡢࡅ࠶࠷࡙ࡠࡕࡘࡔࡕࡕࡒࡕࡇࡇࡣࡈࡎࡒࡐࡏࡈࡣ࡛ࡋࡒࡔࡋࡒࡒࢂࠦ࡯ࡳࠢ࡫࡭࡬࡮ࡥࡳ࠰ࠪ⃋"))
        return False
    if chrome_options and any(bstack11l11l1_opy_ (u"ࠪ࠱࠲࡮ࡥࡢࡦ࡯ࡩࡸࡹࠧ⃌") in value for value in chrome_options.values() if isinstance(value, str)):
        logger.warning(bstack11l11l1_opy_ (u"ࠦࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡹ࡬ࡰࡱࠦ࡮ࡰࡶࠣࡶࡺࡴࠠࡰࡰࠣࡰࡪ࡭ࡡࡤࡻࠣ࡬ࡪࡧࡤ࡭ࡧࡶࡷࠥࡳ࡯ࡥࡧ࠱ࠤࡘࡽࡩࡵࡥ࡫ࠤࡹࡵࠠ࡯ࡧࡺࠤ࡭࡫ࡡࡥ࡮ࡨࡷࡸࠦ࡭ࡰࡦࡨࠤࡴࡸࠠࡢࡸࡲ࡭ࡩࠦࡵࡴ࡫ࡱ࡫ࠥ࡮ࡥࡢࡦ࡯ࡩࡸࡹࠠ࡮ࡱࡧࡩ࠳ࠨ⃍"))
        return False
    return True
  except Exception as e:
    logger.error(bstack11l11l1_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡤࡪࡨࡧࡰ࡯࡮ࡨࠢࡳࡰࡦࡺࡦࡰࡴࡰࠤࡸࡻࡰࡱࡱࡵࡸࠥ࡬࡯ࡳࠢ࡯ࡳࡨࡧ࡬ࠡࡅ࡫ࡶࡴࡳࡥ࠻ࠢࠥ⃎") + str(e))
    return False
def bstack11lll1l11_opy_(bstack1ll1l1lll_opy_, config):
    try:
      bstack1l111ll11ll_opy_ = bstack11l11l1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭⃏") in config and config[bstack11l11l1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ⃐")] == True
      bstack1llll1l1llll_opy_ = bstack11l11l1_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬ⃑") in config and str(config[bstack11l11l1_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ⃒࠭")]).lower() != bstack11l11l1_opy_ (u"ࠪࡪࡦࡲࡳࡦ⃓ࠩ")
      if not (bstack1l111ll11ll_opy_ and (not bstack1ll11lll11_opy_(config) or bstack1llll1l1llll_opy_)):
        return bstack1ll1l1lll_opy_
      bstack1llll1lll11l_opy_ = bstack1lllll111l_opy_.bstack1lllll11l1l1_opy_
      if bstack1llll1lll11l_opy_ is None:
        logger.debug(bstack11l11l1_opy_ (u"ࠦࡌࡵ࡯ࡨ࡮ࡨࠤࡨ࡮ࡲࡰ࡯ࡨࠤࡴࡶࡴࡪࡱࡱࡷࠥࡧࡲࡦࠢࡑࡳࡳ࡫ࠢ⃔"))
        return bstack1ll1l1lll_opy_
      bstack1lllll111l11_opy_ = int(str(bstack1111lllll1l_opy_()).split(bstack11l11l1_opy_ (u"ࠬ࠴ࠧ⃕"))[0])
      logger.debug(bstack11l11l1_opy_ (u"ࠨࡓࡦ࡮ࡨࡲ࡮ࡻ࡭ࠡࡸࡨࡶࡸ࡯࡯࡯ࠢࡧࡩࡹ࡫ࡣࡵࡧࡧ࠾ࠥࠨ⃖") + str(bstack1lllll111l11_opy_) + bstack11l11l1_opy_ (u"ࠢࠣ⃗"))
      if bstack1lllll111l11_opy_ == 3 and isinstance(bstack1ll1l1lll_opy_, dict) and bstack11l11l1_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨ⃘") in bstack1ll1l1lll_opy_ and bstack1llll1lll11l_opy_ is not None:
        if bstack11l11l1_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹ⃙ࠧ") not in bstack1ll1l1lll_opy_[bstack11l11l1_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵ⃚ࠪ")]:
          bstack1ll1l1lll_opy_[bstack11l11l1_opy_ (u"ࠫࡩ࡫ࡳࡪࡴࡨࡨࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠫ⃛")][bstack11l11l1_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ⃜")] = {}
        if bstack11l11l1_opy_ (u"࠭ࡡࡳࡩࡶࠫ⃝") in bstack1llll1lll11l_opy_:
          if bstack11l11l1_opy_ (u"ࠧࡢࡴࡪࡷࠬ⃞") not in bstack1ll1l1lll_opy_[bstack11l11l1_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨ⃟")][bstack11l11l1_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ⃠")]:
            bstack1ll1l1lll_opy_[bstack11l11l1_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪ⃡")][bstack11l11l1_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩ⃢")][bstack11l11l1_opy_ (u"ࠬࡧࡲࡨࡵࠪ⃣")] = []
          for arg in bstack1llll1lll11l_opy_[bstack11l11l1_opy_ (u"࠭ࡡࡳࡩࡶࠫ⃤")]:
            if arg not in bstack1ll1l1lll_opy_[bstack11l11l1_opy_ (u"ࠧࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹ⃥ࠧ")][bstack11l11l1_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ⃦࠭")][bstack11l11l1_opy_ (u"ࠩࡤࡶ࡬ࡹࠧ⃧")]:
              bstack1ll1l1lll_opy_[bstack11l11l1_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵ⃨ࠪ")][bstack11l11l1_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩ⃩")][bstack11l11l1_opy_ (u"ࠬࡧࡲࡨࡵ⃪ࠪ")].append(arg)
        if bstack11l11l1_opy_ (u"࠭ࡥࡹࡶࡨࡲࡸ࡯࡯࡯ࡵ⃫ࠪ") in bstack1llll1lll11l_opy_:
          if bstack11l11l1_opy_ (u"ࠧࡦࡺࡷࡩࡳࡹࡩࡰࡰࡶ⃬ࠫ") not in bstack1ll1l1lll_opy_[bstack11l11l1_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨ⃭")][bstack11l11l1_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹ⃮ࠧ")]:
            bstack1ll1l1lll_opy_[bstack11l11l1_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵ⃯ࠪ")][bstack11l11l1_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩ⃰")][bstack11l11l1_opy_ (u"ࠬ࡫ࡸࡵࡧࡱࡷ࡮ࡵ࡮ࡴࠩ⃱")] = []
          for ext in bstack1llll1lll11l_opy_[bstack11l11l1_opy_ (u"࠭ࡥࡹࡶࡨࡲࡸ࡯࡯࡯ࡵࠪ⃲")]:
            if ext not in bstack1ll1l1lll_opy_[bstack11l11l1_opy_ (u"ࠧࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠧ⃳")][bstack11l11l1_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭⃴")][bstack11l11l1_opy_ (u"ࠩࡨࡼࡹ࡫࡮ࡴ࡫ࡲࡲࡸ࠭⃵")]:
              bstack1ll1l1lll_opy_[bstack11l11l1_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪ⃶")][bstack11l11l1_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩ⃷")][bstack11l11l1_opy_ (u"ࠬ࡫ࡸࡵࡧࡱࡷ࡮ࡵ࡮ࡴࠩ⃸")].append(ext)
        if bstack11l11l1_opy_ (u"࠭ࡰࡳࡧࡩࡷࠬ⃹") in bstack1llll1lll11l_opy_:
          if bstack11l11l1_opy_ (u"ࠧࡱࡴࡨࡪࡸ࠭⃺") not in bstack1ll1l1lll_opy_[bstack11l11l1_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨ⃻")][bstack11l11l1_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ⃼")]:
            bstack1ll1l1lll_opy_[bstack11l11l1_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪ⃽")][bstack11l11l1_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩ⃾")][bstack11l11l1_opy_ (u"ࠬࡶࡲࡦࡨࡶࠫ⃿")] = {}
          bstack111l1111111_opy_(bstack1ll1l1lll_opy_[bstack11l11l1_opy_ (u"࠭ࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠭℀")][bstack11l11l1_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬ℁")][bstack11l11l1_opy_ (u"ࠨࡲࡵࡩ࡫ࡹࠧℂ")],
                    bstack1llll1lll11l_opy_[bstack11l11l1_opy_ (u"ࠩࡳࡶࡪ࡬ࡳࠨ℃")])
        os.environ[bstack11l11l1_opy_ (u"ࠪࡍࡘࡥࡎࡐࡐࡢࡆࡘ࡚ࡁࡄࡍࡢࡍࡓࡌࡒࡂࡡࡄ࠵࠶࡟࡟ࡔࡇࡖࡗࡎࡕࡎࠨ℄")] = bstack11l11l1_opy_ (u"ࠫࡹࡸࡵࡦࠩ℅")
        return bstack1ll1l1lll_opy_
      else:
        chrome_options = None
        if isinstance(bstack1ll1l1lll_opy_, ChromeOptions):
          chrome_options = bstack1ll1l1lll_opy_
        elif isinstance(bstack1ll1l1lll_opy_, dict):
          for value in bstack1ll1l1lll_opy_.values():
            if isinstance(value, ChromeOptions):
              chrome_options = value
              break
        if chrome_options is None:
          chrome_options = ChromeOptions()
          if isinstance(bstack1ll1l1lll_opy_, dict):
            bstack1ll1l1lll_opy_[bstack11l11l1_opy_ (u"ࠬࡵࡰࡵ࡫ࡲࡲࡸ࠭℆")] = chrome_options
          else:
            bstack1ll1l1lll_opy_ = chrome_options
        if bstack1llll1lll11l_opy_ is not None:
          if bstack11l11l1_opy_ (u"࠭ࡡࡳࡩࡶࠫℇ") in bstack1llll1lll11l_opy_:
                bstack1lllll1111l1_opy_ = chrome_options.arguments or []
                new_args = bstack1llll1lll11l_opy_[bstack11l11l1_opy_ (u"ࠧࡢࡴࡪࡷࠬ℈")]
                for arg in new_args:
                    if arg not in bstack1lllll1111l1_opy_:
                        chrome_options.add_argument(arg)
          if bstack11l11l1_opy_ (u"ࠨࡧࡻࡸࡪࡴࡳࡪࡱࡱࡷࠬ℉") in bstack1llll1lll11l_opy_:
                existing_extensions = chrome_options.experimental_options.get(bstack11l11l1_opy_ (u"ࠩࡨࡼࡹ࡫࡮ࡴ࡫ࡲࡲࡸ࠭ℊ"), [])
                bstack1llll1lllll1_opy_ = bstack1llll1lll11l_opy_[bstack11l11l1_opy_ (u"ࠪࡩࡽࡺࡥ࡯ࡵ࡬ࡳࡳࡹࠧℋ")]
                for extension in bstack1llll1lllll1_opy_:
                    if extension not in existing_extensions:
                        chrome_options.add_encoded_extension(extension)
          if bstack11l11l1_opy_ (u"ࠫࡵࡸࡥࡧࡵࠪℌ") in bstack1llll1lll11l_opy_:
                bstack1llll1lll1l1_opy_ = chrome_options.experimental_options.get(bstack11l11l1_opy_ (u"ࠬࡶࡲࡦࡨࡶࠫℍ"), {})
                bstack1llll1l1l1ll_opy_ = bstack1llll1lll11l_opy_[bstack11l11l1_opy_ (u"࠭ࡰࡳࡧࡩࡷࠬℎ")]
                bstack111l1111111_opy_(bstack1llll1lll1l1_opy_, bstack1llll1l1l1ll_opy_)
                chrome_options.add_experimental_option(bstack11l11l1_opy_ (u"ࠧࡱࡴࡨࡪࡸ࠭ℏ"), bstack1llll1lll1l1_opy_)
        os.environ[bstack11l11l1_opy_ (u"ࠨࡋࡖࡣࡓࡕࡎࡠࡄࡖࡘࡆࡉࡋࡠࡋࡑࡊࡗࡇ࡟ࡂ࠳࠴࡝ࡤ࡙ࡅࡔࡕࡌࡓࡓ࠭ℐ")] = bstack11l11l1_opy_ (u"ࠩࡷࡶࡺ࡫ࠧℑ")
        return bstack1ll1l1lll_opy_
    except Exception as e:
      logger.error(bstack11l11l1_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡺ࡬࡮ࡲࡥࠡࡣࡧࡨ࡮ࡴࡧࠡࡰࡲࡲ࠲ࡈࡓࠡ࡫ࡱࡪࡷࡧࠠࡢ࠳࠴ࡽࠥࡩࡨࡳࡱࡰࡩࠥࡵࡰࡵ࡫ࡲࡲࡸࡀࠠࠣℒ") + str(e))
      return bstack1ll1l1lll_opy_