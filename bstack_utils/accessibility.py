# coding: UTF-8
import sys
bstack111ll1_opy_ = sys.version_info [0] == 2
bstack1l11l1_opy_ = 2048
bstack11111l_opy_ = 7
def bstack1ll1ll1_opy_ (bstack11lll1l_opy_):
    global bstack1ll11l1_opy_
    bstack1l1ll_opy_ = ord (bstack11lll1l_opy_ [-1])
    bstack1ll1l1l_opy_ = bstack11lll1l_opy_ [:-1]
    bstack1l1l1ll_opy_ = bstack1l1ll_opy_ % len (bstack1ll1l1l_opy_)
    bstack11ll1ll_opy_ = bstack1ll1l1l_opy_ [:bstack1l1l1ll_opy_] + bstack1ll1l1l_opy_ [bstack1l1l1ll_opy_:]
    if bstack111ll1_opy_:
        bstack111ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11l1_opy_ - (bstack111111l_opy_ + bstack1l1ll_opy_) % bstack11111l_opy_) for bstack111111l_opy_, char in enumerate (bstack11ll1ll_opy_)])
    else:
        bstack111ll_opy_ = str () .join ([chr (ord (char) - bstack1l11l1_opy_ - (bstack111111l_opy_ + bstack1l1ll_opy_) % bstack11111l_opy_) for bstack111111l_opy_, char in enumerate (bstack11ll1ll_opy_)])
    return eval (bstack111ll_opy_)
import os
import json
import requests
import logging
import threading
import bstack_utils.constants as bstack1llll1ll11ll_opy_
from urllib.parse import urlparse
from bstack_utils.constants import bstack11l1l1l11ll_opy_ as bstack1llll1ll1lll_opy_, EVENTS
from bstack_utils.bstack111llll111_opy_ import bstack111llll111_opy_
from bstack_utils.helper import bstack1l11l1ll_opy_, bstack1l1l1l11_opy_, bstack11l1l111ll_opy_, bstack111l11l11ll_opy_, \
  bstack1111l1ll1ll_opy_, bstack1l1l111l11_opy_, get_host_info, bstack111l111ll1l_opy_, bstack111l1l11l1_opy_, error_handler, bstack1111ll1ll1l_opy_, bstack111l1l1l1ll_opy_, bstack1l1lll11_opy_
from browserstack_sdk._version import __version__
from bstack_utils.bstack1l1l1ll111_opy_ import get_logger
from bstack_utils.bstack111l11l1ll_opy_ import bstack1lllll1l11l_opy_
from selenium.webdriver.chrome.options import Options as ChromeOptions
from browserstack_sdk.sdk_cli.cli import cli
from bstack_utils.constants import *
logger = get_logger(__name__)
bstack111l11l1ll_opy_ = bstack1lllll1l11l_opy_()
@error_handler(class_method=False)
def _1lllll11l11l_opy_(driver, bstack1lllll111_opy_):
  response = {}
  try:
    caps = driver.capabilities
    response = {
        bstack1ll1ll1_opy_ (u"ࠪࡳࡸࡥ࡮ࡢ࡯ࡨࠫΈ"): caps.get(bstack1ll1ll1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡔࡡ࡮ࡧࠪῊ"), None),
        bstack1ll1ll1_opy_ (u"ࠬࡵࡳࡠࡸࡨࡶࡸ࡯࡯࡯ࠩΉ"): bstack1lllll111_opy_.get(bstack1ll1ll1_opy_ (u"࠭࡯ࡴࡘࡨࡶࡸ࡯࡯࡯ࠩῌ"), None),
        bstack1ll1ll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡰࡤࡱࡪ࠭῍"): caps.get(bstack1ll1ll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭῎"), None),
        bstack1ll1ll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡺࡪࡸࡳࡪࡱࡱࠫ῏"): caps.get(bstack1ll1ll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫῐ"), None)
    }
  except Exception as error:
    logger.debug(bstack1ll1ll1_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡪࡪࡺࡣࡩ࡫ࡱ࡫ࠥࡶ࡬ࡢࡶࡩࡳࡷࡳࠠࡥࡧࡷࡥ࡮ࡲࡳࠡࡹ࡬ࡸ࡭ࠦࡥࡳࡴࡲࡶࠥࡀࠠࠨῑ") + str(error))
  return response
def on():
    if os.environ.get(bstack1ll1ll1_opy_ (u"ࠬࡈࡓࡠࡃ࠴࠵࡞ࡥࡊࡘࡖࠪῒ"), None) is None or os.environ[bstack1ll1ll1_opy_ (u"࠭ࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗࠫΐ")] == bstack1ll1ll1_opy_ (u"ࠢ࡯ࡷ࡯ࡰࠧ῔"):
        return False
    return True
def bstack11ll1lll1_opy_(config):
  return config.get(bstack1ll1ll1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ῕"), False) or any([p.get(bstack1ll1ll1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩῖ"), False) == True for p in config.get(bstack1ll1ll1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ῗ"), [])])
def bstack1ll1lll111_opy_(config, bstack1l1lll111l_opy_):
  try:
    bstack1llll1ll1ll1_opy_ = config.get(bstack1ll1ll1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫῘ"), False)
    if int(bstack1l1lll111l_opy_) < len(config.get(bstack1ll1ll1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨῙ"), [])) and config[bstack1ll1ll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩῚ")][bstack1l1lll111l_opy_]:
      bstack1lllll11ll1l_opy_ = config[bstack1ll1ll1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪΊ")][bstack1l1lll111l_opy_].get(bstack1ll1ll1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ῜"), None)
    else:
      bstack1lllll11ll1l_opy_ = config.get(bstack1ll1ll1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ῝"), None)
    if bstack1lllll11ll1l_opy_ != None:
      bstack1llll1ll1ll1_opy_ = bstack1lllll11ll1l_opy_
    bstack1llll1llllll_opy_ = os.getenv(bstack1ll1ll1_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨ῞")) is not None and len(os.getenv(bstack1ll1ll1_opy_ (u"ࠫࡇ࡙࡟ࡂ࠳࠴࡝ࡤࡐࡗࡕࠩ῟"))) > 0 and os.getenv(bstack1ll1ll1_opy_ (u"ࠬࡈࡓࡠࡃ࠴࠵࡞ࡥࡊࡘࡖࠪῠ")) != bstack1ll1ll1_opy_ (u"࠭࡮ࡶ࡮࡯ࠫῡ")
    return bstack1llll1ll1ll1_opy_ and bstack1llll1llllll_opy_
  except Exception as error:
    logger.debug(bstack1ll1ll1_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡶࡦࡴ࡬ࡪࡾ࡯࡮ࡨࠢࡷ࡬ࡪࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡳࡦࡵࡶ࡭ࡴࡴࠠࡸ࡫ࡷ࡬ࠥ࡫ࡲࡳࡱࡵࠤ࠿ࠦࠧῢ") + str(error))
  return False
def bstack111llllll_opy_(test_tags):
  bstack1l111ll111l_opy_ = os.getenv(bstack1ll1ll1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡤࡇࡃࡄࡇࡖࡗࡎࡈࡉࡍࡋࡗ࡝ࡤࡉࡏࡏࡈࡌࡋ࡚ࡘࡁࡕࡋࡒࡒࡤ࡟ࡍࡍࠩΰ"))
  if bstack1l111ll111l_opy_ is None:
    return True
  bstack1l111ll111l_opy_ = json.loads(bstack1l111ll111l_opy_)
  try:
    include_tags = bstack1l111ll111l_opy_[bstack1ll1ll1_opy_ (u"ࠩ࡬ࡲࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧῤ")] if bstack1ll1ll1_opy_ (u"ࠪ࡭ࡳࡩ࡬ࡶࡦࡨࡘࡦ࡭ࡳࡊࡰࡗࡩࡸࡺࡩ࡯ࡩࡖࡧࡴࡶࡥࠨῥ") in bstack1l111ll111l_opy_ and isinstance(bstack1l111ll111l_opy_[bstack1ll1ll1_opy_ (u"ࠫ࡮ࡴࡣ࡭ࡷࡧࡩ࡙ࡧࡧࡴࡋࡱࡘࡪࡹࡴࡪࡰࡪࡗࡨࡵࡰࡦࠩῦ")], list) else []
    exclude_tags = bstack1l111ll111l_opy_[bstack1ll1ll1_opy_ (u"ࠬ࡫ࡸࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪῧ")] if bstack1ll1ll1_opy_ (u"࠭ࡥࡹࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫῨ") in bstack1l111ll111l_opy_ and isinstance(bstack1l111ll111l_opy_[bstack1ll1ll1_opy_ (u"ࠧࡦࡺࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩࠬῩ")], list) else []
    excluded = any(tag in exclude_tags for tag in test_tags)
    included = len(include_tags) == 0 or any(tag in include_tags for tag in test_tags)
    return not excluded and included
  except Exception as error:
    logger.debug(bstack1ll1ll1_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡸࡪ࡬ࡰࡪࠦࡶࡢ࡮࡬ࡨࡦࡺࡩ࡯ࡩࠣࡸࡪࡹࡴࠡࡥࡤࡷࡪࠦࡦࡰࡴࠣࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡦࡪ࡬࡯ࡳࡧࠣࡷࡨࡧ࡮࡯࡫ࡱ࡫࠳ࠦࡅࡳࡴࡲࡶࠥࡀࠠࠣῪ") + str(error))
  return False
def bstack1lllll11l1l1_opy_(config, frameworkName, bstack1llll1llll11_opy_, bstack1lllll11llll_opy_):
  bstack1llll1lll1l1_opy_ = bstack111l11l11ll_opy_(config)
  bstack1llll1lll11l_opy_ = bstack1111l1ll1ll_opy_(config)
  if bstack1llll1lll1l1_opy_ is None or bstack1llll1lll11l_opy_ is None:
    logger.error(bstack1ll1ll1_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡽࡨࡪ࡮ࡨࠤࡨࡸࡥࡢࡶ࡬ࡲ࡬ࠦࡴࡦࡵࡷࠤࡷࡻ࡮ࠡࡨࡲࡶࠥࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮࠻ࠢࡐ࡭ࡸࡹࡩ࡯ࡩࠣࡥࡺࡺࡨࡦࡰࡷ࡭ࡨࡧࡴࡪࡱࡱࠤࡹࡵ࡫ࡦࡰࠪΎ"))
    return [None, None]
  try:
    settings = json.loads(os.getenv(bstack1ll1ll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚࡟ࡂࡅࡆࡉࡘ࡙ࡉࡃࡋࡏࡍ࡙࡟࡟ࡄࡑࡑࡊࡎࡍࡕࡓࡃࡗࡍࡔࡔ࡟࡚ࡏࡏࠫῬ"), bstack1ll1ll1_opy_ (u"ࠫࢀࢃࠧ῭")))
    data = {
        bstack1ll1ll1_opy_ (u"ࠬࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࠪ΅"): config[bstack1ll1ll1_opy_ (u"࠭ࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠫ`")],
        bstack1ll1ll1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪ῰"): config.get(bstack1ll1ll1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫ῱"), os.path.basename(os.getcwd())),
        bstack1ll1ll1_opy_ (u"ࠩࡶࡸࡦࡸࡴࡕ࡫ࡰࡩࠬῲ"): bstack1l11l1ll_opy_(),
        bstack1ll1ll1_opy_ (u"ࠪࡨࡪࡹࡣࡳ࡫ࡳࡸ࡮ࡵ࡮ࠨῳ"): config.get(bstack1ll1ll1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡇࡩࡸࡩࡲࡪࡲࡷ࡭ࡴࡴࠧῴ"), bstack1ll1ll1_opy_ (u"ࠬ࠭῵")),
        bstack1ll1ll1_opy_ (u"࠭ࡳࡰࡷࡵࡧࡪ࠭ῶ"): {
            bstack1ll1ll1_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡑࡥࡲ࡫ࠧῷ"): frameworkName,
            bstack1ll1ll1_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮࡚ࡪࡸࡳࡪࡱࡱࠫῸ"): bstack1llll1llll11_opy_,
            bstack1ll1ll1_opy_ (u"ࠩࡶࡨࡰ࡜ࡥࡳࡵ࡬ࡳࡳ࠭Ό"): __version__,
            bstack1ll1ll1_opy_ (u"ࠪࡰࡦࡴࡧࡶࡣࡪࡩࠬῺ"): bstack1ll1ll1_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫΏ"),
            bstack1ll1ll1_opy_ (u"ࠬࡺࡥࡴࡶࡉࡶࡦࡳࡥࡸࡱࡵ࡯ࠬῼ"): bstack1ll1ll1_opy_ (u"࠭ࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࠨ´"),
            bstack1ll1ll1_opy_ (u"ࠧࡵࡧࡶࡸࡋࡸࡡ࡮ࡧࡺࡳࡷࡱࡖࡦࡴࡶ࡭ࡴࡴࠧ῾"): bstack1lllll11llll_opy_
        },
        bstack1ll1ll1_opy_ (u"ࠨࡵࡨࡸࡹ࡯࡮ࡨࡵࠪ῿"): settings,
        bstack1ll1ll1_opy_ (u"ࠩࡹࡩࡷࡹࡩࡰࡰࡆࡳࡳࡺࡲࡰ࡮ࠪ "): bstack111l111ll1l_opy_(),
        bstack1ll1ll1_opy_ (u"ࠪࡧ࡮ࡏ࡮ࡧࡱࠪ "): bstack1l1l111l11_opy_(),
        bstack1ll1ll1_opy_ (u"ࠫ࡭ࡵࡳࡵࡋࡱࡪࡴ࠭ "): get_host_info(),
        bstack1ll1ll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠧ "): bstack11l1l111ll_opy_(config)
    }
    headers = {
        bstack1ll1ll1_opy_ (u"࠭ࡃࡰࡰࡷࡩࡳࡺ࠭ࡕࡻࡳࡩࠬ "): bstack1ll1ll1_opy_ (u"ࠧࡢࡲࡳࡰ࡮ࡩࡡࡵ࡫ࡲࡲ࠴ࡰࡳࡰࡰࠪ "),
    }
    config = {
        bstack1ll1ll1_opy_ (u"ࠨࡣࡸࡸ࡭࠭ "): (bstack1llll1lll1l1_opy_, bstack1llll1lll11l_opy_),
        bstack1ll1ll1_opy_ (u"ࠩ࡫ࡩࡦࡪࡥࡳࡵࠪ "): headers
    }
    response = bstack111l1l11l1_opy_(bstack1ll1ll1_opy_ (u"ࠪࡔࡔ࡙ࡔࠨ "), bstack1llll1ll1lll_opy_ + bstack1ll1ll1_opy_ (u"ࠫ࠴ࡼ࠲࠰ࡶࡨࡷࡹࡥࡲࡶࡰࡶࠫ "), data, config)
    bstack1lllll11l1ll_opy_ = response.json()
    if bstack1lllll11l1ll_opy_[bstack1ll1ll1_opy_ (u"ࠬࡹࡵࡤࡥࡨࡷࡸ࠭ ")]:
      parsed = json.loads(os.getenv(bstack1ll1ll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡢࡅࡈࡉࡅࡔࡕࡌࡆࡎࡒࡉࡕ࡛ࡢࡇࡔࡔࡆࡊࡉࡘࡖࡆ࡚ࡉࡐࡐࡢ࡝ࡒࡒࠧ​"), bstack1ll1ll1_opy_ (u"ࠧࡼࡿࠪ‌")))
      parsed[bstack1ll1ll1_opy_ (u"ࠨࡵࡦࡥࡳࡴࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩ‍")] = bstack1lllll11l1ll_opy_[bstack1ll1ll1_opy_ (u"ࠩࡧࡥࡹࡧࠧ‎")][bstack1ll1ll1_opy_ (u"ࠪࡷࡨࡧ࡮࡯ࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫ‏")]
      os.environ[bstack1ll1ll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡠࡃࡆࡇࡊ࡙ࡓࡊࡄࡌࡐࡎ࡚࡙ࡠࡅࡒࡒࡋࡏࡇࡖࡔࡄࡘࡎࡕࡎࡠ࡛ࡐࡐࠬ‐")] = json.dumps(parsed)
      bstack111llll111_opy_.bstack111l1llll1_opy_(bstack1lllll11l1ll_opy_[bstack1ll1ll1_opy_ (u"ࠬࡪࡡࡵࡣࠪ‑")][bstack1ll1ll1_opy_ (u"࠭ࡳࡤࡴ࡬ࡴࡹࡹࠧ‒")])
      bstack111llll111_opy_.bstack1lllll1l11l1_opy_(bstack1lllll11l1ll_opy_[bstack1ll1ll1_opy_ (u"ࠧࡥࡣࡷࡥࠬ–")][bstack1ll1ll1_opy_ (u"ࠨࡥࡲࡱࡲࡧ࡮ࡥࡵࠪ—")])
      bstack111llll111_opy_.store()
      return bstack1lllll11l1ll_opy_[bstack1ll1ll1_opy_ (u"ࠩࡧࡥࡹࡧࠧ―")][bstack1ll1ll1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡗࡳࡰ࡫࡮ࠨ‖")], bstack1lllll11l1ll_opy_[bstack1ll1ll1_opy_ (u"ࠫࡩࡧࡴࡢࠩ‗")][bstack1ll1ll1_opy_ (u"ࠬ࡯ࡤࠨ‘")]
    else:
      logger.error(bstack1ll1ll1_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡺ࡬࡮ࡲࡥࠡࡴࡸࡲࡳ࡯࡮ࡨࠢࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲ࠿ࠦࠧ’") + bstack1lllll11l1ll_opy_[bstack1ll1ll1_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ‚")])
      if bstack1lllll11l1ll_opy_[bstack1ll1ll1_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ‛")] == bstack1ll1ll1_opy_ (u"ࠩࡌࡲࡻࡧ࡬ࡪࡦࠣࡧࡴࡴࡦࡪࡩࡸࡶࡦࡺࡩࡰࡰࠣࡴࡦࡹࡳࡦࡦ࠱ࠫ“"):
        for bstack1lllll111l1l_opy_ in bstack1lllll11l1ll_opy_[bstack1ll1ll1_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࡵࠪ”")]:
          logger.error(bstack1lllll111l1l_opy_[bstack1ll1ll1_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ„")])
      return None, None
  except Exception as error:
    logger.error(bstack1ll1ll1_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡹ࡫࡭ࡱ࡫ࠠࡤࡴࡨࡥࡹ࡯࡮ࡨࠢࡷࡩࡸࡺࠠࡳࡷࡱࠤ࡫ࡵࡲࠡࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱ࠾ࠥࠨ‟") +  str(error))
    return None, None
def bstack1lllll111l11_opy_():
  if os.getenv(bstack1ll1ll1_opy_ (u"࠭ࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗࠫ†")) is None:
    return {
        bstack1ll1ll1_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧ‡"): bstack1ll1ll1_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧ•"),
        bstack1ll1ll1_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ‣"): bstack1ll1ll1_opy_ (u"ࠪࡆࡺ࡯࡬ࡥࠢࡦࡶࡪࡧࡴࡪࡱࡱࠤ࡭ࡧࡤࠡࡨࡤ࡭ࡱ࡫ࡤ࠯ࠩ․")
    }
  data = {bstack1ll1ll1_opy_ (u"ࠫࡪࡴࡤࡕ࡫ࡰࡩࠬ‥"): bstack1l11l1ll_opy_()}
  headers = {
      bstack1ll1ll1_opy_ (u"ࠬࡇࡵࡵࡪࡲࡶ࡮ࢀࡡࡵ࡫ࡲࡲࠬ…"): bstack1ll1ll1_opy_ (u"࠭ࡂࡦࡣࡵࡩࡷࠦࠧ‧") + os.getenv(bstack1ll1ll1_opy_ (u"ࠢࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠧ ")),
      bstack1ll1ll1_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡗࡽࡵ࡫ࠧ "): bstack1ll1ll1_opy_ (u"ࠩࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯࡫ࡵࡲࡲࠬ‪")
  }
  response = bstack111l1l11l1_opy_(bstack1ll1ll1_opy_ (u"ࠪࡔ࡚࡚ࠧ‫"), bstack1llll1ll1lll_opy_ + bstack1ll1ll1_opy_ (u"ࠫ࠴ࡺࡥࡴࡶࡢࡶࡺࡴࡳ࠰ࡵࡷࡳࡵ࠭‬"), data, { bstack1ll1ll1_opy_ (u"ࠬ࡮ࡥࡢࡦࡨࡶࡸ࠭‭"): headers })
  try:
    if response.status_code == 200:
      logger.info(bstack1ll1ll1_opy_ (u"ࠨࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡗࡩࡸࡺࠠࡓࡷࡱࠤࡲࡧࡲ࡬ࡧࡧࠤࡦࡹࠠࡤࡱࡰࡴࡱ࡫ࡴࡦࡦࠣࡥࡹࠦࠢ‮") + bstack1l1l1l11_opy_().isoformat() + bstack1ll1ll1_opy_ (u"࡛ࠧࠩ "))
      return {bstack1ll1ll1_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨ‰"): bstack1ll1ll1_opy_ (u"ࠩࡶࡹࡨࡩࡥࡴࡵࠪ‱"), bstack1ll1ll1_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ′"): bstack1ll1ll1_opy_ (u"ࠫࠬ″")}
    else:
      response.raise_for_status()
  except requests.RequestException as error:
    logger.error(bstack1ll1ll1_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡹ࡫࡭ࡱ࡫ࠠ࡮ࡣࡵ࡯࡮ࡴࡧࠡࡥࡲࡱࡵࡲࡥࡵ࡫ࡲࡲࠥࡵࡦࠡࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤ࡙࡫ࡳࡵࠢࡕࡹࡳࡀࠠࠣ‴") + str(error))
    return {
        bstack1ll1ll1_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭‵"): bstack1ll1ll1_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭‶"),
        bstack1ll1ll1_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ‷"): str(error)
    }
def bstack1lllll11l111_opy_(bstack1lllll1111l1_opy_):
    return re.match(bstack1ll1ll1_opy_ (u"ࡴࠪࡢࡡࡪࠫࠩ࡞࠱ࡠࡩ࠱ࠩࡀࠦࠪ‸"), bstack1lllll1111l1_opy_.strip()) is not None
def bstack1lll1ll111_opy_(caps, options, desired_capabilities={}, config=None):
    try:
        if options:
          bstack1lllll11111l_opy_ = options.to_capabilities()
        elif desired_capabilities:
          bstack1lllll11111l_opy_ = desired_capabilities
        else:
          bstack1lllll11111l_opy_ = {}
        bstack1l111l111l1_opy_ = (bstack1lllll11111l_opy_.get(bstack1ll1ll1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡓࡧ࡭ࡦࠩ‹"), bstack1ll1ll1_opy_ (u"ࠫࠬ›")).lower() or caps.get(bstack1ll1ll1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡎࡢ࡯ࡨࠫ※"), bstack1ll1ll1_opy_ (u"࠭ࠧ‼")).lower())
        if bstack1l111l111l1_opy_ == bstack1ll1ll1_opy_ (u"ࠧࡪࡱࡶࠫ‽"):
            return True
        if bstack1l111l111l1_opy_ == bstack1ll1ll1_opy_ (u"ࠨࡣࡱࡨࡷࡵࡩࡥࠩ‾"):
            bstack1l111ll1lll_opy_ = str(float(caps.get(bstack1ll1ll1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰ࡚ࡪࡸࡳࡪࡱࡱࠫ‿")) or bstack1lllll11111l_opy_.get(bstack1ll1ll1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫ⁀"), {}).get(bstack1ll1ll1_opy_ (u"ࠫࡴࡹࡖࡦࡴࡶ࡭ࡴࡴࠧ⁁"),bstack1ll1ll1_opy_ (u"ࠬ࠭⁂"))))
            if bstack1l111l111l1_opy_ == bstack1ll1ll1_opy_ (u"࠭ࡡ࡯ࡦࡵࡳ࡮ࡪࠧ⁃") and int(bstack1l111ll1lll_opy_.split(bstack1ll1ll1_opy_ (u"ࠧ࠯ࠩ⁄"))[0]) < float(bstack11l1l1111l1_opy_):
                logger.warning(str(bstack11l1l1ll1l1_opy_))
                return False
            return True
        bstack1l111lll11l_opy_ = caps.get(bstack1ll1ll1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩ⁅"), {}).get(bstack1ll1ll1_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࡐࡤࡱࡪ࠭⁆"), caps.get(bstack1ll1ll1_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࠪ⁇"), bstack1ll1ll1_opy_ (u"ࠫࠬ⁈")))
        if bstack1l111lll11l_opy_:
            logger.warning(bstack1ll1ll1_opy_ (u"ࠧࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡺ࡭ࡱࡲࠠࡳࡷࡱࠤࡴࡴ࡬ࡺࠢࡲࡲࠥࡊࡥࡴ࡭ࡷࡳࡵࠦࡢࡳࡱࡺࡷࡪࡸࡳ࠯ࠤ⁉"))
            return False
        browser = caps.get(bstack1ll1ll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫ⁊"), bstack1ll1ll1_opy_ (u"ࠧࠨ⁋")).lower() or bstack1lllll11111l_opy_.get(bstack1ll1ll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭⁌"), bstack1ll1ll1_opy_ (u"ࠩࠪ⁍")).lower()
        if browser != bstack1ll1ll1_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧࠪ⁎"):
            logger.warning(bstack1ll1ll1_opy_ (u"ࠦࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡹ࡬ࡰࡱࠦࡲࡶࡰࠣࡳࡳࡲࡹࠡࡱࡱࠤࡈ࡮ࡲࡰ࡯ࡨࠤࡧࡸ࡯ࡸࡵࡨࡶࡸ࠴ࠢ⁏"))
            return False
        browser_version = caps.get(bstack1ll1ll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭⁐")) or caps.get(bstack1ll1ll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨ⁑")) or bstack1lllll11111l_opy_.get(bstack1ll1ll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨ⁒")) or bstack1lllll11111l_opy_.get(bstack1ll1ll1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩ⁓"), {}).get(bstack1ll1ll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪ⁔")) or bstack1lllll11111l_opy_.get(bstack1ll1ll1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫ⁕"), {}).get(bstack1ll1ll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭⁖"))
        bstack1l111ll1l11_opy_ = bstack1llll1ll11ll_opy_.bstack1l1111ll1ll_opy_
        bstack1lllll111111_opy_ = False
        if config is not None:
          bstack1lllll111111_opy_ = bstack1ll1ll1_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩ⁗") in config and str(config[bstack1ll1ll1_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪ⁘")]).lower() != bstack1ll1ll1_opy_ (u"ࠧࡧࡣ࡯ࡷࡪ࠭⁙")
        if os.environ.get(bstack1ll1ll1_opy_ (u"ࠨࡋࡖࡣࡓࡕࡎࡠࡄࡖࡘࡆࡉࡋࡠࡋࡑࡊࡗࡇ࡟ࡂ࠳࠴࡝ࡤ࡙ࡅࡔࡕࡌࡓࡓ࠭⁚"), bstack1ll1ll1_opy_ (u"ࠩࠪ⁛")).lower() == bstack1ll1ll1_opy_ (u"ࠪࡸࡷࡻࡥࠨ⁜") or bstack1lllll111111_opy_:
          bstack1l111ll1l11_opy_ = bstack1llll1ll11ll_opy_.bstack1l111lll1ll_opy_
        if browser_version and browser_version != bstack1ll1ll1_opy_ (u"ࠫࡱࡧࡴࡦࡵࡷࠫ⁝") and int(browser_version.split(bstack1ll1ll1_opy_ (u"ࠬ࠴ࠧ⁞"))[0]) <= bstack1l111ll1l11_opy_:
          logger.warning(bstack1lll1ll111l_opy_ (u"࠭ࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡻ࡮ࡲ࡬ࠡࡴࡸࡲࠥࡵ࡮࡭ࡻࠣࡳࡳࠦࡃࡩࡴࡲࡱࡪࠦࡢࡳࡱࡺࡷࡪࡸࠠࡷࡧࡵࡷ࡮ࡵ࡮ࠡࡩࡵࡩࡦࡺࡥࡳࠢࡷ࡬ࡦࡴࠠࡼ࡯࡬ࡲࡤࡧ࠱࠲ࡻࡢࡷࡺࡶࡰࡰࡴࡷࡩࡩࡥࡣࡩࡴࡲࡱࡪࡥࡶࡦࡴࡶ࡭ࡴࡴࡽ࠯ࠩ "))
          return False
        if not options:
          bstack1l111l1l1ll_opy_ = caps.get(bstack1ll1ll1_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬ⁠")) or bstack1lllll11111l_opy_.get(bstack1ll1ll1_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭⁡"), {})
          if bstack1ll1ll1_opy_ (u"ࠩ࠰࠱࡭࡫ࡡࡥ࡮ࡨࡷࡸ࠭⁢") in bstack1l111l1l1ll_opy_.get(bstack1ll1ll1_opy_ (u"ࠪࡥࡷ࡭ࡳࠨ⁣"), []):
              logger.warning(bstack1ll1ll1_opy_ (u"ࠦࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡹ࡬ࡰࡱࠦ࡮ࡰࡶࠣࡶࡺࡴࠠࡰࡰࠣࡰࡪ࡭ࡡࡤࡻࠣ࡬ࡪࡧࡤ࡭ࡧࡶࡷࠥࡳ࡯ࡥࡧ࠱ࠤࡘࡽࡩࡵࡥ࡫ࠤࡹࡵࠠ࡯ࡧࡺࠤ࡭࡫ࡡࡥ࡮ࡨࡷࡸࠦ࡭ࡰࡦࡨࠤࡴࡸࠠࡢࡸࡲ࡭ࡩࠦࡵࡴ࡫ࡱ࡫ࠥ࡮ࡥࡢࡦ࡯ࡩࡸࡹࠠ࡮ࡱࡧࡩ࠳ࠨ⁤"))
              return False
        return True
    except Exception as error:
        logger.debug(bstack1ll1ll1_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡻࡧ࡬ࡪࡦࡤࡸࡪࠦࡡ࠲࠳ࡼࠤࡸࡻࡰࡱࡱࡵࡸࠥࡀࠢ⁥") + str(error))
        return False
def set_capabilities(caps, config):
  try:
    bstack1l1l1ll11ll_opy_ = config.get(bstack1ll1ll1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭⁦"), {})
    bstack1l1l1ll11ll_opy_[bstack1ll1ll1_opy_ (u"ࠧࡢࡷࡷ࡬࡙ࡵ࡫ࡦࡰࠪ⁧")] = os.getenv(bstack1ll1ll1_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭⁨"))
    bstack1111ll11l1l_opy_ = json.loads(os.getenv(bstack1ll1ll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡥࡁࡄࡅࡈࡗࡘࡏࡂࡊࡎࡌࡘ࡞ࡥࡃࡐࡐࡉࡍࡌ࡛ࡒࡂࡖࡌࡓࡓࡥ࡙ࡎࡎࠪ⁩"), bstack1ll1ll1_opy_ (u"ࠪࡿࢂ࠭⁪"))).get(bstack1ll1ll1_opy_ (u"ࠫࡸࡩࡡ࡯ࡰࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬ⁫"))
    if not config[bstack1ll1ll1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡔࡷࡵࡤࡶࡥࡷࡑࡦࡶࠧ⁬")].get(bstack1ll1ll1_opy_ (u"ࠨࡡࡱࡲࡢࡥࡺࡺ࡯࡮ࡣࡷࡩࠧ⁭")):
      if bstack1ll1ll1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨ⁮") in caps:
        caps[bstack1ll1ll1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩ⁯")][bstack1ll1ll1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩ⁰")] = bstack1l1l1ll11ll_opy_
        caps[bstack1ll1ll1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫⁱ")][bstack1ll1ll1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫ⁲")][bstack1ll1ll1_opy_ (u"ࠬࡹࡣࡢࡰࡱࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭⁳")] = bstack1111ll11l1l_opy_
      else:
        caps[bstack1ll1ll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬ⁴")] = bstack1l1l1ll11ll_opy_
        caps[bstack1ll1ll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭⁵")][bstack1ll1ll1_opy_ (u"ࠨࡵࡦࡥࡳࡴࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩ⁶")] = bstack1111ll11l1l_opy_
  except Exception as error:
    logger.debug(bstack1ll1ll1_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡽࡨࡪ࡮ࡨࠤࡸ࡫ࡴࡵ࡫ࡱ࡫ࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳ࠯ࠢࡈࡶࡷࡵࡲ࠻ࠢࠥ⁷") +  str(error))
def bstack111ll1ll1l_opy_(driver, bstack1lllll11ll11_opy_):
  try:
    setattr(driver, bstack1ll1ll1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡄ࠵࠶ࡿࡓࡩࡱࡸࡰࡩ࡙ࡣࡢࡰࠪ⁸"), True)
    session = driver.session_id
    if session:
      bstack1llll1llll1l_opy_ = True
      current_url = driver.current_url
      try:
        url = urlparse(current_url)
      except Exception as e:
        bstack1llll1llll1l_opy_ = False
      bstack1llll1llll1l_opy_ = url.scheme in [bstack1ll1ll1_opy_ (u"ࠦ࡭ࡺࡴࡱࠤ⁹"), bstack1ll1ll1_opy_ (u"ࠧ࡮ࡴࡵࡲࡶࠦ⁺")]
      if bstack1llll1llll1l_opy_:
        if bstack1lllll11ll11_opy_:
          logger.info(bstack1ll1ll1_opy_ (u"ࠨࡓࡦࡶࡸࡴࠥ࡬࡯ࡳࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡷࡩࡸࡺࡩ࡯ࡩࠣ࡬ࡦࡹࠠࡴࡶࡤࡶࡹ࡫ࡤ࠯ࠢࡄࡹࡹࡵ࡭ࡢࡶࡨࠤࡹ࡫ࡳࡵࠢࡦࡥࡸ࡫ࠠࡦࡺࡨࡧࡺࡺࡩࡰࡰࠣࡻ࡮ࡲ࡬ࠡࡤࡨ࡫࡮ࡴࠠ࡮ࡱࡰࡩࡳࡺࡡࡳ࡫࡯ࡽ࠳ࠨ⁻"))
      return bstack1lllll11ll11_opy_
  except Exception as e:
    logger.error(bstack1ll1ll1_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡳࡵࡣࡵࡸ࡮ࡴࡧࠡࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡹࡣࡢࡰࠣࡪࡴࡸࠠࡵࡪ࡬ࡷࠥࡺࡥࡴࡶࠣࡧࡦࡹࡥ࠻ࠢࠥ⁼") + str(e))
    return False
def bstack111l111l_opy_(driver, name, path):
  try:
    bstack1l111l1111l_opy_ = {
        bstack1ll1ll1_opy_ (u"ࠨࡶ࡫ࡘࡪࡹࡴࡓࡷࡱ࡙ࡺ࡯ࡤࠨ⁽"): threading.current_thread().current_test_uuid,
        bstack1ll1ll1_opy_ (u"ࠩࡷ࡬ࡇࡻࡩ࡭ࡦࡘࡹ࡮ࡪࠧ⁾"): os.environ.get(bstack1ll1ll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨⁿ"), bstack1ll1ll1_opy_ (u"ࠫࠬ₀")),
        bstack1ll1ll1_opy_ (u"ࠬࡺࡨࡋࡹࡷࡘࡴࡱࡥ࡯ࠩ₁"): os.environ.get(bstack1ll1ll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪ₂"), bstack1ll1ll1_opy_ (u"ࠧࠨ₃"))
    }
    bstack1ll111l11ll_opy_ = bstack111l11l1ll_opy_.bstack1ll11l11l1l_opy_(EVENTS.bstack11111l111_opy_.value)
    logger.debug(bstack1ll1ll1_opy_ (u"ࠨࡒࡨࡶ࡫ࡵࡲ࡮࡫ࡱ࡫ࠥࡹࡣࡢࡰࠣࡦࡪ࡬࡯ࡳࡧࠣࡷࡦࡼࡩ࡯ࡩࠣࡶࡪࡹࡵ࡭ࡶࡶࠫ₄"))
    try:
      if (bstack1l1lll11_opy_(threading.current_thread(), bstack1ll1ll1_opy_ (u"ࠩ࡬ࡷࡆࡶࡰࡂ࠳࠴ࡽ࡙࡫ࡳࡵࠩ₅"), None) and bstack1l1lll11_opy_(threading.current_thread(), bstack1ll1ll1_opy_ (u"ࠪࡥࡵࡶࡁ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬ₆"), None)):
        scripts = {bstack1ll1ll1_opy_ (u"ࠫࡸࡩࡡ࡯ࠩ₇"): bstack111llll111_opy_.perform_scan}
        bstack1llll1ll1l1l_opy_ = json.loads(scripts[bstack1ll1ll1_opy_ (u"ࠧࡹࡣࡢࡰࠥ₈")].replace(bstack1ll1ll1_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࠤ₉"), bstack1ll1ll1_opy_ (u"ࠢࠣ₊")))
        bstack1llll1ll1l1l_opy_[bstack1ll1ll1_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫ₋")][bstack1ll1ll1_opy_ (u"ࠩࡰࡩࡹ࡮࡯ࡥࠩ₌")] = None
        scripts[bstack1ll1ll1_opy_ (u"ࠥࡷࡨࡧ࡮ࠣ₍")] = bstack1ll1ll1_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࠢ₎") + json.dumps(bstack1llll1ll1l1l_opy_)
        bstack111llll111_opy_.bstack111l1llll1_opy_(scripts)
        bstack111llll111_opy_.store()
        logger.debug(driver.execute_script(bstack111llll111_opy_.perform_scan))
      else:
        logger.debug(driver.execute_async_script(bstack111llll111_opy_.perform_scan, {bstack1ll1ll1_opy_ (u"ࠧࡳࡥࡵࡪࡲࡨࠧ₏"): name}))
      bstack111l11l1ll_opy_.end(EVENTS.bstack11111l111_opy_.value, bstack1ll111l11ll_opy_ + bstack1ll1ll1_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨₐ"), bstack1ll111l11ll_opy_ + bstack1ll1ll1_opy_ (u"ࠢ࠻ࡧࡱࡨࠧₑ"), True, None)
    except Exception as error:
      bstack111l11l1ll_opy_.end(EVENTS.bstack11111l111_opy_.value, bstack1ll111l11ll_opy_ + bstack1ll1ll1_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣₒ"), bstack1ll111l11ll_opy_ + bstack1ll1ll1_opy_ (u"ࠤ࠽ࡩࡳࡪࠢₓ"), False, str(error))
    bstack1ll111l11ll_opy_ = bstack111l11l1ll_opy_.bstack11ll1ll11ll_opy_(EVENTS.bstack1l1111lll11_opy_.value)
    bstack111l11l1ll_opy_.mark(bstack1ll111l11ll_opy_ + bstack1ll1ll1_opy_ (u"ࠥ࠾ࡸࡺࡡࡳࡶࠥₔ"))
    try:
      if (bstack1l1lll11_opy_(threading.current_thread(), bstack1ll1ll1_opy_ (u"ࠫ࡮ࡹࡁࡱࡲࡄ࠵࠶ࡿࡔࡦࡵࡷࠫₕ"), None) and bstack1l1lll11_opy_(threading.current_thread(), bstack1ll1ll1_opy_ (u"ࠬࡧࡰࡱࡃ࠴࠵ࡾࡖ࡬ࡢࡶࡩࡳࡷࡳࠧₖ"), None)):
        scripts = {bstack1ll1ll1_opy_ (u"࠭ࡳࡤࡣࡱࠫₗ"): bstack111llll111_opy_.perform_scan}
        bstack1llll1ll1l1l_opy_ = json.loads(scripts[bstack1ll1ll1_opy_ (u"ࠢࡴࡥࡤࡲࠧₘ")].replace(bstack1ll1ll1_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࠦₙ"), bstack1ll1ll1_opy_ (u"ࠤࠥₚ")))
        bstack1llll1ll1l1l_opy_[bstack1ll1ll1_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ₛ")][bstack1ll1ll1_opy_ (u"ࠫࡲ࡫ࡴࡩࡱࡧࠫₜ")] = None
        scripts[bstack1ll1ll1_opy_ (u"ࠧࡹࡣࡢࡰࠥ₝")] = bstack1ll1ll1_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࠤ₞") + json.dumps(bstack1llll1ll1l1l_opy_)
        bstack111llll111_opy_.bstack111l1llll1_opy_(scripts)
        bstack111llll111_opy_.store()
        logger.debug(driver.execute_script(bstack111llll111_opy_.perform_scan))
      else:
        logger.debug(driver.execute_async_script(bstack111llll111_opy_.bstack1lllll1l11ll_opy_, bstack1l111l1111l_opy_))
      bstack111l11l1ll_opy_.end(bstack1ll111l11ll_opy_, bstack1ll111l11ll_opy_ + bstack1ll1ll1_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢ₟"), bstack1ll111l11ll_opy_ + bstack1ll1ll1_opy_ (u"ࠣ࠼ࡨࡲࡩࠨ₠"),True, None)
    except Exception as error:
      bstack111l11l1ll_opy_.end(bstack1ll111l11ll_opy_, bstack1ll111l11ll_opy_ + bstack1ll1ll1_opy_ (u"ࠤ࠽ࡷࡹࡧࡲࡵࠤ₡"), bstack1ll111l11ll_opy_ + bstack1ll1ll1_opy_ (u"ࠥ࠾ࡪࡴࡤࠣ₢"),False, str(error))
    logger.info(bstack1ll1ll1_opy_ (u"ࠦࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡹ࡫ࡳࡵ࡫ࡱ࡫ࠥ࡬࡯ࡳࠢࡷ࡬࡮ࡹࠠࡵࡧࡶࡸࠥࡩࡡࡴࡧࠣ࡬ࡦࡹࠠࡦࡰࡧࡩࡩ࠴ࠢ₣"))
  except Exception as bstack1l111l11l1l_opy_:
    logger.error(bstack1ll1ll1_opy_ (u"ࠧࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡸࡥࡴࡷ࡯ࡸࡸࠦࡣࡰࡷ࡯ࡨࠥࡴ࡯ࡵࠢࡥࡩࠥࡶࡲࡰࡥࡨࡷࡸ࡫ࡤࠡࡨࡲࡶࠥࡺࡨࡦࠢࡷࡩࡸࡺࠠࡤࡣࡶࡩ࠿ࠦࠢ₤") + str(path) + bstack1ll1ll1_opy_ (u"ࠨࠠࡆࡴࡵࡳࡷࠦ࠺ࠣ₥") + str(bstack1l111l11l1l_opy_))
def bstack1llll1lll1ll_opy_(driver):
    caps = driver.capabilities
    if caps.get(bstack1ll1ll1_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡐࡤࡱࡪࠨ₦")) and str(caps.get(bstack1ll1ll1_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡑࡥࡲ࡫ࠢ₧"))).lower() == bstack1ll1ll1_opy_ (u"ࠤࡤࡲࡩࡸ࡯ࡪࡦࠥ₨"):
        bstack1l111ll1lll_opy_ = caps.get(bstack1ll1ll1_opy_ (u"ࠥࡥࡵࡶࡩࡶ࡯࠽ࡴࡱࡧࡴࡧࡱࡵࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠧ₩")) or caps.get(bstack1ll1ll1_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲ࡜ࡥࡳࡵ࡬ࡳࡳࠨ₪"))
        if bstack1l111ll1lll_opy_ and int(str(bstack1l111ll1lll_opy_)) < bstack11l1l1111l1_opy_:
            return False
    return True
def bstack1ll111ll1l_opy_(config):
  if bstack1ll1ll1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ₫") in config:
        return config[bstack1ll1ll1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭€")]
  for platform in config.get(bstack1ll1ll1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ₭"), []):
      if bstack1ll1ll1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ₮") in platform:
          return platform[bstack1ll1ll1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ₯")]
  return None
def bstack111l1l1l1l_opy_(bstack11l11l1l1_opy_):
  try:
    browser_name = bstack11l11l1l1_opy_[bstack1ll1ll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡳࡧ࡭ࡦࠩ₰")]
    browser_version = bstack11l11l1l1_opy_[bstack1ll1ll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭₱")]
    chrome_options = bstack11l11l1l1_opy_[bstack1ll1ll1_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࡤࡵࡰࡵ࡫ࡲࡲࡸ࠭₲")]
    try:
        bstack1lllll111ll1_opy_ = int(browser_version.split(bstack1ll1ll1_opy_ (u"࠭࠮ࠨ₳"))[0])
    except ValueError as e:
        logger.error(bstack1ll1ll1_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡷࡩ࡫࡯ࡩࠥࡩ࡯࡯ࡸࡨࡶࡹ࡯࡮ࡨࠢࡥࡶࡴࡽࡳࡦࡴࠣࡺࡪࡸࡳࡪࡱࡱࠦ₴") + str(e))
        return False
    if not (browser_name and browser_name.lower() == bstack1ll1ll1_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࠨ₵")):
        logger.warning(bstack1ll1ll1_opy_ (u"ࠤࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡷࡪ࡮࡯ࠤࡷࡻ࡮ࠡࡱࡱࡰࡾࠦ࡯࡯ࠢࡆ࡬ࡷࡵ࡭ࡦࠢࡥࡶࡴࡽࡳࡦࡴࡶ࠲ࠧ₶"))
        return False
    if bstack1lllll111ll1_opy_ < bstack1llll1ll11ll_opy_.bstack1l111lll1ll_opy_:
        logger.warning(bstack1lll1ll111l_opy_ (u"ࠪࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡳࡧࡴࡹ࡮ࡸࡥࡴࠢࡆ࡬ࡷࡵ࡭ࡦࠢࡹࡩࡷࡹࡩࡰࡰࠣࡿࡈࡕࡎࡔࡖࡄࡒ࡙࡙࠮ࡎࡋࡑࡍࡒ࡛ࡍࡠࡐࡒࡒࡤࡈࡓࡕࡃࡆࡏࡤࡏࡎࡇࡔࡄࡣࡆ࠷࠱࡚ࡡࡖ࡙ࡕࡖࡏࡓࡖࡈࡈࡤࡉࡈࡓࡑࡐࡉࡤ࡜ࡅࡓࡕࡌࡓࡓࢃࠠࡰࡴࠣ࡬࡮࡭ࡨࡦࡴ࠱ࠫ₷"))
        return False
    if chrome_options and any(bstack1ll1ll1_opy_ (u"ࠫ࠲࠳ࡨࡦࡣࡧࡰࡪࡹࡳࠨ₸") in value for value in chrome_options.values() if isinstance(value, str)):
        logger.warning(bstack1ll1ll1_opy_ (u"ࠧࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡺ࡭ࡱࡲࠠ࡯ࡱࡷࠤࡷࡻ࡮ࠡࡱࡱࠤࡱ࡫ࡧࡢࡥࡼࠤ࡭࡫ࡡࡥ࡮ࡨࡷࡸࠦ࡭ࡰࡦࡨ࠲࡙ࠥࡷࡪࡶࡦ࡬ࠥࡺ࡯ࠡࡰࡨࡻࠥ࡮ࡥࡢࡦ࡯ࡩࡸࡹࠠ࡮ࡱࡧࡩࠥࡵࡲࠡࡣࡹࡳ࡮ࡪࠠࡶࡵ࡬ࡲ࡬ࠦࡨࡦࡣࡧࡰࡪࡹࡳࠡ࡯ࡲࡨࡪ࠴ࠢ₹"))
        return False
    return True
  except Exception as e:
    logger.error(bstack1ll1ll1_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡥ࡫ࡩࡨࡱࡩ࡯ࡩࠣࡴࡱࡧࡴࡧࡱࡵࡱࠥࡹࡵࡱࡲࡲࡶࡹࠦࡦࡰࡴࠣࡰࡴࡩࡡ࡭ࠢࡆ࡬ࡷࡵ࡭ࡦ࠼ࠣࠦ₺") + str(e))
    return False
def bstack1ll1l1lll1_opy_(bstack1lll1l11l1_opy_, config):
    try:
      bstack1l111lllll1_opy_ = bstack1ll1ll1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ₻") in config and config[bstack1ll1ll1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ₼")] == True
      bstack1lllll111111_opy_ = bstack1ll1ll1_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭₽") in config and str(config[bstack1ll1ll1_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧ₾")]).lower() != bstack1ll1ll1_opy_ (u"ࠫ࡫ࡧ࡬ࡴࡧࠪ₿")
      if not (bstack1l111lllll1_opy_ and (not bstack11l1l111ll_opy_(config) or bstack1lllll111111_opy_)):
        return bstack1lll1l11l1_opy_
      bstack1llll1ll1l11_opy_ = bstack111llll111_opy_.bstack1lllll1l1l1l_opy_
      if bstack1llll1ll1l11_opy_ is None:
        logger.debug(bstack1ll1ll1_opy_ (u"ࠧࡍ࡯ࡰࡩ࡯ࡩࠥࡩࡨࡳࡱࡰࡩࠥࡵࡰࡵ࡫ࡲࡲࡸࠦࡡࡳࡧࠣࡒࡴࡴࡥࠣ⃀"))
        return bstack1lll1l11l1_opy_
      bstack1lllll1111ll_opy_ = int(str(bstack111l1l1l1ll_opy_()).split(bstack1ll1ll1_opy_ (u"࠭࠮ࠨ⃁"))[0])
      logger.debug(bstack1ll1ll1_opy_ (u"ࠢࡔࡧ࡯ࡩࡳ࡯ࡵ࡮ࠢࡹࡩࡷࡹࡩࡰࡰࠣࡨࡪࡺࡥࡤࡶࡨࡨ࠿ࠦࠢ⃂") + str(bstack1lllll1111ll_opy_) + bstack1ll1ll1_opy_ (u"ࠣࠤ⃃"))
      if bstack1lllll1111ll_opy_ == 3 and isinstance(bstack1lll1l11l1_opy_, dict) and bstack1ll1ll1_opy_ (u"ࠩࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩ⃄") in bstack1lll1l11l1_opy_ and bstack1llll1ll1l11_opy_ is not None:
        if bstack1ll1ll1_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨ⃅") not in bstack1lll1l11l1_opy_[bstack1ll1ll1_opy_ (u"ࠫࡩ࡫ࡳࡪࡴࡨࡨࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠫ⃆")]:
          bstack1lll1l11l1_opy_[bstack1ll1ll1_opy_ (u"ࠬࡪࡥࡴ࡫ࡵࡩࡩࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠬ⃇")][bstack1ll1ll1_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫ⃈")] = {}
        if bstack1ll1ll1_opy_ (u"ࠧࡢࡴࡪࡷࠬ⃉") in bstack1llll1ll1l11_opy_:
          if bstack1ll1ll1_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭⃊") not in bstack1lll1l11l1_opy_[bstack1ll1ll1_opy_ (u"ࠩࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩ⃋")][bstack1ll1ll1_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨ⃌")]:
            bstack1lll1l11l1_opy_[bstack1ll1ll1_opy_ (u"ࠫࡩ࡫ࡳࡪࡴࡨࡨࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠫ⃍")][bstack1ll1ll1_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ⃎")][bstack1ll1ll1_opy_ (u"࠭ࡡࡳࡩࡶࠫ⃏")] = []
          for arg in bstack1llll1ll1l11_opy_[bstack1ll1ll1_opy_ (u"ࠧࡢࡴࡪࡷࠬ⃐")]:
            if arg not in bstack1lll1l11l1_opy_[bstack1ll1ll1_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨ⃑")][bstack1ll1ll1_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹ⃒ࠧ")][bstack1ll1ll1_opy_ (u"ࠪࡥࡷ࡭ࡳࠨ⃓")]:
              bstack1lll1l11l1_opy_[bstack1ll1ll1_opy_ (u"ࠫࡩ࡫ࡳࡪࡴࡨࡨࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠫ⃔")][bstack1ll1ll1_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ⃕")][bstack1ll1ll1_opy_ (u"࠭ࡡࡳࡩࡶࠫ⃖")].append(arg)
        if bstack1ll1ll1_opy_ (u"ࠧࡦࡺࡷࡩࡳࡹࡩࡰࡰࡶࠫ⃗") in bstack1llll1ll1l11_opy_:
          if bstack1ll1ll1_opy_ (u"ࠨࡧࡻࡸࡪࡴࡳࡪࡱࡱࡷ⃘ࠬ") not in bstack1lll1l11l1_opy_[bstack1ll1ll1_opy_ (u"ࠩࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴ⃙ࠩ")][bstack1ll1ll1_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨ⃚")]:
            bstack1lll1l11l1_opy_[bstack1ll1ll1_opy_ (u"ࠫࡩ࡫ࡳࡪࡴࡨࡨࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠫ⃛")][bstack1ll1ll1_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ⃜")][bstack1ll1ll1_opy_ (u"࠭ࡥࡹࡶࡨࡲࡸ࡯࡯࡯ࡵࠪ⃝")] = []
          for ext in bstack1llll1ll1l11_opy_[bstack1ll1ll1_opy_ (u"ࠧࡦࡺࡷࡩࡳࡹࡩࡰࡰࡶࠫ⃞")]:
            if ext not in bstack1lll1l11l1_opy_[bstack1ll1ll1_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨ⃟")][bstack1ll1ll1_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ⃠")][bstack1ll1ll1_opy_ (u"ࠪࡩࡽࡺࡥ࡯ࡵ࡬ࡳࡳࡹࠧ⃡")]:
              bstack1lll1l11l1_opy_[bstack1ll1ll1_opy_ (u"ࠫࡩ࡫ࡳࡪࡴࡨࡨࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠫ⃢")][bstack1ll1ll1_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ⃣")][bstack1ll1ll1_opy_ (u"࠭ࡥࡹࡶࡨࡲࡸ࡯࡯࡯ࡵࠪ⃤")].append(ext)
        if bstack1ll1ll1_opy_ (u"ࠧࡱࡴࡨࡪࡸ⃥࠭") in bstack1llll1ll1l11_opy_:
          if bstack1ll1ll1_opy_ (u"ࠨࡲࡵࡩ࡫ࡹ⃦ࠧ") not in bstack1lll1l11l1_opy_[bstack1ll1ll1_opy_ (u"ࠩࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩ⃧")][bstack1ll1ll1_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨ⃨")]:
            bstack1lll1l11l1_opy_[bstack1ll1ll1_opy_ (u"ࠫࡩ࡫ࡳࡪࡴࡨࡨࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠫ⃩")][bstack1ll1ll1_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵ⃪ࠪ")][bstack1ll1ll1_opy_ (u"࠭ࡰࡳࡧࡩࡷ⃫ࠬ")] = {}
          bstack1111ll1ll1l_opy_(bstack1lll1l11l1_opy_[bstack1ll1ll1_opy_ (u"ࠧࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹ⃬ࠧ")][bstack1ll1ll1_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ⃭࠭")][bstack1ll1ll1_opy_ (u"ࠩࡳࡶࡪ࡬ࡳࠨ⃮")],
                    bstack1llll1ll1l11_opy_[bstack1ll1ll1_opy_ (u"ࠪࡴࡷ࡫ࡦࡴ⃯ࠩ")])
        os.environ[bstack1ll1ll1_opy_ (u"ࠫࡎ࡙࡟ࡏࡑࡑࡣࡇ࡙ࡔࡂࡅࡎࡣࡎࡔࡆࡓࡃࡢࡅ࠶࠷࡙ࡠࡕࡈࡗࡘࡏࡏࡏࠩ⃰")] = bstack1ll1ll1_opy_ (u"ࠬࡺࡲࡶࡧࠪ⃱")
        return bstack1lll1l11l1_opy_
      else:
        chrome_options = None
        if isinstance(bstack1lll1l11l1_opy_, ChromeOptions):
          chrome_options = bstack1lll1l11l1_opy_
        elif isinstance(bstack1lll1l11l1_opy_, dict):
          for value in bstack1lll1l11l1_opy_.values():
            if isinstance(value, ChromeOptions):
              chrome_options = value
              break
        if chrome_options is None:
          chrome_options = ChromeOptions()
          if isinstance(bstack1lll1l11l1_opy_, dict):
            bstack1lll1l11l1_opy_[bstack1ll1ll1_opy_ (u"࠭࡯ࡱࡶ࡬ࡳࡳࡹࠧ⃲")] = chrome_options
          else:
            bstack1lll1l11l1_opy_ = chrome_options
        if bstack1llll1ll1l11_opy_ is not None:
          if bstack1ll1ll1_opy_ (u"ࠧࡢࡴࡪࡷࠬ⃳") in bstack1llll1ll1l11_opy_:
                bstack1lllll111lll_opy_ = chrome_options.arguments or []
                new_args = bstack1llll1ll1l11_opy_[bstack1ll1ll1_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭⃴")]
                for arg in new_args:
                    if arg not in bstack1lllll111lll_opy_:
                        chrome_options.add_argument(arg)
          if bstack1ll1ll1_opy_ (u"ࠩࡨࡼࡹ࡫࡮ࡴ࡫ࡲࡲࡸ࠭⃵") in bstack1llll1ll1l11_opy_:
                existing_extensions = chrome_options.experimental_options.get(bstack1ll1ll1_opy_ (u"ࠪࡩࡽࡺࡥ࡯ࡵ࡬ࡳࡳࡹࠧ⃶"), [])
                bstack1llll1lllll1_opy_ = bstack1llll1ll1l11_opy_[bstack1ll1ll1_opy_ (u"ࠫࡪࡾࡴࡦࡰࡶ࡭ࡴࡴࡳࠨ⃷")]
                for extension in bstack1llll1lllll1_opy_:
                    if extension not in existing_extensions:
                        chrome_options.add_encoded_extension(extension)
          if bstack1ll1ll1_opy_ (u"ࠬࡶࡲࡦࡨࡶࠫ⃸") in bstack1llll1ll1l11_opy_:
                bstack1llll1lll111_opy_ = chrome_options.experimental_options.get(bstack1ll1ll1_opy_ (u"࠭ࡰࡳࡧࡩࡷࠬ⃹"), {})
                bstack1lllll11lll1_opy_ = bstack1llll1ll1l11_opy_[bstack1ll1ll1_opy_ (u"ࠧࡱࡴࡨࡪࡸ࠭⃺")]
                bstack1111ll1ll1l_opy_(bstack1llll1lll111_opy_, bstack1lllll11lll1_opy_)
                chrome_options.add_experimental_option(bstack1ll1ll1_opy_ (u"ࠨࡲࡵࡩ࡫ࡹࠧ⃻"), bstack1llll1lll111_opy_)
        os.environ[bstack1ll1ll1_opy_ (u"ࠩࡌࡗࡤࡔࡏࡏࡡࡅࡗ࡙ࡇࡃࡌࡡࡌࡒࡋࡘࡁࡠࡃ࠴࠵࡞ࡥࡓࡆࡕࡖࡍࡔࡔࠧ⃼")] = bstack1ll1ll1_opy_ (u"ࠪࡸࡷࡻࡥࠨ⃽")
        return bstack1lll1l11l1_opy_
    except Exception as e:
      logger.error(bstack1ll1ll1_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡯࡬ࡦࠢࡤࡨࡩ࡯࡮ࡨࠢࡱࡳࡳ࠳ࡂࡔࠢ࡬ࡲ࡫ࡸࡡࠡࡣ࠴࠵ࡾࠦࡣࡩࡴࡲࡱࡪࠦ࡯ࡱࡶ࡬ࡳࡳࡹ࠺ࠡࠤ⃾") + str(e))
      return bstack1lll1l11l1_opy_