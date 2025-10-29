# coding: UTF-8
import sys
bstack1l1l111_opy_ = sys.version_info [0] == 2
bstack11l1ll_opy_ = 2048
bstack1llll11_opy_ = 7
def bstack11ll1l_opy_ (bstack1llllll1_opy_):
    global bstack1ll11_opy_
    bstack11ll111_opy_ = ord (bstack1llllll1_opy_ [-1])
    bstack1lll111_opy_ = bstack1llllll1_opy_ [:-1]
    bstack11l11l_opy_ = bstack11ll111_opy_ % len (bstack1lll111_opy_)
    bstack1l1ll11_opy_ = bstack1lll111_opy_ [:bstack11l11l_opy_] + bstack1lll111_opy_ [bstack11l11l_opy_:]
    if bstack1l1l111_opy_:
        bstack11111l1_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll_opy_ - (bstack1l11111_opy_ + bstack11ll111_opy_) % bstack1llll11_opy_) for bstack1l11111_opy_, char in enumerate (bstack1l1ll11_opy_)])
    else:
        bstack11111l1_opy_ = str () .join ([chr (ord (char) - bstack11l1ll_opy_ - (bstack1l11111_opy_ + bstack11ll111_opy_) % bstack1llll11_opy_) for bstack1l11111_opy_, char in enumerate (bstack1l1ll11_opy_)])
    return eval (bstack11111l1_opy_)
import os
import json
import requests
import logging
import threading
import bstack_utils.constants as bstack1llll1l1l11l_opy_
from urllib.parse import urlparse
from bstack_utils.constants import bstack11l11ll11ll_opy_ as bstack1llll1l1l1l1_opy_, EVENTS
from bstack_utils.bstack1l1l111ll_opy_ import bstack1l1l111ll_opy_
from bstack_utils.helper import bstack1l111ll1_opy_, bstack1l1l1ll1_opy_, bstack11ll1l1l1_opy_, bstack111l1l11l1l_opy_, \
  bstack111l111l1l1_opy_, bstack1l1ll1l1ll_opy_, get_host_info, bstack1111lll1l11_opy_, bstack1l1llllll_opy_, error_handler, bstack1111l11l111_opy_, bstack111l1111l1l_opy_, bstack1lllll11_opy_
from browserstack_sdk._version import __version__
from bstack_utils.bstack1l11111111_opy_ import get_logger
from bstack_utils.bstack1ll1l1lll_opy_ import bstack1llll111ll1_opy_
from selenium.webdriver.chrome.options import Options as ChromeOptions
from browserstack_sdk.sdk_cli.cli import cli
from bstack_utils.constants import *
logger = get_logger(__name__)
bstack1ll1l1lll_opy_ = bstack1llll111ll1_opy_()
@error_handler(class_method=False)
def _1llll1lll1ll_opy_(driver, bstack1llll111l_opy_):
  response = {}
  try:
    caps = driver.capabilities
    response = {
        bstack11ll1l_opy_ (u"ࠧࡰࡵࡢࡲࡦࡳࡥࠨ "): caps.get(bstack11ll1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡑࡥࡲ࡫ࠧ "), None),
        bstack11ll1l_opy_ (u"ࠩࡲࡷࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ "): bstack1llll111l_opy_.get(bstack11ll1l_opy_ (u"ࠪࡳࡸ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ "), None),
        bstack11ll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡤࡴࡡ࡮ࡧࠪ "): caps.get(bstack11ll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪ "), None),
        bstack11ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨ​"): caps.get(bstack11ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨ‌"), None)
    }
  except Exception as error:
    logger.debug(bstack11ll1l_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡧࡧࡷࡧ࡭࡯࡮ࡨࠢࡳࡰࡦࡺࡦࡰࡴࡰࠤࡩ࡫ࡴࡢ࡫࡯ࡷࠥࡽࡩࡵࡪࠣࡩࡷࡸ࡯ࡳࠢ࠽ࠤࠬ‍") + str(error))
  return response
def on():
    if os.environ.get(bstack11ll1l_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧ‎"), None) is None or os.environ[bstack11ll1l_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨ‏")] == bstack11ll1l_opy_ (u"ࠦࡳࡻ࡬࡭ࠤ‐"):
        return False
    return True
def bstack11111ll111_opy_(config):
  return config.get(bstack11ll1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ‑"), False) or any([p.get(bstack11ll1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭‒"), False) == True for p in config.get(bstack11ll1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ–"), [])])
def bstack1111llll1_opy_(config, bstack1l1llll1ll_opy_):
  try:
    bstack1llll1l1lll1_opy_ = config.get(bstack11ll1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ—"), False)
    if int(bstack1l1llll1ll_opy_) < len(config.get(bstack11ll1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ―"), [])) and config[bstack11ll1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭‖")][bstack1l1llll1ll_opy_]:
      bstack1llll1l1ll11_opy_ = config[bstack11ll1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ‗")][bstack1l1llll1ll_opy_].get(bstack11ll1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ‘"), None)
    else:
      bstack1llll1l1ll11_opy_ = config.get(bstack11ll1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭’"), None)
    if bstack1llll1l1ll11_opy_ != None:
      bstack1llll1l1lll1_opy_ = bstack1llll1l1ll11_opy_
    bstack1llll1l11ll1_opy_ = os.getenv(bstack11ll1l_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠬ‚")) is not None and len(os.getenv(bstack11ll1l_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭‛"))) > 0 and os.getenv(bstack11ll1l_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧ“")) != bstack11ll1l_opy_ (u"ࠪࡲࡺࡲ࡬ࠨ”")
    return bstack1llll1l1lll1_opy_ and bstack1llll1l11ll1_opy_
  except Exception as error:
    logger.debug(bstack11ll1l_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡺࡪࡸࡩࡧࡻ࡬ࡲ࡬ࠦࡴࡩࡧࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡷࡪࡹࡳࡪࡱࡱࠤࡼ࡯ࡴࡩࠢࡨࡶࡷࡵࡲࠡ࠼ࠣࠫ„") + str(error))
  return False
def bstack111l1ll11_opy_(test_tags):
  bstack1l111l1ll1l_opy_ = os.getenv(bstack11ll1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡡࡄࡇࡈࡋࡓࡔࡋࡅࡍࡑࡏࡔ࡚ࡡࡆࡓࡓࡌࡉࡈࡗࡕࡅ࡙ࡏࡏࡏࡡ࡜ࡑࡑ࠭‟"))
  if bstack1l111l1ll1l_opy_ is None:
    return True
  bstack1l111l1ll1l_opy_ = json.loads(bstack1l111l1ll1l_opy_)
  try:
    include_tags = bstack1l111l1ll1l_opy_[bstack11ll1l_opy_ (u"࠭ࡩ࡯ࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫ†")] if bstack11ll1l_opy_ (u"ࠧࡪࡰࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩࠬ‡") in bstack1l111l1ll1l_opy_ and isinstance(bstack1l111l1ll1l_opy_[bstack11ll1l_opy_ (u"ࠨ࡫ࡱࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ࠭•")], list) else []
    exclude_tags = bstack1l111l1ll1l_opy_[bstack11ll1l_opy_ (u"ࠩࡨࡼࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧ‣")] if bstack11ll1l_opy_ (u"ࠪࡩࡽࡩ࡬ࡶࡦࡨࡘࡦ࡭ࡳࡊࡰࡗࡩࡸࡺࡩ࡯ࡩࡖࡧࡴࡶࡥࠨ․") in bstack1l111l1ll1l_opy_ and isinstance(bstack1l111l1ll1l_opy_[bstack11ll1l_opy_ (u"ࠫࡪࡾࡣ࡭ࡷࡧࡩ࡙ࡧࡧࡴࡋࡱࡘࡪࡹࡴࡪࡰࡪࡗࡨࡵࡰࡦࠩ‥")], list) else []
    excluded = any(tag in exclude_tags for tag in test_tags)
    included = len(include_tags) == 0 or any(tag in include_tags for tag in test_tags)
    return not excluded and included
  except Exception as error:
    logger.debug(bstack11ll1l_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡺࡦࡲࡩࡥࡣࡷ࡭ࡳ࡭ࠠࡵࡧࡶࡸࠥࡩࡡࡴࡧࠣࡪࡴࡸࠠࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡣࡧࡩࡳࡷ࡫ࠠࡴࡥࡤࡲࡳ࡯࡮ࡨ࠰ࠣࡉࡷࡸ࡯ࡳࠢ࠽ࠤࠧ…") + str(error))
  return False
def bstack1llll1l11l11_opy_(config, frameworkName, bstack1llll1ll11ll_opy_, bstack1llll1l11l1l_opy_):
  bstack1llll1ll1l11_opy_ = bstack111l1l11l1l_opy_(config)
  bstack1llll1lll1l1_opy_ = bstack111l111l1l1_opy_(config)
  if bstack1llll1ll1l11_opy_ is None or bstack1llll1lll1l1_opy_ is None:
    logger.error(bstack11ll1l_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡺ࡬࡮ࡲࡥࠡࡥࡵࡩࡦࡺࡩ࡯ࡩࠣࡸࡪࡹࡴࠡࡴࡸࡲࠥ࡬࡯ࡳࠢࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲ࠿ࠦࡍࡪࡵࡶ࡭ࡳ࡭ࠠࡢࡷࡷ࡬ࡪࡴࡴࡪࡥࡤࡸ࡮ࡵ࡮ࠡࡶࡲ࡯ࡪࡴࠧ‧"))
    return [None, None]
  try:
    settings = json.loads(os.getenv(bstack11ll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡣࡆࡉࡃࡆࡕࡖࡍࡇࡏࡌࡊࡖ࡜ࡣࡈࡕࡎࡇࡋࡊ࡙ࡗࡇࡔࡊࡑࡑࡣ࡞ࡓࡌࠨ "), bstack11ll1l_opy_ (u"ࠨࡽࢀࠫ ")))
    data = {
        bstack11ll1l_opy_ (u"ࠩࡳࡶࡴࡰࡥࡤࡶࡑࡥࡲ࡫ࠧ‪"): config[bstack11ll1l_opy_ (u"ࠪࡴࡷࡵࡪࡦࡥࡷࡒࡦࡳࡥࠨ‫")],
        bstack11ll1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧ‬"): config.get(bstack11ll1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ‭"), os.path.basename(os.getcwd())),
        bstack11ll1l_opy_ (u"࠭ࡳࡵࡣࡵࡸ࡙࡯࡭ࡦࠩ‮"): bstack1l111ll1_opy_(),
        bstack11ll1l_opy_ (u"ࠧࡥࡧࡶࡧࡷ࡯ࡰࡵ࡫ࡲࡲࠬ "): config.get(bstack11ll1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡄࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࠫ‰"), bstack11ll1l_opy_ (u"ࠩࠪ‱")),
        bstack11ll1l_opy_ (u"ࠪࡷࡴࡻࡲࡤࡧࠪ′"): {
            bstack11ll1l_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࡎࡢ࡯ࡨࠫ″"): frameworkName,
            bstack11ll1l_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡗࡧࡵࡷ࡮ࡵ࡮ࠨ‴"): bstack1llll1ll11ll_opy_,
            bstack11ll1l_opy_ (u"࠭ࡳࡥ࡭࡙ࡩࡷࡹࡩࡰࡰࠪ‵"): __version__,
            bstack11ll1l_opy_ (u"ࠧ࡭ࡣࡱ࡫ࡺࡧࡧࡦࠩ‶"): bstack11ll1l_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨ‷"),
            bstack11ll1l_opy_ (u"ࠩࡷࡩࡸࡺࡆࡳࡣࡰࡩࡼࡵࡲ࡬ࠩ‸"): bstack11ll1l_opy_ (u"ࠪࡷࡪࡲࡥ࡯࡫ࡸࡱࠬ‹"),
            bstack11ll1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡈࡵࡥࡲ࡫ࡷࡰࡴ࡮࡚ࡪࡸࡳࡪࡱࡱࠫ›"): bstack1llll1l11l1l_opy_
        },
        bstack11ll1l_opy_ (u"ࠬࡹࡥࡵࡶ࡬ࡲ࡬ࡹࠧ※"): settings,
        bstack11ll1l_opy_ (u"࠭ࡶࡦࡴࡶ࡭ࡴࡴࡃࡰࡰࡷࡶࡴࡲࠧ‼"): bstack1111lll1l11_opy_(),
        bstack11ll1l_opy_ (u"ࠧࡤ࡫ࡌࡲ࡫ࡵࠧ‽"): bstack1l1ll1l1ll_opy_(),
        bstack11ll1l_opy_ (u"ࠨࡪࡲࡷࡹࡏ࡮ࡧࡱࠪ‾"): get_host_info(),
        bstack11ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫ‿"): bstack11ll1l1l1_opy_(config)
    }
    headers = {
        bstack11ll1l_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱࡙ࡿࡰࡦࠩ⁀"): bstack11ll1l_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧ⁁"),
    }
    config = {
        bstack11ll1l_opy_ (u"ࠬࡧࡵࡵࡪࠪ⁂"): (bstack1llll1ll1l11_opy_, bstack1llll1lll1l1_opy_),
        bstack11ll1l_opy_ (u"࠭ࡨࡦࡣࡧࡩࡷࡹࠧ⁃"): headers
    }
    response = bstack1l1llllll_opy_(bstack11ll1l_opy_ (u"ࠧࡑࡑࡖࡘࠬ⁄"), bstack1llll1l1l1l1_opy_ + bstack11ll1l_opy_ (u"ࠨ࠱ࡹ࠶࠴ࡺࡥࡴࡶࡢࡶࡺࡴࡳࠨ⁅"), data, config)
    bstack1llll1llll1l_opy_ = response.json()
    if bstack1llll1llll1l_opy_[bstack11ll1l_opy_ (u"ࠩࡶࡹࡨࡩࡥࡴࡵࠪ⁆")]:
      parsed = json.loads(os.getenv(bstack11ll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚࡟ࡂࡅࡆࡉࡘ࡙ࡉࡃࡋࡏࡍ࡙࡟࡟ࡄࡑࡑࡊࡎࡍࡕࡓࡃࡗࡍࡔࡔ࡟࡚ࡏࡏࠫ⁇"), bstack11ll1l_opy_ (u"ࠫࢀࢃࠧ⁈")))
      parsed[bstack11ll1l_opy_ (u"ࠬࡹࡣࡢࡰࡱࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭⁉")] = bstack1llll1llll1l_opy_[bstack11ll1l_opy_ (u"࠭ࡤࡢࡶࡤࠫ⁊")][bstack11ll1l_opy_ (u"ࠧࡴࡥࡤࡲࡳ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨ⁋")]
      os.environ[bstack11ll1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡤࡇࡃࡄࡇࡖࡗࡎࡈࡉࡍࡋࡗ࡝ࡤࡉࡏࡏࡈࡌࡋ࡚ࡘࡁࡕࡋࡒࡒࡤ࡟ࡍࡍࠩ⁌")] = json.dumps(parsed)
      bstack1l1l111ll_opy_.bstack111lll11l_opy_(bstack1llll1llll1l_opy_[bstack11ll1l_opy_ (u"ࠩࡧࡥࡹࡧࠧ⁍")][bstack11ll1l_opy_ (u"ࠪࡷࡨࡸࡩࡱࡶࡶࠫ⁎")])
      bstack1l1l111ll_opy_.bstack1lllll111l1l_opy_(bstack1llll1llll1l_opy_[bstack11ll1l_opy_ (u"ࠫࡩࡧࡴࡢࠩ⁏")][bstack11ll1l_opy_ (u"ࠬࡩ࡯࡮࡯ࡤࡲࡩࡹࠧ⁐")])
      bstack1l1l111ll_opy_.store()
      return bstack1llll1llll1l_opy_[bstack11ll1l_opy_ (u"࠭ࡤࡢࡶࡤࠫ⁑")][bstack11ll1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡔࡰ࡭ࡨࡲࠬ⁒")], bstack1llll1llll1l_opy_[bstack11ll1l_opy_ (u"ࠨࡦࡤࡸࡦ࠭⁓")][bstack11ll1l_opy_ (u"ࠩ࡬ࡨࠬ⁔")]
    else:
      logger.error(bstack11ll1l_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡷࡩ࡫࡯ࡩࠥࡸࡵ࡯ࡰ࡬ࡲ࡬ࠦࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯࠼ࠣࠫ⁕") + bstack1llll1llll1l_opy_[bstack11ll1l_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ⁖")])
      if bstack1llll1llll1l_opy_[bstack11ll1l_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭⁗")] == bstack11ll1l_opy_ (u"࠭ࡉ࡯ࡸࡤࡰ࡮ࡪࠠࡤࡱࡱࡪ࡮࡭ࡵࡳࡣࡷ࡭ࡴࡴࠠࡱࡣࡶࡷࡪࡪ࠮ࠨ⁘"):
        for bstack1llll1llllll_opy_ in bstack1llll1llll1l_opy_[bstack11ll1l_opy_ (u"ࠧࡦࡴࡵࡳࡷࡹࠧ⁙")]:
          logger.error(bstack1llll1llllll_opy_[bstack11ll1l_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ⁚")])
      return None, None
  except Exception as error:
    logger.error(bstack11ll1l_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡽࡨࡪ࡮ࡨࠤࡨࡸࡥࡢࡶ࡬ࡲ࡬ࠦࡴࡦࡵࡷࠤࡷࡻ࡮ࠡࡨࡲࡶࠥࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮࠻ࠢࠥ⁛") +  str(error))
    return None, None
def bstack1llll1ll111l_opy_():
  if os.getenv(bstack11ll1l_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨ⁜")) is None:
    return {
        bstack11ll1l_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫ⁝"): bstack11ll1l_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫ⁞"),
        bstack11ll1l_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ "): bstack11ll1l_opy_ (u"ࠧࡃࡷ࡬ࡰࡩࠦࡣࡳࡧࡤࡸ࡮ࡵ࡮ࠡࡪࡤࡨࠥ࡬ࡡࡪ࡮ࡨࡨ࠳࠭⁠")
    }
  data = {bstack11ll1l_opy_ (u"ࠨࡧࡱࡨ࡙࡯࡭ࡦࠩ⁡"): bstack1l111ll1_opy_()}
  headers = {
      bstack11ll1l_opy_ (u"ࠩࡄࡹࡹ࡮࡯ࡳ࡫ࡽࡥࡹ࡯࡯࡯ࠩ⁢"): bstack11ll1l_opy_ (u"ࠪࡆࡪࡧࡲࡦࡴࠣࠫ⁣") + os.getenv(bstack11ll1l_opy_ (u"ࠦࡇ࡙࡟ࡂ࠳࠴࡝ࡤࡐࡗࡕࠤ⁤")),
      bstack11ll1l_opy_ (u"ࠬࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡔࡺࡲࡨࠫ⁥"): bstack11ll1l_opy_ (u"࠭ࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳࡯ࡹ࡯࡯ࠩ⁦")
  }
  response = bstack1l1llllll_opy_(bstack11ll1l_opy_ (u"ࠧࡑࡗࡗࠫ⁧"), bstack1llll1l1l1l1_opy_ + bstack11ll1l_opy_ (u"ࠨ࠱ࡷࡩࡸࡺ࡟ࡳࡷࡱࡷ࠴ࡹࡴࡰࡲࠪ⁨"), data, { bstack11ll1l_opy_ (u"ࠩ࡫ࡩࡦࡪࡥࡳࡵࠪ⁩"): headers })
  try:
    if response.status_code == 200:
      logger.info(bstack11ll1l_opy_ (u"ࠥࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡔࡦࡵࡷࠤࡗࡻ࡮ࠡ࡯ࡤࡶࡰ࡫ࡤࠡࡣࡶࠤࡨࡵ࡭ࡱ࡮ࡨࡸࡪࡪࠠࡢࡶࠣࠦ⁪") + bstack1l1l1ll1_opy_().isoformat() + bstack11ll1l_opy_ (u"ࠫ࡟࠭⁫"))
      return {bstack11ll1l_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬ⁬"): bstack11ll1l_opy_ (u"࠭ࡳࡶࡥࡦࡩࡸࡹࠧ⁭"), bstack11ll1l_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ⁮"): bstack11ll1l_opy_ (u"ࠨࠩ⁯")}
    else:
      response.raise_for_status()
  except requests.RequestException as error:
    logger.error(bstack11ll1l_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡽࡨࡪ࡮ࡨࠤࡲࡧࡲ࡬࡫ࡱ࡫ࠥࡩ࡯࡮ࡲ࡯ࡩࡹ࡯࡯࡯ࠢࡲࡪࠥࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡖࡨࡷࡹࠦࡒࡶࡰ࠽ࠤࠧ⁰") + str(error))
    return {
        bstack11ll1l_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪⁱ"): bstack11ll1l_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪ⁲"),
        bstack11ll1l_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭⁳"): str(error)
    }
def bstack1lllll111111_opy_(bstack1llll1l1llll_opy_):
    return re.match(bstack11ll1l_opy_ (u"ࡸࠧ࡟࡞ࡧ࠯࠭ࡢ࠮࡝ࡦ࠮࠭ࡄࠪࠧ⁴"), bstack1llll1l1llll_opy_.strip()) is not None
def bstack1111l11l1_opy_(caps, options, desired_capabilities={}, config=None):
    try:
        if options:
          bstack1llll1lll11l_opy_ = options.to_capabilities()
        elif desired_capabilities:
          bstack1llll1lll11l_opy_ = desired_capabilities
        else:
          bstack1llll1lll11l_opy_ = {}
        bstack1l1111lllll_opy_ = (bstack1llll1lll11l_opy_.get(bstack11ll1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡐࡤࡱࡪ࠭⁵"), bstack11ll1l_opy_ (u"ࠨࠩ⁶")).lower() or caps.get(bstack11ll1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡒࡦࡳࡥࠨ⁷"), bstack11ll1l_opy_ (u"ࠪࠫ⁸")).lower())
        if bstack1l1111lllll_opy_ == bstack11ll1l_opy_ (u"ࠫ࡮ࡵࡳࠨ⁹"):
            return True
        if bstack1l1111lllll_opy_ == bstack11ll1l_opy_ (u"ࠬࡧ࡮ࡥࡴࡲ࡭ࡩ࠭⁺"):
            bstack1l111l11l11_opy_ = str(float(caps.get(bstack11ll1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠨ⁻")) or bstack1llll1lll11l_opy_.get(bstack11ll1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨ⁼"), {}).get(bstack11ll1l_opy_ (u"ࠨࡱࡶ࡚ࡪࡸࡳࡪࡱࡱࠫ⁽"),bstack11ll1l_opy_ (u"ࠩࠪ⁾"))))
            if bstack1l1111lllll_opy_ == bstack11ll1l_opy_ (u"ࠪࡥࡳࡪࡲࡰ࡫ࡧࠫⁿ") and int(bstack1l111l11l11_opy_.split(bstack11ll1l_opy_ (u"ࠫ࠳࠭₀"))[0]) < float(bstack11l11ll111l_opy_):
                logger.warning(str(bstack11l11llll1l_opy_))
                return False
            return True
        bstack1l11111llll_opy_ = caps.get(bstack11ll1l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭₁"), {}).get(bstack11ll1l_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪࡔࡡ࡮ࡧࠪ₂"), caps.get(bstack11ll1l_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࠧ₃"), bstack11ll1l_opy_ (u"ࠨࠩ₄")))
        if bstack1l11111llll_opy_:
            logger.warning(bstack11ll1l_opy_ (u"ࠤࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡷࡪ࡮࡯ࠤࡷࡻ࡮ࠡࡱࡱࡰࡾࠦ࡯࡯ࠢࡇࡩࡸࡱࡴࡰࡲࠣࡦࡷࡵࡷࡴࡧࡵࡷ࠳ࠨ₅"))
            return False
        browser = caps.get(bstack11ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨ₆"), bstack11ll1l_opy_ (u"ࠫࠬ₇")).lower() or bstack1llll1lll11l_opy_.get(bstack11ll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪ₈"), bstack11ll1l_opy_ (u"࠭ࠧ₉")).lower()
        if browser != bstack11ll1l_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࠧ₊"):
            logger.warning(bstack11ll1l_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡽࡩ࡭࡮ࠣࡶࡺࡴࠠࡰࡰ࡯ࡽࠥࡵ࡮ࠡࡅ࡫ࡶࡴࡳࡥࠡࡤࡵࡳࡼࡹࡥࡳࡵ࠱ࠦ₋"))
            return False
        browser_version = caps.get(bstack11ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪ₌")) or caps.get(bstack11ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬ₍")) or bstack1llll1lll11l_opy_.get(bstack11ll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬ₎")) or bstack1llll1lll11l_opy_.get(bstack11ll1l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭₏"), {}).get(bstack11ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧₐ")) or bstack1llll1lll11l_opy_.get(bstack11ll1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨₑ"), {}).get(bstack11ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡹࡩࡷࡹࡩࡰࡰࠪₒ"))
        bstack1l11111ll1l_opy_ = bstack1llll1l1l11l_opy_.bstack1l111l1111l_opy_
        bstack1llll1ll1lll_opy_ = False
        if config is not None:
          bstack1llll1ll1lll_opy_ = bstack11ll1l_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭ₓ") in config and str(config[bstack11ll1l_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧₔ")]).lower() != bstack11ll1l_opy_ (u"ࠫ࡫ࡧ࡬ࡴࡧࠪₕ")
        if os.environ.get(bstack11ll1l_opy_ (u"ࠬࡏࡓࡠࡐࡒࡒࡤࡈࡓࡕࡃࡆࡏࡤࡏࡎࡇࡔࡄࡣࡆ࠷࠱࡚ࡡࡖࡉࡘ࡙ࡉࡐࡐࠪₖ"), bstack11ll1l_opy_ (u"࠭ࠧₗ")).lower() == bstack11ll1l_opy_ (u"ࠧࡵࡴࡸࡩࠬₘ") or bstack1llll1ll1lll_opy_:
          bstack1l11111ll1l_opy_ = bstack1llll1l1l11l_opy_.bstack1l111ll111l_opy_
        if browser_version and browser_version != bstack11ll1l_opy_ (u"ࠨ࡮ࡤࡸࡪࡹࡴࠨₙ") and int(browser_version.split(bstack11ll1l_opy_ (u"ࠩ࠱ࠫₚ"))[0]) <= bstack1l11111ll1l_opy_:
          logger.warning(bstack11ll1l1l_opy_ (u"ࠪࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡸ࡫࡯ࡰࠥࡸࡵ࡯ࠢࡲࡲࡱࡿࠠࡰࡰࠣࡇ࡭ࡸ࡯࡮ࡧࠣࡦࡷࡵࡷࡴࡧࡵࠤࡻ࡫ࡲࡴ࡫ࡲࡲࠥ࡭ࡲࡦࡣࡷࡩࡷࠦࡴࡩࡣࡱࠤࢀࡳࡩ࡯ࡡࡤ࠵࠶ࡿ࡟ࡴࡷࡳࡴࡴࡸࡴࡦࡦࡢࡧ࡭ࡸ࡯࡮ࡧࡢࡺࡪࡸࡳࡪࡱࡱࢁ࠳࠭ₛ"))
          return False
        if not options:
          bstack1l111l1l11l_opy_ = caps.get(bstack11ll1l_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩₜ")) or bstack1llll1lll11l_opy_.get(bstack11ll1l_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ₝"), {})
          if bstack11ll1l_opy_ (u"࠭࠭࠮ࡪࡨࡥࡩࡲࡥࡴࡵࠪ₞") in bstack1l111l1l11l_opy_.get(bstack11ll1l_opy_ (u"ࠧࡢࡴࡪࡷࠬ₟"), []):
              logger.warning(bstack11ll1l_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡽࡩ࡭࡮ࠣࡲࡴࡺࠠࡳࡷࡱࠤࡴࡴࠠ࡭ࡧࡪࡥࡨࡿࠠࡩࡧࡤࡨࡱ࡫ࡳࡴࠢࡰࡳࡩ࡫࠮ࠡࡕࡺ࡭ࡹࡩࡨࠡࡶࡲࠤࡳ࡫ࡷࠡࡪࡨࡥࡩࡲࡥࡴࡵࠣࡱࡴࡪࡥࠡࡱࡵࠤࡦࡼ࡯ࡪࡦࠣࡹࡸ࡯࡮ࡨࠢ࡫ࡩࡦࡪ࡬ࡦࡵࡶࠤࡲࡵࡤࡦ࠰ࠥ₠"))
              return False
        return True
    except Exception as error:
        logger.debug(bstack11ll1l_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡸࡤࡰ࡮ࡪࡡࡵࡧࠣࡥ࠶࠷ࡹࠡࡵࡸࡴࡵࡵࡲࡵࠢ࠽ࠦ₡") + str(error))
        return False
def set_capabilities(caps, config):
  try:
    bstack1l1l111l111_opy_ = config.get(bstack11ll1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪ₢"), {})
    bstack1l1l111l111_opy_[bstack11ll1l_opy_ (u"ࠫࡦࡻࡴࡩࡖࡲ࡯ࡪࡴࠧ₣")] = os.getenv(bstack11ll1l_opy_ (u"ࠬࡈࡓࡠࡃ࠴࠵࡞ࡥࡊࡘࡖࠪ₤"))
    bstack111l1l1ll11_opy_ = json.loads(os.getenv(bstack11ll1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡢࡅࡈࡉࡅࡔࡕࡌࡆࡎࡒࡉࡕ࡛ࡢࡇࡔࡔࡆࡊࡉࡘࡖࡆ࡚ࡉࡐࡐࡢ࡝ࡒࡒࠧ₥"), bstack11ll1l_opy_ (u"ࠧࡼࡿࠪ₦"))).get(bstack11ll1l_opy_ (u"ࠨࡵࡦࡥࡳࡴࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩ₧"))
    if not config[bstack11ll1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡑࡴࡲࡨࡺࡩࡴࡎࡣࡳࠫ₨")].get(bstack11ll1l_opy_ (u"ࠥࡥࡵࡶ࡟ࡢࡷࡷࡳࡲࡧࡴࡦࠤ₩")):
      if bstack11ll1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬ₪") in caps:
        caps[bstack11ll1l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭₫")][bstack11ll1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭€")] = bstack1l1l111l111_opy_
        caps[bstack11ll1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨ₭")][bstack11ll1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨ₮")][bstack11ll1l_opy_ (u"ࠩࡶࡧࡦࡴ࡮ࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪ₯")] = bstack111l1l1ll11_opy_
      else:
        caps[bstack11ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩ₰")] = bstack1l1l111l111_opy_
        caps[bstack11ll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪ₱")][bstack11ll1l_opy_ (u"ࠬࡹࡣࡢࡰࡱࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭₲")] = bstack111l1l1ll11_opy_
  except Exception as error:
    logger.debug(bstack11ll1l_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡺ࡬࡮ࡲࡥࠡࡵࡨࡸࡹ࡯࡮ࡨࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷ࠳ࠦࡅࡳࡴࡲࡶ࠿ࠦࠢ₳") +  str(error))
def bstack1l11llll1l_opy_(driver, bstack1llll1l1l1ll_opy_):
  try:
    setattr(driver, bstack11ll1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡁ࠲࠳ࡼࡗ࡭ࡵࡵ࡭ࡦࡖࡧࡦࡴࠧ₴"), True)
    session = driver.session_id
    if session:
      bstack1llll1llll11_opy_ = True
      current_url = driver.current_url
      try:
        url = urlparse(current_url)
      except Exception as e:
        bstack1llll1llll11_opy_ = False
      bstack1llll1llll11_opy_ = url.scheme in [bstack11ll1l_opy_ (u"ࠣࡪࡷࡸࡵࠨ₵"), bstack11ll1l_opy_ (u"ࠤ࡫ࡸࡹࡶࡳࠣ₶")]
      if bstack1llll1llll11_opy_:
        if bstack1llll1l1l1ll_opy_:
          logger.info(bstack11ll1l_opy_ (u"ࠥࡗࡪࡺࡵࡱࠢࡩࡳࡷࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡴࡦࡵࡷ࡭ࡳ࡭ࠠࡩࡣࡶࠤࡸࡺࡡࡳࡶࡨࡨ࠳ࠦࡁࡶࡶࡲࡱࡦࡺࡥࠡࡶࡨࡷࡹࠦࡣࡢࡵࡨࠤࡪࡾࡥࡤࡷࡷ࡭ࡴࡴࠠࡸ࡫࡯ࡰࠥࡨࡥࡨ࡫ࡱࠤࡲࡵ࡭ࡦࡰࡷࡥࡷ࡯࡬ࡺ࠰ࠥ₷"))
      return bstack1llll1l1l1ll_opy_
  except Exception as e:
    logger.error(bstack11ll1l_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡷࡹࡧࡲࡵ࡫ࡱ࡫ࠥࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡶࡧࡦࡴࠠࡧࡱࡵࠤࡹ࡮ࡩࡴࠢࡷࡩࡸࡺࠠࡤࡣࡶࡩ࠿ࠦࠢ₸") + str(e))
    return False
def bstack1lll111ll_opy_(driver, name, path):
  try:
    bstack1l11111lll1_opy_ = {
        bstack11ll1l_opy_ (u"ࠬࡺࡨࡕࡧࡶࡸࡗࡻ࡮ࡖࡷ࡬ࡨࠬ₹"): threading.current_thread().current_test_uuid,
        bstack11ll1l_opy_ (u"࠭ࡴࡩࡄࡸ࡭ࡱࡪࡕࡶ࡫ࡧࠫ₺"): os.environ.get(bstack11ll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬ₻"), bstack11ll1l_opy_ (u"ࠨࠩ₼")),
        bstack11ll1l_opy_ (u"ࠩࡷ࡬ࡏࡽࡴࡕࡱ࡮ࡩࡳ࠭₽"): os.environ.get(bstack11ll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢࡎ࡜࡚ࠧ₾"), bstack11ll1l_opy_ (u"ࠫࠬ₿"))
    }
    bstack1ll111l1l1l_opy_ = bstack1ll1l1lll_opy_.bstack1ll1l111ll1_opy_(EVENTS.bstack1ll1111lll_opy_.value)
    logger.debug(bstack11ll1l_opy_ (u"ࠬࡖࡥࡳࡨࡲࡶࡲ࡯࡮ࡨࠢࡶࡧࡦࡴࠠࡣࡧࡩࡳࡷ࡫ࠠࡴࡣࡹ࡭ࡳ࡭ࠠࡳࡧࡶࡹࡱࡺࡳࠨ⃀"))
    try:
      if (bstack1lllll11_opy_(threading.current_thread(), bstack11ll1l_opy_ (u"࠭ࡩࡴࡃࡳࡴࡆ࠷࠱ࡺࡖࡨࡷࡹ࠭⃁"), None) and bstack1lllll11_opy_(threading.current_thread(), bstack11ll1l_opy_ (u"ࠧࡢࡲࡳࡅ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩ⃂"), None)):
        scripts = {bstack11ll1l_opy_ (u"ࠨࡵࡦࡥࡳ࠭⃃"): bstack1l1l111ll_opy_.perform_scan}
        bstack1llll1l1ll1l_opy_ = json.loads(scripts[bstack11ll1l_opy_ (u"ࠤࡶࡧࡦࡴࠢ⃄")].replace(bstack11ll1l_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࠨ⃅"), bstack11ll1l_opy_ (u"ࠦࠧ⃆")))
        bstack1llll1l1ll1l_opy_[bstack11ll1l_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨ⃇")][bstack11ll1l_opy_ (u"࠭࡭ࡦࡶ࡫ࡳࡩ࠭⃈")] = None
        scripts[bstack11ll1l_opy_ (u"ࠢࡴࡥࡤࡲࠧ⃉")] = bstack11ll1l_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࠦ⃊") + json.dumps(bstack1llll1l1ll1l_opy_)
        bstack1l1l111ll_opy_.bstack111lll11l_opy_(scripts)
        bstack1l1l111ll_opy_.store()
        logger.debug(driver.execute_script(bstack1l1l111ll_opy_.perform_scan))
      else:
        logger.debug(driver.execute_async_script(bstack1l1l111ll_opy_.perform_scan, {bstack11ll1l_opy_ (u"ࠤࡰࡩࡹ࡮࡯ࡥࠤ⃋"): name}))
      bstack1ll1l1lll_opy_.end(EVENTS.bstack1ll1111lll_opy_.value, bstack1ll111l1l1l_opy_ + bstack11ll1l_opy_ (u"ࠥ࠾ࡸࡺࡡࡳࡶࠥ⃌"), bstack1ll111l1l1l_opy_ + bstack11ll1l_opy_ (u"ࠦ࠿࡫࡮ࡥࠤ⃍"), True, None)
    except Exception as error:
      bstack1ll1l1lll_opy_.end(EVENTS.bstack1ll1111lll_opy_.value, bstack1ll111l1l1l_opy_ + bstack11ll1l_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧ⃎"), bstack1ll111l1l1l_opy_ + bstack11ll1l_opy_ (u"ࠨ࠺ࡦࡰࡧࠦ⃏"), False, str(error))
    bstack1ll111l1l1l_opy_ = bstack1ll1l1lll_opy_.bstack11ll1l11l11_opy_(EVENTS.bstack1l111l1ll11_opy_.value)
    bstack1ll1l1lll_opy_.mark(bstack1ll111l1l1l_opy_ + bstack11ll1l_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢ⃐"))
    try:
      if (bstack1lllll11_opy_(threading.current_thread(), bstack11ll1l_opy_ (u"ࠨ࡫ࡶࡅࡵࡶࡁ࠲࠳ࡼࡘࡪࡹࡴࠨ⃑"), None) and bstack1lllll11_opy_(threading.current_thread(), bstack11ll1l_opy_ (u"ࠩࡤࡴࡵࡇ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰ⃒ࠫ"), None)):
        scripts = {bstack11ll1l_opy_ (u"ࠪࡷࡨࡧ࡮ࠨ⃓"): bstack1l1l111ll_opy_.perform_scan}
        bstack1llll1l1ll1l_opy_ = json.loads(scripts[bstack11ll1l_opy_ (u"ࠦࡸࡩࡡ࡯ࠤ⃔")].replace(bstack11ll1l_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࠣ⃕"), bstack11ll1l_opy_ (u"ࠨࠢ⃖")))
        bstack1llll1l1ll1l_opy_[bstack11ll1l_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪ⃗")][bstack11ll1l_opy_ (u"ࠨ࡯ࡨࡸ࡭ࡵࡤࠨ⃘")] = None
        scripts[bstack11ll1l_opy_ (u"ࠤࡶࡧࡦࡴ⃙ࠢ")] = bstack11ll1l_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࠨ⃚") + json.dumps(bstack1llll1l1ll1l_opy_)
        bstack1l1l111ll_opy_.bstack111lll11l_opy_(scripts)
        bstack1l1l111ll_opy_.store()
        logger.debug(driver.execute_script(bstack1l1l111ll_opy_.perform_scan))
      else:
        logger.debug(driver.execute_async_script(bstack1l1l111ll_opy_.bstack1lllll11111l_opy_, bstack1l11111lll1_opy_))
      bstack1ll1l1lll_opy_.end(bstack1ll111l1l1l_opy_, bstack1ll111l1l1l_opy_ + bstack11ll1l_opy_ (u"ࠦ࠿ࡹࡴࡢࡴࡷࠦ⃛"), bstack1ll111l1l1l_opy_ + bstack11ll1l_opy_ (u"ࠧࡀࡥ࡯ࡦࠥ⃜"),True, None)
    except Exception as error:
      bstack1ll1l1lll_opy_.end(bstack1ll111l1l1l_opy_, bstack1ll111l1l1l_opy_ + bstack11ll1l_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨ⃝"), bstack1ll111l1l1l_opy_ + bstack11ll1l_opy_ (u"ࠢ࠻ࡧࡱࡨࠧ⃞"),False, str(error))
    logger.info(bstack11ll1l_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡶࡨࡷࡹ࡯࡮ࡨࠢࡩࡳࡷࠦࡴࡩ࡫ࡶࠤࡹ࡫ࡳࡵࠢࡦࡥࡸ࡫ࠠࡩࡣࡶࠤࡪࡴࡤࡦࡦ࠱ࠦ⃟"))
  except Exception as bstack1l11111l11l_opy_:
    logger.error(bstack11ll1l_opy_ (u"ࠤࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡵࡩࡸࡻ࡬ࡵࡵࠣࡧࡴࡻ࡬ࡥࠢࡱࡳࡹࠦࡢࡦࠢࡳࡶࡴࡩࡥࡴࡵࡨࡨࠥ࡬࡯ࡳࠢࡷ࡬ࡪࠦࡴࡦࡵࡷࠤࡨࡧࡳࡦ࠼ࠣࠦ⃠") + str(path) + bstack11ll1l_opy_ (u"ࠥࠤࡊࡸࡲࡰࡴࠣ࠾ࠧ⃡") + str(bstack1l11111l11l_opy_))
def bstack1llll1ll1111_opy_(driver):
    caps = driver.capabilities
    if caps.get(bstack11ll1l_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲࡔࡡ࡮ࡧࠥ⃢")) and str(caps.get(bstack11ll1l_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࡎࡢ࡯ࡨࠦ⃣"))).lower() == bstack11ll1l_opy_ (u"ࠨࡡ࡯ࡦࡵࡳ࡮ࡪࠢ⃤"):
        bstack1l111l11l11_opy_ = caps.get(bstack11ll1l_opy_ (u"ࠢࡢࡲࡳ࡭ࡺࡳ࠺ࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠤ⃥")) or caps.get(bstack11ll1l_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࡙ࡩࡷࡹࡩࡰࡰ⃦ࠥ"))
        if bstack1l111l11l11_opy_ and int(str(bstack1l111l11l11_opy_)) < bstack11l11ll111l_opy_:
            return False
    return True
def bstack111l1111l_opy_(config):
  if bstack11ll1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ⃧") in config:
        return config[bstack11ll1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻ⃨ࠪ")]
  for platform in config.get(bstack11ll1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ⃩"), []):
      if bstack11ll1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽ⃪ࠬ") in platform:
          return platform[bstack11ll1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ⃫࠭")]
  return None
def bstack1l11111l1l_opy_(bstack11ll1ll1l1_opy_):
  try:
    browser_name = bstack11ll1ll1l1_opy_[bstack11ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡰࡤࡱࡪ⃬࠭")]
    browser_version = bstack11ll1ll1l1_opy_[bstack11ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡹࡩࡷࡹࡩࡰࡰ⃭ࠪ")]
    chrome_options = bstack11ll1ll1l1_opy_[bstack11ll1l_opy_ (u"ࠩࡦ࡬ࡷࡵ࡭ࡦࡡࡲࡴࡹ࡯࡯࡯ࡵ⃮ࠪ")]
    try:
        bstack1llll1lll111_opy_ = int(browser_version.split(bstack11ll1l_opy_ (u"ࠪ࠲⃯ࠬ"))[0])
    except ValueError as e:
        logger.error(bstack11ll1l_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡯࡬ࡦࠢࡦࡳࡳࡼࡥࡳࡶ࡬ࡲ࡬ࠦࡢࡳࡱࡺࡷࡪࡸࠠࡷࡧࡵࡷ࡮ࡵ࡮ࠣ⃰") + str(e))
        return False
    if not (browser_name and browser_name.lower() == bstack11ll1l_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࠬ⃱")):
        logger.warning(bstack11ll1l_opy_ (u"ࠨࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡻ࡮ࡲ࡬ࠡࡴࡸࡲࠥࡵ࡮࡭ࡻࠣࡳࡳࠦࡃࡩࡴࡲࡱࡪࠦࡢࡳࡱࡺࡷࡪࡸࡳ࠯ࠤ⃲"))
        return False
    if bstack1llll1lll111_opy_ < bstack1llll1l1l11l_opy_.bstack1l111ll111l_opy_:
        logger.warning(bstack11ll1l1l_opy_ (u"ࠧࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡷ࡫ࡱࡶ࡫ࡵࡩࡸࠦࡃࡩࡴࡲࡱࡪࠦࡶࡦࡴࡶ࡭ࡴࡴࠠࡼࡅࡒࡒࡘ࡚ࡁࡏࡖࡖ࠲ࡒࡏࡎࡊࡏࡘࡑࡤࡔࡏࡏࡡࡅࡗ࡙ࡇࡃࡌࡡࡌࡒࡋࡘࡁࡠࡃ࠴࠵࡞ࡥࡓࡖࡒࡓࡓࡗ࡚ࡅࡅࡡࡆࡌࡗࡕࡍࡆࡡ࡙ࡉࡗ࡙ࡉࡐࡐࢀࠤࡴࡸࠠࡩ࡫ࡪ࡬ࡪࡸ࠮ࠨ⃳"))
        return False
    if chrome_options and any(bstack11ll1l_opy_ (u"ࠨ࠯࠰࡬ࡪࡧࡤ࡭ࡧࡶࡷࠬ⃴") in value for value in chrome_options.values() if isinstance(value, str)):
        logger.warning(bstack11ll1l_opy_ (u"ࠤࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡷࡪ࡮࡯ࠤࡳࡵࡴࠡࡴࡸࡲࠥࡵ࡮ࠡ࡮ࡨ࡫ࡦࡩࡹࠡࡪࡨࡥࡩࡲࡥࡴࡵࠣࡱࡴࡪࡥ࠯ࠢࡖࡻ࡮ࡺࡣࡩࠢࡷࡳࠥࡴࡥࡸࠢ࡫ࡩࡦࡪ࡬ࡦࡵࡶࠤࡲࡵࡤࡦࠢࡲࡶࠥࡧࡶࡰ࡫ࡧࠤࡺࡹࡩ࡯ࡩࠣ࡬ࡪࡧࡤ࡭ࡧࡶࡷࠥࡳ࡯ࡥࡧ࠱ࠦ⃵"))
        return False
    return True
  except Exception as e:
    logger.error(bstack11ll1l_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡩࡨࡦࡥ࡮࡭ࡳ࡭ࠠࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࠢࡶࡹࡵࡶ࡯ࡳࡶࠣࡪࡴࡸࠠ࡭ࡱࡦࡥࡱࠦࡃࡩࡴࡲࡱࡪࡀࠠࠣ⃶") + str(e))
    return False
def bstack1llll1l11l_opy_(bstack11lll1ll1_opy_, config):
    try:
      bstack1l1111ll11l_opy_ = bstack11ll1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ⃷") in config and config[bstack11ll1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ⃸")] == True
      bstack1llll1ll1lll_opy_ = bstack11ll1l_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪ⃹") in config and str(config[bstack11ll1l_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫ⃺")]).lower() != bstack11ll1l_opy_ (u"ࠨࡨࡤࡰࡸ࡫ࠧ⃻")
      if not (bstack1l1111ll11l_opy_ and (not bstack11ll1l1l1_opy_(config) or bstack1llll1ll1lll_opy_)):
        return bstack11lll1ll1_opy_
      bstack1llll1l1l111_opy_ = bstack1l1l111ll_opy_.bstack1lllll111ll1_opy_
      if bstack1llll1l1l111_opy_ is None:
        logger.debug(bstack11ll1l_opy_ (u"ࠤࡊࡳࡴ࡭࡬ࡦࠢࡦ࡬ࡷࡵ࡭ࡦࠢࡲࡴࡹ࡯࡯࡯ࡵࠣࡥࡷ࡫ࠠࡏࡱࡱࡩࠧ⃼"))
        return bstack11lll1ll1_opy_
      bstack1llll1ll1ll1_opy_ = int(str(bstack111l1111l1l_opy_()).split(bstack11ll1l_opy_ (u"ࠪ࠲ࠬ⃽"))[0])
      logger.debug(bstack11ll1l_opy_ (u"ࠦࡘ࡫࡬ࡦࡰ࡬ࡹࡲࠦࡶࡦࡴࡶ࡭ࡴࡴࠠࡥࡧࡷࡩࡨࡺࡥࡥ࠼ࠣࠦ⃾") + str(bstack1llll1ll1ll1_opy_) + bstack11ll1l_opy_ (u"ࠧࠨ⃿"))
      if bstack1llll1ll1ll1_opy_ == 3 and isinstance(bstack11lll1ll1_opy_, dict) and bstack11ll1l_opy_ (u"࠭ࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠭℀") in bstack11lll1ll1_opy_ and bstack1llll1l1l111_opy_ is not None:
        if bstack11ll1l_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬ℁") not in bstack11lll1ll1_opy_[bstack11ll1l_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨℂ")]:
          bstack11lll1ll1_opy_[bstack11ll1l_opy_ (u"ࠩࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩ℃")][bstack11ll1l_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨ℄")] = {}
        if bstack11ll1l_opy_ (u"ࠫࡦࡸࡧࡴࠩ℅") in bstack1llll1l1l111_opy_:
          if bstack11ll1l_opy_ (u"ࠬࡧࡲࡨࡵࠪ℆") not in bstack11lll1ll1_opy_[bstack11ll1l_opy_ (u"࠭ࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠭ℇ")][bstack11ll1l_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬ℈")]:
            bstack11lll1ll1_opy_[bstack11ll1l_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨ℉")][bstack11ll1l_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧℊ")][bstack11ll1l_opy_ (u"ࠪࡥࡷ࡭ࡳࠨℋ")] = []
          for arg in bstack1llll1l1l111_opy_[bstack11ll1l_opy_ (u"ࠫࡦࡸࡧࡴࠩℌ")]:
            if arg not in bstack11lll1ll1_opy_[bstack11ll1l_opy_ (u"ࠬࡪࡥࡴ࡫ࡵࡩࡩࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠬℍ")][bstack11ll1l_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫℎ")][bstack11ll1l_opy_ (u"ࠧࡢࡴࡪࡷࠬℏ")]:
              bstack11lll1ll1_opy_[bstack11ll1l_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨℐ")][bstack11ll1l_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧℑ")][bstack11ll1l_opy_ (u"ࠪࡥࡷ࡭ࡳࠨℒ")].append(arg)
        if bstack11ll1l_opy_ (u"ࠫࡪࡾࡴࡦࡰࡶ࡭ࡴࡴࡳࠨℓ") in bstack1llll1l1l111_opy_:
          if bstack11ll1l_opy_ (u"ࠬ࡫ࡸࡵࡧࡱࡷ࡮ࡵ࡮ࡴࠩ℔") not in bstack11lll1ll1_opy_[bstack11ll1l_opy_ (u"࠭ࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠭ℕ")][bstack11ll1l_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬ№")]:
            bstack11lll1ll1_opy_[bstack11ll1l_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨ℗")][bstack11ll1l_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ℘")][bstack11ll1l_opy_ (u"ࠪࡩࡽࡺࡥ࡯ࡵ࡬ࡳࡳࡹࠧℙ")] = []
          for ext in bstack1llll1l1l111_opy_[bstack11ll1l_opy_ (u"ࠫࡪࡾࡴࡦࡰࡶ࡭ࡴࡴࡳࠨℚ")]:
            if ext not in bstack11lll1ll1_opy_[bstack11ll1l_opy_ (u"ࠬࡪࡥࡴ࡫ࡵࡩࡩࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠬℛ")][bstack11ll1l_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫℜ")][bstack11ll1l_opy_ (u"ࠧࡦࡺࡷࡩࡳࡹࡩࡰࡰࡶࠫℝ")]:
              bstack11lll1ll1_opy_[bstack11ll1l_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨ℞")][bstack11ll1l_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ℟")][bstack11ll1l_opy_ (u"ࠪࡩࡽࡺࡥ࡯ࡵ࡬ࡳࡳࡹࠧ℠")].append(ext)
        if bstack11ll1l_opy_ (u"ࠫࡵࡸࡥࡧࡵࠪ℡") in bstack1llll1l1l111_opy_:
          if bstack11ll1l_opy_ (u"ࠬࡶࡲࡦࡨࡶࠫ™") not in bstack11lll1ll1_opy_[bstack11ll1l_opy_ (u"࠭ࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠭℣")][bstack11ll1l_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬℤ")]:
            bstack11lll1ll1_opy_[bstack11ll1l_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨ℥")][bstack11ll1l_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧΩ")][bstack11ll1l_opy_ (u"ࠪࡴࡷ࡫ࡦࡴࠩ℧")] = {}
          bstack1111l11l111_opy_(bstack11lll1ll1_opy_[bstack11ll1l_opy_ (u"ࠫࡩ࡫ࡳࡪࡴࡨࡨࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠫℨ")][bstack11ll1l_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ℩")][bstack11ll1l_opy_ (u"࠭ࡰࡳࡧࡩࡷࠬK")],
                    bstack1llll1l1l111_opy_[bstack11ll1l_opy_ (u"ࠧࡱࡴࡨࡪࡸ࠭Å")])
        os.environ[bstack11ll1l_opy_ (u"ࠨࡋࡖࡣࡓࡕࡎࡠࡄࡖࡘࡆࡉࡋࡠࡋࡑࡊࡗࡇ࡟ࡂ࠳࠴࡝ࡤ࡙ࡅࡔࡕࡌࡓࡓ࠭ℬ")] = bstack11ll1l_opy_ (u"ࠩࡷࡶࡺ࡫ࠧℭ")
        return bstack11lll1ll1_opy_
      else:
        chrome_options = None
        if isinstance(bstack11lll1ll1_opy_, ChromeOptions):
          chrome_options = bstack11lll1ll1_opy_
        elif isinstance(bstack11lll1ll1_opy_, dict):
          for value in bstack11lll1ll1_opy_.values():
            if isinstance(value, ChromeOptions):
              chrome_options = value
              break
        if chrome_options is None:
          chrome_options = ChromeOptions()
          if isinstance(bstack11lll1ll1_opy_, dict):
            bstack11lll1ll1_opy_[bstack11ll1l_opy_ (u"ࠪࡳࡵࡺࡩࡰࡰࡶࠫ℮")] = chrome_options
          else:
            bstack11lll1ll1_opy_ = chrome_options
        if bstack1llll1l1l111_opy_ is not None:
          if bstack11ll1l_opy_ (u"ࠫࡦࡸࡧࡴࠩℯ") in bstack1llll1l1l111_opy_:
                bstack1llll1lllll1_opy_ = chrome_options.arguments or []
                new_args = bstack1llll1l1l111_opy_[bstack11ll1l_opy_ (u"ࠬࡧࡲࡨࡵࠪℰ")]
                for arg in new_args:
                    if arg not in bstack1llll1lllll1_opy_:
                        chrome_options.add_argument(arg)
          if bstack11ll1l_opy_ (u"࠭ࡥࡹࡶࡨࡲࡸ࡯࡯࡯ࡵࠪℱ") in bstack1llll1l1l111_opy_:
                existing_extensions = chrome_options.experimental_options.get(bstack11ll1l_opy_ (u"ࠧࡦࡺࡷࡩࡳࡹࡩࡰࡰࡶࠫℲ"), [])
                bstack1llll1ll1l1l_opy_ = bstack1llll1l1l111_opy_[bstack11ll1l_opy_ (u"ࠨࡧࡻࡸࡪࡴࡳࡪࡱࡱࡷࠬℳ")]
                for extension in bstack1llll1ll1l1l_opy_:
                    if extension not in existing_extensions:
                        chrome_options.add_encoded_extension(extension)
          if bstack11ll1l_opy_ (u"ࠩࡳࡶࡪ࡬ࡳࠨℴ") in bstack1llll1l1l111_opy_:
                bstack1llll1ll11l1_opy_ = chrome_options.experimental_options.get(bstack11ll1l_opy_ (u"ࠪࡴࡷ࡫ࡦࡴࠩℵ"), {})
                bstack1llll1l11lll_opy_ = bstack1llll1l1l111_opy_[bstack11ll1l_opy_ (u"ࠫࡵࡸࡥࡧࡵࠪℶ")]
                bstack1111l11l111_opy_(bstack1llll1ll11l1_opy_, bstack1llll1l11lll_opy_)
                chrome_options.add_experimental_option(bstack11ll1l_opy_ (u"ࠬࡶࡲࡦࡨࡶࠫℷ"), bstack1llll1ll11l1_opy_)
        os.environ[bstack11ll1l_opy_ (u"࠭ࡉࡔࡡࡑࡓࡓࡥࡂࡔࡖࡄࡇࡐࡥࡉࡏࡈࡕࡅࡤࡇ࠱࠲࡛ࡢࡗࡊ࡙ࡓࡊࡑࡑࠫℸ")] = bstack11ll1l_opy_ (u"ࠧࡵࡴࡸࡩࠬℹ")
        return bstack11lll1ll1_opy_
    except Exception as e:
      logger.error(bstack11ll1l_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡸࡪ࡬ࡰࡪࠦࡡࡥࡦ࡬ࡲ࡬ࠦ࡮ࡰࡰ࠰ࡆࡘࠦࡩ࡯ࡨࡵࡥࠥࡧ࠱࠲ࡻࠣࡧ࡭ࡸ࡯࡮ࡧࠣࡳࡵࡺࡩࡰࡰࡶ࠾ࠥࠨ℺") + str(e))
      return bstack11lll1ll1_opy_