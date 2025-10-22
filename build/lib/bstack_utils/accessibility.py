# coding: UTF-8
import sys
bstack1l111_opy_ = sys.version_info [0] == 2
bstack11l111_opy_ = 2048
bstack1l1l_opy_ = 7
def bstack1l111ll_opy_ (bstack1llllll1_opy_):
    global bstack111l1l1_opy_
    bstack1lll111_opy_ = ord (bstack1llllll1_opy_ [-1])
    bstack1ll11l1_opy_ = bstack1llllll1_opy_ [:-1]
    bstack1l11lll_opy_ = bstack1lll111_opy_ % len (bstack1ll11l1_opy_)
    bstack11l1l1_opy_ = bstack1ll11l1_opy_ [:bstack1l11lll_opy_] + bstack1ll11l1_opy_ [bstack1l11lll_opy_:]
    if bstack1l111_opy_:
        bstack11l11l_opy_ = unicode () .join ([unichr (ord (char) - bstack11l111_opy_ - (bstack11l1l1l_opy_ + bstack1lll111_opy_) % bstack1l1l_opy_) for bstack11l1l1l_opy_, char in enumerate (bstack11l1l1_opy_)])
    else:
        bstack11l11l_opy_ = str () .join ([chr (ord (char) - bstack11l111_opy_ - (bstack11l1l1l_opy_ + bstack1lll111_opy_) % bstack1l1l_opy_) for bstack11l1l1l_opy_, char in enumerate (bstack11l1l1_opy_)])
    return eval (bstack11l11l_opy_)
import os
import json
import requests
import logging
import threading
import bstack_utils.constants as bstack1llll1l11lll_opy_
from urllib.parse import urlparse
from bstack_utils.constants import bstack11l11l1ll1l_opy_ as bstack1llll1ll11l1_opy_, EVENTS
from bstack_utils.bstack1ll11l1ll_opy_ import bstack1ll11l1ll_opy_
from bstack_utils.helper import bstack1ll11lll_opy_, bstack1llll1l1_opy_, bstack1111lllll_opy_, bstack1111l1ll1ll_opy_, \
  bstack111l11ll11l_opy_, bstack11ll111lll_opy_, get_host_info, bstack111l1111ll1_opy_, bstack11l1lllll1_opy_, error_handler, bstack1111ll11lll_opy_, bstack111l11llll1_opy_, bstack1l1111ll_opy_
from browserstack_sdk._version import __version__
from bstack_utils.bstack11ll1ll1l_opy_ import get_logger
from bstack_utils.bstack111llll1l_opy_ import bstack1llll11l1ll_opy_
from selenium.webdriver.chrome.options import Options as ChromeOptions
from browserstack_sdk.sdk_cli.cli import cli
from bstack_utils.constants import *
logger = get_logger(__name__)
bstack111llll1l_opy_ = bstack1llll11l1ll_opy_()
@error_handler(class_method=False)
def _1llll1lll11l_opy_(driver, bstack11111ll1_opy_):
  response = {}
  try:
    caps = driver.capabilities
    response = {
        bstack1l111ll_opy_ (u"ࠩࡲࡷࡤࡴࡡ࡮ࡧࠪῤ"): caps.get(bstack1l111ll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡓࡧ࡭ࡦࠩῥ"), None),
        bstack1l111ll_opy_ (u"ࠫࡴࡹ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨῦ"): bstack11111ll1_opy_.get(bstack1l111ll_opy_ (u"ࠬࡵࡳࡗࡧࡵࡷ࡮ࡵ࡮ࠨῧ"), None),
        bstack1l111ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸ࡟࡯ࡣࡰࡩࠬῨ"): caps.get(bstack1l111ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬῩ"), None),
        bstack1l111ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡹࡩࡷࡹࡩࡰࡰࠪῪ"): caps.get(bstack1l111ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪΎ"), None)
    }
  except Exception as error:
    logger.debug(bstack1l111ll_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡩࡩࡹࡩࡨࡪࡰࡪࠤࡵࡲࡡࡵࡨࡲࡶࡲࠦࡤࡦࡶࡤ࡭ࡱࡹࠠࡸ࡫ࡷ࡬ࠥ࡫ࡲࡳࡱࡵࠤ࠿ࠦࠧῬ") + str(error))
  return response
def on():
    if os.environ.get(bstack1l111ll_opy_ (u"ࠫࡇ࡙࡟ࡂ࠳࠴࡝ࡤࡐࡗࡕࠩ῭"), None) is None or os.environ[bstack1l111ll_opy_ (u"ࠬࡈࡓࡠࡃ࠴࠵࡞ࡥࡊࡘࡖࠪ΅")] == bstack1l111ll_opy_ (u"ࠨ࡮ࡶ࡮࡯ࠦ`"):
        return False
    return True
def bstack11ll1llll_opy_(config):
  return config.get(bstack1l111ll_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ῰"), False) or any([p.get(bstack1l111ll_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ῱"), False) == True for p in config.get(bstack1l111ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬῲ"), [])])
def bstack1l11lllll1_opy_(config, bstack111111l11_opy_):
  try:
    bstack1llll1l1ll11_opy_ = config.get(bstack1l111ll_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪῳ"), False)
    if int(bstack111111l11_opy_) < len(config.get(bstack1l111ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧῴ"), [])) and config[bstack1l111ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ῵")][bstack111111l11_opy_]:
      bstack1llll1l1lll1_opy_ = config[bstack1l111ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩῶ")][bstack111111l11_opy_].get(bstack1l111ll_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧῷ"), None)
    else:
      bstack1llll1l1lll1_opy_ = config.get(bstack1l111ll_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨῸ"), None)
    if bstack1llll1l1lll1_opy_ != None:
      bstack1llll1l1ll11_opy_ = bstack1llll1l1lll1_opy_
    bstack1llll1ll11ll_opy_ = os.getenv(bstack1l111ll_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧΌ")) is not None and len(os.getenv(bstack1l111ll_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨῺ"))) > 0 and os.getenv(bstack1l111ll_opy_ (u"ࠫࡇ࡙࡟ࡂ࠳࠴࡝ࡤࡐࡗࡕࠩΏ")) != bstack1l111ll_opy_ (u"ࠬࡴࡵ࡭࡮ࠪῼ")
    return bstack1llll1l1ll11_opy_ and bstack1llll1ll11ll_opy_
  except Exception as error:
    logger.debug(bstack1l111ll_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡼࡥࡳ࡫ࡩࡽ࡮ࡴࡧࠡࡶ࡫ࡩࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡷࡪࡶ࡫ࠤࡪࡸࡲࡰࡴࠣ࠾ࠥ࠭´") + str(error))
  return False
def bstack1ll1ll1ll_opy_(test_tags):
  bstack1l111l11l1l_opy_ = os.getenv(bstack1l111ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡣࡆࡉࡃࡆࡕࡖࡍࡇࡏࡌࡊࡖ࡜ࡣࡈࡕࡎࡇࡋࡊ࡙ࡗࡇࡔࡊࡑࡑࡣ࡞ࡓࡌࠨ῾"))
  if bstack1l111l11l1l_opy_ is None:
    return True
  bstack1l111l11l1l_opy_ = json.loads(bstack1l111l11l1l_opy_)
  try:
    include_tags = bstack1l111l11l1l_opy_[bstack1l111ll_opy_ (u"ࠨ࡫ࡱࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ࠭῿")] if bstack1l111ll_opy_ (u"ࠩ࡬ࡲࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧ ") in bstack1l111l11l1l_opy_ and isinstance(bstack1l111l11l1l_opy_[bstack1l111ll_opy_ (u"ࠪ࡭ࡳࡩ࡬ࡶࡦࡨࡘࡦ࡭ࡳࡊࡰࡗࡩࡸࡺࡩ࡯ࡩࡖࡧࡴࡶࡥࠨ ")], list) else []
    exclude_tags = bstack1l111l11l1l_opy_[bstack1l111ll_opy_ (u"ࠫࡪࡾࡣ࡭ࡷࡧࡩ࡙ࡧࡧࡴࡋࡱࡘࡪࡹࡴࡪࡰࡪࡗࡨࡵࡰࡦࠩ ")] if bstack1l111ll_opy_ (u"ࠬ࡫ࡸࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪ ") in bstack1l111l11l1l_opy_ and isinstance(bstack1l111l11l1l_opy_[bstack1l111ll_opy_ (u"࠭ࡥࡹࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫ ")], list) else []
    excluded = any(tag in exclude_tags for tag in test_tags)
    included = len(include_tags) == 0 or any(tag in include_tags for tag in test_tags)
    return not excluded and included
  except Exception as error:
    logger.debug(bstack1l111ll_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡷࡩ࡫࡯ࡩࠥࡼࡡ࡭࡫ࡧࡥࡹ࡯࡮ࡨࠢࡷࡩࡸࡺࠠࡤࡣࡶࡩࠥ࡬࡯ࡳࠢࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡥࡩ࡫ࡵࡲࡦࠢࡶࡧࡦࡴ࡮ࡪࡰࡪ࠲ࠥࡋࡲࡳࡱࡵࠤ࠿ࠦࠢ ") + str(error))
  return False
def bstack1llll1llll1l_opy_(config, frameworkName, bstack1llll1llllll_opy_, bstack1llll1ll1ll1_opy_):
  bstack1llll1ll1l11_opy_ = bstack1111l1ll1ll_opy_(config)
  bstack1llll1l1l111_opy_ = bstack111l11ll11l_opy_(config)
  if bstack1llll1ll1l11_opy_ is None or bstack1llll1l1l111_opy_ is None:
    logger.error(bstack1l111ll_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡼ࡮ࡩ࡭ࡧࠣࡧࡷ࡫ࡡࡵ࡫ࡱ࡫ࠥࡺࡥࡴࡶࠣࡶࡺࡴࠠࡧࡱࡵࠤࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࠺ࠡࡏ࡬ࡷࡸ࡯࡮ࡨࠢࡤࡹࡹ࡮ࡥ࡯ࡶ࡬ࡧࡦࡺࡩࡰࡰࠣࡸࡴࡱࡥ࡯ࠩ "))
    return [None, None]
  try:
    settings = json.loads(os.getenv(bstack1l111ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡥࡁࡄࡅࡈࡗࡘࡏࡂࡊࡎࡌࡘ࡞ࡥࡃࡐࡐࡉࡍࡌ࡛ࡒࡂࡖࡌࡓࡓࡥ࡙ࡎࡎࠪ "), bstack1l111ll_opy_ (u"ࠪࡿࢂ࠭ ")))
    data = {
        bstack1l111ll_opy_ (u"ࠫࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠩ "): config[bstack1l111ll_opy_ (u"ࠬࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࠪ ")],
        bstack1l111ll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩ​"): config.get(bstack1l111ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪ‌"), os.path.basename(os.getcwd())),
        bstack1l111ll_opy_ (u"ࠨࡵࡷࡥࡷࡺࡔࡪ࡯ࡨࠫ‍"): bstack1ll11lll_opy_(),
        bstack1l111ll_opy_ (u"ࠩࡧࡩࡸࡩࡲࡪࡲࡷ࡭ࡴࡴࠧ‎"): config.get(bstack1l111ll_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡆࡨࡷࡨࡸࡩࡱࡶ࡬ࡳࡳ࠭‏"), bstack1l111ll_opy_ (u"ࠫࠬ‐")),
        bstack1l111ll_opy_ (u"ࠬࡹ࡯ࡶࡴࡦࡩࠬ‑"): {
            bstack1l111ll_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡐࡤࡱࡪ࠭‒"): frameworkName,
            bstack1l111ll_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭࡙ࡩࡷࡹࡩࡰࡰࠪ–"): bstack1llll1llllll_opy_,
            bstack1l111ll_opy_ (u"ࠨࡵࡧ࡯࡛࡫ࡲࡴ࡫ࡲࡲࠬ—"): __version__,
            bstack1l111ll_opy_ (u"ࠩ࡯ࡥࡳ࡭ࡵࡢࡩࡨࠫ―"): bstack1l111ll_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪ‖"),
            bstack1l111ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡈࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫ‗"): bstack1l111ll_opy_ (u"ࠬࡹࡥ࡭ࡧࡱ࡭ࡺࡳࠧ‘"),
            bstack1l111ll_opy_ (u"࠭ࡴࡦࡵࡷࡊࡷࡧ࡭ࡦࡹࡲࡶࡰ࡜ࡥࡳࡵ࡬ࡳࡳ࠭’"): bstack1llll1ll1ll1_opy_
        },
        bstack1l111ll_opy_ (u"ࠧࡴࡧࡷࡸ࡮ࡴࡧࡴࠩ‚"): settings,
        bstack1l111ll_opy_ (u"ࠨࡸࡨࡶࡸ࡯࡯࡯ࡅࡲࡲࡹࡸ࡯࡭ࠩ‛"): bstack111l1111ll1_opy_(),
        bstack1l111ll_opy_ (u"ࠩࡦ࡭ࡎࡴࡦࡰࠩ“"): bstack11ll111lll_opy_(),
        bstack1l111ll_opy_ (u"ࠪ࡬ࡴࡹࡴࡊࡰࡩࡳࠬ”"): get_host_info(),
        bstack1l111ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭„"): bstack1111lllll_opy_(config)
    }
    headers = {
        bstack1l111ll_opy_ (u"ࠬࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡔࡺࡲࡨࠫ‟"): bstack1l111ll_opy_ (u"࠭ࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳࡯ࡹ࡯࡯ࠩ†"),
    }
    config = {
        bstack1l111ll_opy_ (u"ࠧࡢࡷࡷ࡬ࠬ‡"): (bstack1llll1ll1l11_opy_, bstack1llll1l1l111_opy_),
        bstack1l111ll_opy_ (u"ࠨࡪࡨࡥࡩ࡫ࡲࡴࠩ•"): headers
    }
    response = bstack11l1lllll1_opy_(bstack1l111ll_opy_ (u"ࠩࡓࡓࡘ࡚ࠧ‣"), bstack1llll1ll11l1_opy_ + bstack1l111ll_opy_ (u"ࠪ࠳ࡻ࠸࠯ࡵࡧࡶࡸࡤࡸࡵ࡯ࡵࠪ․"), data, config)
    bstack1llll1l11ll1_opy_ = response.json()
    if bstack1llll1l11ll1_opy_[bstack1l111ll_opy_ (u"ࠫࡸࡻࡣࡤࡧࡶࡷࠬ‥")]:
      parsed = json.loads(os.getenv(bstack1l111ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡡࡄࡇࡈࡋࡓࡔࡋࡅࡍࡑࡏࡔ࡚ࡡࡆࡓࡓࡌࡉࡈࡗࡕࡅ࡙ࡏࡏࡏࡡ࡜ࡑࡑ࠭…"), bstack1l111ll_opy_ (u"࠭ࡻࡾࠩ‧")))
      parsed[bstack1l111ll_opy_ (u"ࠧࡴࡥࡤࡲࡳ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨ ")] = bstack1llll1l11ll1_opy_[bstack1l111ll_opy_ (u"ࠨࡦࡤࡸࡦ࠭ ")][bstack1l111ll_opy_ (u"ࠩࡶࡧࡦࡴ࡮ࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪ‪")]
      os.environ[bstack1l111ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚࡟ࡂࡅࡆࡉࡘ࡙ࡉࡃࡋࡏࡍ࡙࡟࡟ࡄࡑࡑࡊࡎࡍࡕࡓࡃࡗࡍࡔࡔ࡟࡚ࡏࡏࠫ‫")] = json.dumps(parsed)
      bstack1ll11l1ll_opy_.bstack11l1l1lll_opy_(bstack1llll1l11ll1_opy_[bstack1l111ll_opy_ (u"ࠫࡩࡧࡴࡢࠩ‬")][bstack1l111ll_opy_ (u"ࠬࡹࡣࡳ࡫ࡳࡸࡸ࠭‭")])
      bstack1ll11l1ll_opy_.bstack1lllll1111ll_opy_(bstack1llll1l11ll1_opy_[bstack1l111ll_opy_ (u"࠭ࡤࡢࡶࡤࠫ‮")][bstack1l111ll_opy_ (u"ࠧࡤࡱࡰࡱࡦࡴࡤࡴࠩ ")])
      bstack1ll11l1ll_opy_.store()
      return bstack1llll1l11ll1_opy_[bstack1l111ll_opy_ (u"ࠨࡦࡤࡸࡦ࠭‰")][bstack1l111ll_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡖࡲ࡯ࡪࡴࠧ‱")], bstack1llll1l11ll1_opy_[bstack1l111ll_opy_ (u"ࠪࡨࡦࡺࡡࠨ′")][bstack1l111ll_opy_ (u"ࠫ࡮ࡪࠧ″")]
    else:
      logger.error(bstack1l111ll_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡹ࡫࡭ࡱ࡫ࠠࡳࡷࡱࡲ࡮ࡴࡧࠡࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱ࠾ࠥ࠭‴") + bstack1llll1l11ll1_opy_[bstack1l111ll_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ‵")])
      if bstack1llll1l11ll1_opy_[bstack1l111ll_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ‶")] == bstack1l111ll_opy_ (u"ࠨࡋࡱࡺࡦࡲࡩࡥࠢࡦࡳࡳ࡬ࡩࡨࡷࡵࡥࡹ࡯࡯࡯ࠢࡳࡥࡸࡹࡥࡥ࠰ࠪ‷"):
        for bstack1llll1l1llll_opy_ in bstack1llll1l11ll1_opy_[bstack1l111ll_opy_ (u"ࠩࡨࡶࡷࡵࡲࡴࠩ‸")]:
          logger.error(bstack1llll1l1llll_opy_[bstack1l111ll_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ‹")])
      return None, None
  except Exception as error:
    logger.error(bstack1l111ll_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡸࡪ࡬ࡰࡪࠦࡣࡳࡧࡤࡸ࡮ࡴࡧࠡࡶࡨࡷࡹࠦࡲࡶࡰࠣࡪࡴࡸࠠࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰ࠽ࠤࠧ›") +  str(error))
    return None, None
def bstack1lllll11111l_opy_():
  if os.getenv(bstack1l111ll_opy_ (u"ࠬࡈࡓࡠࡃ࠴࠵࡞ࡥࡊࡘࡖࠪ※")) is None:
    return {
        bstack1l111ll_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭‼"): bstack1l111ll_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭‽"),
        bstack1l111ll_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ‾"): bstack1l111ll_opy_ (u"ࠩࡅࡹ࡮ࡲࡤࠡࡥࡵࡩࡦࡺࡩࡰࡰࠣ࡬ࡦࡪࠠࡧࡣ࡬ࡰࡪࡪ࠮ࠨ‿")
    }
  data = {bstack1l111ll_opy_ (u"ࠪࡩࡳࡪࡔࡪ࡯ࡨࠫ⁀"): bstack1ll11lll_opy_()}
  headers = {
      bstack1l111ll_opy_ (u"ࠫࡆࡻࡴࡩࡱࡵ࡭ࡿࡧࡴࡪࡱࡱࠫ⁁"): bstack1l111ll_opy_ (u"ࠬࡈࡥࡢࡴࡨࡶࠥ࠭⁂") + os.getenv(bstack1l111ll_opy_ (u"ࠨࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗࠦ⁃")),
      bstack1l111ll_opy_ (u"ࠧࡄࡱࡱࡸࡪࡴࡴ࠮ࡖࡼࡴࡪ࠭⁄"): bstack1l111ll_opy_ (u"ࠨࡣࡳࡴࡱ࡯ࡣࡢࡶ࡬ࡳࡳ࠵ࡪࡴࡱࡱࠫ⁅")
  }
  response = bstack11l1lllll1_opy_(bstack1l111ll_opy_ (u"ࠩࡓ࡙࡙࠭⁆"), bstack1llll1ll11l1_opy_ + bstack1l111ll_opy_ (u"ࠪ࠳ࡹ࡫ࡳࡵࡡࡵࡹࡳࡹ࠯ࡴࡶࡲࡴࠬ⁇"), data, { bstack1l111ll_opy_ (u"ࠫ࡭࡫ࡡࡥࡧࡵࡷࠬ⁈"): headers })
  try:
    if response.status_code == 200:
      logger.info(bstack1l111ll_opy_ (u"ࠧࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡖࡨࡷࡹࠦࡒࡶࡰࠣࡱࡦࡸ࡫ࡦࡦࠣࡥࡸࠦࡣࡰ࡯ࡳࡰࡪࡺࡥࡥࠢࡤࡸࠥࠨ⁉") + bstack1llll1l1_opy_().isoformat() + bstack1l111ll_opy_ (u"࡚࠭ࠨ⁊"))
      return {bstack1l111ll_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧ⁋"): bstack1l111ll_opy_ (u"ࠨࡵࡸࡧࡨ࡫ࡳࡴࠩ⁌"), bstack1l111ll_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ⁍"): bstack1l111ll_opy_ (u"ࠪࠫ⁎")}
    else:
      response.raise_for_status()
  except requests.RequestException as error:
    logger.error(bstack1l111ll_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡸࡪ࡬ࡰࡪࠦ࡭ࡢࡴ࡮࡭ࡳ࡭ࠠࡤࡱࡰࡴࡱ࡫ࡴࡪࡱࡱࠤࡴ࡬ࠠࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡘࡪࡹࡴࠡࡔࡸࡲ࠿ࠦࠢ⁏") + str(error))
    return {
        bstack1l111ll_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬ⁐"): bstack1l111ll_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬ⁑"),
        bstack1l111ll_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ⁒"): str(error)
    }
def bstack1llll1lll1l1_opy_(bstack1llll1ll1l1l_opy_):
    return re.match(bstack1l111ll_opy_ (u"ࡳࠩࡡࡠࡩ࠱ࠨ࡝࠰࡟ࡨ࠰࠯࠿ࠥࠩ⁓"), bstack1llll1ll1l1l_opy_.strip()) is not None
def bstack11ll1l11l1_opy_(caps, options, desired_capabilities={}, config=None):
    try:
        if options:
          bstack1llll1l1l11l_opy_ = options.to_capabilities()
        elif desired_capabilities:
          bstack1llll1l1l11l_opy_ = desired_capabilities
        else:
          bstack1llll1l1l11l_opy_ = {}
        bstack1l111l11ll1_opy_ = (bstack1llll1l1l11l_opy_.get(bstack1l111ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡒࡦࡳࡥࠨ⁔"), bstack1l111ll_opy_ (u"ࠪࠫ⁕")).lower() or caps.get(bstack1l111ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡔࡡ࡮ࡧࠪ⁖"), bstack1l111ll_opy_ (u"ࠬ࠭⁗")).lower())
        if bstack1l111l11ll1_opy_ == bstack1l111ll_opy_ (u"࠭ࡩࡰࡵࠪ⁘"):
            return True
        if bstack1l111l11ll1_opy_ == bstack1l111ll_opy_ (u"ࠧࡢࡰࡧࡶࡴ࡯ࡤࠨ⁙"):
            bstack1l1111ll1l1_opy_ = str(float(caps.get(bstack1l111ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࡙ࡩࡷࡹࡩࡰࡰࠪ⁚")) or bstack1llll1l1l11l_opy_.get(bstack1l111ll_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪ⁛"), {}).get(bstack1l111ll_opy_ (u"ࠪࡳࡸ࡜ࡥࡳࡵ࡬ࡳࡳ࠭⁜"),bstack1l111ll_opy_ (u"ࠫࠬ⁝"))))
            if bstack1l111l11ll1_opy_ == bstack1l111ll_opy_ (u"ࠬࡧ࡮ࡥࡴࡲ࡭ࡩ࠭⁞") and int(bstack1l1111ll1l1_opy_.split(bstack1l111ll_opy_ (u"࠭࠮ࠨ "))[0]) < float(bstack11l11ll1ll1_opy_):
                logger.warning(str(bstack11l11lll111_opy_))
                return False
            return True
        bstack1l111l11lll_opy_ = caps.get(bstack1l111ll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨ⁠"), {}).get(bstack1l111ll_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࡏࡣࡰࡩࠬ⁡"), caps.get(bstack1l111ll_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࠩ⁢"), bstack1l111ll_opy_ (u"ࠪࠫ⁣")))
        if bstack1l111l11lll_opy_:
            logger.warning(bstack1l111ll_opy_ (u"ࠦࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡹ࡬ࡰࡱࠦࡲࡶࡰࠣࡳࡳࡲࡹࠡࡱࡱࠤࡉ࡫ࡳ࡬ࡶࡲࡴࠥࡨࡲࡰࡹࡶࡩࡷࡹ࠮ࠣ⁤"))
            return False
        browser = caps.get(bstack1l111ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪ⁥"), bstack1l111ll_opy_ (u"࠭ࠧ⁦")).lower() or bstack1llll1l1l11l_opy_.get(bstack1l111ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬ⁧"), bstack1l111ll_opy_ (u"ࠨࠩ⁨")).lower()
        if browser != bstack1l111ll_opy_ (u"ࠩࡦ࡬ࡷࡵ࡭ࡦࠩ⁩"):
            logger.warning(bstack1l111ll_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡸ࡫࡯ࡰࠥࡸࡵ࡯ࠢࡲࡲࡱࡿࠠࡰࡰࠣࡇ࡭ࡸ࡯࡮ࡧࠣࡦࡷࡵࡷࡴࡧࡵࡷ࠳ࠨ⁪"))
            return False
        browser_version = caps.get(bstack1l111ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬ⁫")) or caps.get(bstack1l111ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡥࡶࡦࡴࡶ࡭ࡴࡴࠧ⁬")) or bstack1llll1l1l11l_opy_.get(bstack1l111ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧ⁭")) or bstack1llll1l1l11l_opy_.get(bstack1l111ll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨ⁮"), {}).get(bstack1l111ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩ⁯")) or bstack1llll1l1l11l_opy_.get(bstack1l111ll_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪ⁰"), {}).get(bstack1l111ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬⁱ"))
        bstack1l1111llll1_opy_ = bstack1llll1l11lll_opy_.bstack1l11111llll_opy_
        bstack1llll1l1l1ll_opy_ = False
        if config is not None:
          bstack1llll1l1l1ll_opy_ = bstack1l111ll_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨ⁲") in config and str(config[bstack1l111ll_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩ⁳")]).lower() != bstack1l111ll_opy_ (u"࠭ࡦࡢ࡮ࡶࡩࠬ⁴")
        if os.environ.get(bstack1l111ll_opy_ (u"ࠧࡊࡕࡢࡒࡔࡔ࡟ࡃࡕࡗࡅࡈࡑ࡟ࡊࡐࡉࡖࡆࡥࡁ࠲࠳࡜ࡣࡘࡋࡓࡔࡋࡒࡒࠬ⁵"), bstack1l111ll_opy_ (u"ࠨࠩ⁶")).lower() == bstack1l111ll_opy_ (u"ࠩࡷࡶࡺ࡫ࠧ⁷") or bstack1llll1l1l1ll_opy_:
          bstack1l1111llll1_opy_ = bstack1llll1l11lll_opy_.bstack1l11111ll11_opy_
        if browser_version and browser_version != bstack1l111ll_opy_ (u"ࠪࡰࡦࡺࡥࡴࡶࠪ⁸") and int(browser_version.split(bstack1l111ll_opy_ (u"ࠫ࠳࠭⁹"))[0]) <= bstack1l1111llll1_opy_:
          logger.warning(bstack1lll11lllll_opy_ (u"ࠬࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡺ࡭ࡱࡲࠠࡳࡷࡱࠤࡴࡴ࡬ࡺࠢࡲࡲࠥࡉࡨࡳࡱࡰࡩࠥࡨࡲࡰࡹࡶࡩࡷࠦࡶࡦࡴࡶ࡭ࡴࡴࠠࡨࡴࡨࡥࡹ࡫ࡲࠡࡶ࡫ࡥࡳࠦࡻ࡮࡫ࡱࡣࡦ࠷࠱ࡺࡡࡶࡹࡵࡶ࡯ࡳࡶࡨࡨࡤࡩࡨࡳࡱࡰࡩࡤࡼࡥࡳࡵ࡬ࡳࡳࢃ࠮ࠨ⁺"))
          return False
        if not options:
          bstack1l111l11111_opy_ = caps.get(bstack1l111ll_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫ⁻")) or bstack1llll1l1l11l_opy_.get(bstack1l111ll_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬ⁼"), {})
          if bstack1l111ll_opy_ (u"ࠨ࠯࠰࡬ࡪࡧࡤ࡭ࡧࡶࡷࠬ⁽") in bstack1l111l11111_opy_.get(bstack1l111ll_opy_ (u"ࠩࡤࡶ࡬ࡹࠧ⁾"), []):
              logger.warning(bstack1l111ll_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡸ࡫࡯ࡰࠥࡴ࡯ࡵࠢࡵࡹࡳࠦ࡯࡯ࠢ࡯ࡩ࡬ࡧࡣࡺࠢ࡫ࡩࡦࡪ࡬ࡦࡵࡶࠤࡲࡵࡤࡦ࠰ࠣࡗࡼ࡯ࡴࡤࡪࠣࡸࡴࠦ࡮ࡦࡹࠣ࡬ࡪࡧࡤ࡭ࡧࡶࡷࠥࡳ࡯ࡥࡧࠣࡳࡷࠦࡡࡷࡱ࡬ࡨࠥࡻࡳࡪࡰࡪࠤ࡭࡫ࡡࡥ࡮ࡨࡷࡸࠦ࡭ࡰࡦࡨ࠲ࠧⁿ"))
              return False
        return True
    except Exception as error:
        logger.debug(bstack1l111ll_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡺࡦࡲࡩࡥࡣࡷࡩࠥࡧ࠱࠲ࡻࠣࡷࡺࡶࡰࡰࡴࡷࠤ࠿ࠨ₀") + str(error))
        return False
def set_capabilities(caps, config):
  try:
    bstack1l1l1l11111_opy_ = config.get(bstack1l111ll_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬ₁"), {})
    bstack1l1l1l11111_opy_[bstack1l111ll_opy_ (u"࠭ࡡࡶࡶ࡫ࡘࡴࡱࡥ࡯ࠩ₂")] = os.getenv(bstack1l111ll_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠬ₃"))
    bstack111l1l1lll1_opy_ = json.loads(os.getenv(bstack1l111ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡤࡇࡃࡄࡇࡖࡗࡎࡈࡉࡍࡋࡗ࡝ࡤࡉࡏࡏࡈࡌࡋ࡚ࡘࡁࡕࡋࡒࡒࡤ࡟ࡍࡍࠩ₄"), bstack1l111ll_opy_ (u"ࠩࡾࢁࠬ₅"))).get(bstack1l111ll_opy_ (u"ࠪࡷࡨࡧ࡮࡯ࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫ₆"))
    if not config[bstack1l111ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡓࡶࡴࡪࡵࡤࡶࡐࡥࡵ࠭₇")].get(bstack1l111ll_opy_ (u"ࠧࡧࡰࡱࡡࡤࡹࡹࡵ࡭ࡢࡶࡨࠦ₈")):
      if bstack1l111ll_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧ₉") in caps:
        caps[bstack1l111ll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨ₊")][bstack1l111ll_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨ₋")] = bstack1l1l1l11111_opy_
        caps[bstack1l111ll_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪ₌")][bstack1l111ll_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪ₍")][bstack1l111ll_opy_ (u"ࠫࡸࡩࡡ࡯ࡰࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬ₎")] = bstack111l1l1lll1_opy_
      else:
        caps[bstack1l111ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫ₏")] = bstack1l1l1l11111_opy_
        caps[bstack1l111ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬₐ")][bstack1l111ll_opy_ (u"ࠧࡴࡥࡤࡲࡳ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨₑ")] = bstack111l1l1lll1_opy_
  except Exception as error:
    logger.debug(bstack1l111ll_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡼ࡮ࡩ࡭ࡧࠣࡷࡪࡺࡴࡪࡰࡪࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹ࠮ࠡࡇࡵࡶࡴࡸ࠺ࠡࠤₒ") +  str(error))
def bstack1l1ll1ll1l_opy_(driver, bstack1llll1lllll1_opy_):
  try:
    setattr(driver, bstack1l111ll_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡃ࠴࠵ࡾ࡙ࡨࡰࡷ࡯ࡨࡘࡩࡡ࡯ࠩₓ"), True)
    session = driver.session_id
    if session:
      bstack1llll1l1ll1l_opy_ = True
      current_url = driver.current_url
      try:
        url = urlparse(current_url)
      except Exception as e:
        bstack1llll1l1ll1l_opy_ = False
      bstack1llll1l1ll1l_opy_ = url.scheme in [bstack1l111ll_opy_ (u"ࠥ࡬ࡹࡺࡰࠣₔ"), bstack1l111ll_opy_ (u"ࠦ࡭ࡺࡴࡱࡵࠥₕ")]
      if bstack1llll1l1ll1l_opy_:
        if bstack1llll1lllll1_opy_:
          logger.info(bstack1l111ll_opy_ (u"࡙ࠧࡥࡵࡷࡳࠤ࡫ࡵࡲࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡶࡨࡷࡹ࡯࡮ࡨࠢ࡫ࡥࡸࠦࡳࡵࡣࡵࡸࡪࡪ࠮ࠡࡃࡸࡸࡴࡳࡡࡵࡧࠣࡸࡪࡹࡴࠡࡥࡤࡷࡪࠦࡥࡹࡧࡦࡹࡹ࡯࡯࡯ࠢࡺ࡭ࡱࡲࠠࡣࡧࡪ࡭ࡳࠦ࡭ࡰ࡯ࡨࡲࡹࡧࡲࡪ࡮ࡼ࠲ࠧₖ"))
      return bstack1llll1lllll1_opy_
  except Exception as e:
    logger.error(bstack1l111ll_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡹࡴࡢࡴࡷ࡭ࡳ࡭ࠠࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡸࡩࡡ࡯ࠢࡩࡳࡷࠦࡴࡩ࡫ࡶࠤࡹ࡫ࡳࡵࠢࡦࡥࡸ࡫࠺ࠡࠤₗ") + str(e))
    return False
def bstack1111111l_opy_(driver, name, path):
  try:
    bstack1l111l111ll_opy_ = {
        bstack1l111ll_opy_ (u"ࠧࡵࡪࡗࡩࡸࡺࡒࡶࡰࡘࡹ࡮ࡪࠧₘ"): threading.current_thread().current_test_uuid,
        bstack1l111ll_opy_ (u"ࠨࡶ࡫ࡆࡺ࡯࡬ࡥࡗࡸ࡭ࡩ࠭ₙ"): os.environ.get(bstack1l111ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧₚ"), bstack1l111ll_opy_ (u"ࠪࠫₛ")),
        bstack1l111ll_opy_ (u"ࠫࡹ࡮ࡊࡸࡶࡗࡳࡰ࡫࡮ࠨₜ"): os.environ.get(bstack1l111ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩ₝"), bstack1l111ll_opy_ (u"࠭ࠧ₞"))
    }
    bstack1ll111ll111_opy_ = bstack111llll1l_opy_.bstack1ll1l11l1ll_opy_(EVENTS.bstack11l1ll11l_opy_.value)
    logger.debug(bstack1l111ll_opy_ (u"ࠧࡑࡧࡵࡪࡴࡸ࡭ࡪࡰࡪࠤࡸࡩࡡ࡯ࠢࡥࡩ࡫ࡵࡲࡦࠢࡶࡥࡻ࡯࡮ࡨࠢࡵࡩࡸࡻ࡬ࡵࡵࠪ₟"))
    try:
      if (bstack1l1111ll_opy_(threading.current_thread(), bstack1l111ll_opy_ (u"ࠨ࡫ࡶࡅࡵࡶࡁ࠲࠳ࡼࡘࡪࡹࡴࠨ₠"), None) and bstack1l1111ll_opy_(threading.current_thread(), bstack1l111ll_opy_ (u"ࠩࡤࡴࡵࡇ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫ₡"), None)):
        scripts = {bstack1l111ll_opy_ (u"ࠪࡷࡨࡧ࡮ࠨ₢"): bstack1ll11l1ll_opy_.perform_scan}
        bstack1lllll1111l1_opy_ = json.loads(scripts[bstack1l111ll_opy_ (u"ࠦࡸࡩࡡ࡯ࠤ₣")].replace(bstack1l111ll_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࠣ₤"), bstack1l111ll_opy_ (u"ࠨࠢ₥")))
        bstack1lllll1111l1_opy_[bstack1l111ll_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪ₦")][bstack1l111ll_opy_ (u"ࠨ࡯ࡨࡸ࡭ࡵࡤࠨ₧")] = None
        scripts[bstack1l111ll_opy_ (u"ࠤࡶࡧࡦࡴࠢ₨")] = bstack1l111ll_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࠨ₩") + json.dumps(bstack1lllll1111l1_opy_)
        bstack1ll11l1ll_opy_.bstack11l1l1lll_opy_(scripts)
        bstack1ll11l1ll_opy_.store()
        logger.debug(driver.execute_script(bstack1ll11l1ll_opy_.perform_scan))
      else:
        logger.debug(driver.execute_async_script(bstack1ll11l1ll_opy_.perform_scan, {bstack1l111ll_opy_ (u"ࠦࡲ࡫ࡴࡩࡱࡧࠦ₪"): name}))
      bstack111llll1l_opy_.end(EVENTS.bstack11l1ll11l_opy_.value, bstack1ll111ll111_opy_ + bstack1l111ll_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧ₫"), bstack1ll111ll111_opy_ + bstack1l111ll_opy_ (u"ࠨ࠺ࡦࡰࡧࠦ€"), True, None)
    except Exception as error:
      bstack111llll1l_opy_.end(EVENTS.bstack11l1ll11l_opy_.value, bstack1ll111ll111_opy_ + bstack1l111ll_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢ₭"), bstack1ll111ll111_opy_ + bstack1l111ll_opy_ (u"ࠣ࠼ࡨࡲࡩࠨ₮"), False, str(error))
    bstack1ll111ll111_opy_ = bstack111llll1l_opy_.bstack11ll1l11ll1_opy_(EVENTS.bstack1l1111l1l11_opy_.value)
    bstack111llll1l_opy_.mark(bstack1ll111ll111_opy_ + bstack1l111ll_opy_ (u"ࠤ࠽ࡷࡹࡧࡲࡵࠤ₯"))
    try:
      if (bstack1l1111ll_opy_(threading.current_thread(), bstack1l111ll_opy_ (u"ࠪ࡭ࡸࡇࡰࡱࡃ࠴࠵ࡾ࡚ࡥࡴࡶࠪ₰"), None) and bstack1l1111ll_opy_(threading.current_thread(), bstack1l111ll_opy_ (u"ࠫࡦࡶࡰࡂ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭₱"), None)):
        scripts = {bstack1l111ll_opy_ (u"ࠬࡹࡣࡢࡰࠪ₲"): bstack1ll11l1ll_opy_.perform_scan}
        bstack1lllll1111l1_opy_ = json.loads(scripts[bstack1l111ll_opy_ (u"ࠨࡳࡤࡣࡱࠦ₳")].replace(bstack1l111ll_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࠥ₴"), bstack1l111ll_opy_ (u"ࠣࠤ₵")))
        bstack1lllll1111l1_opy_[bstack1l111ll_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬ₶")][bstack1l111ll_opy_ (u"ࠪࡱࡪࡺࡨࡰࡦࠪ₷")] = None
        scripts[bstack1l111ll_opy_ (u"ࠦࡸࡩࡡ࡯ࠤ₸")] = bstack1l111ll_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࠣ₹") + json.dumps(bstack1lllll1111l1_opy_)
        bstack1ll11l1ll_opy_.bstack11l1l1lll_opy_(scripts)
        bstack1ll11l1ll_opy_.store()
        logger.debug(driver.execute_script(bstack1ll11l1ll_opy_.perform_scan))
      else:
        logger.debug(driver.execute_async_script(bstack1ll11l1ll_opy_.bstack1lllll11l11l_opy_, bstack1l111l111ll_opy_))
      bstack111llll1l_opy_.end(bstack1ll111ll111_opy_, bstack1ll111ll111_opy_ + bstack1l111ll_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨ₺"), bstack1ll111ll111_opy_ + bstack1l111ll_opy_ (u"ࠢ࠻ࡧࡱࡨࠧ₻"),True, None)
    except Exception as error:
      bstack111llll1l_opy_.end(bstack1ll111ll111_opy_, bstack1ll111ll111_opy_ + bstack1l111ll_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣ₼"), bstack1ll111ll111_opy_ + bstack1l111ll_opy_ (u"ࠤ࠽ࡩࡳࡪࠢ₽"),False, str(error))
    logger.info(bstack1l111ll_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡸࡪࡹࡴࡪࡰࡪࠤ࡫ࡵࡲࠡࡶ࡫࡭ࡸࠦࡴࡦࡵࡷࠤࡨࡧࡳࡦࠢ࡫ࡥࡸࠦࡥ࡯ࡦࡨࡨ࠳ࠨ₾"))
  except Exception as bstack1l1111l1l1l_opy_:
    logger.error(bstack1l111ll_opy_ (u"ࠦࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡷ࡫ࡳࡶ࡮ࡷࡷࠥࡩ࡯ࡶ࡮ࡧࠤࡳࡵࡴࠡࡤࡨࠤࡵࡸ࡯ࡤࡧࡶࡷࡪࡪࠠࡧࡱࡵࠤࡹ࡮ࡥࠡࡶࡨࡷࡹࠦࡣࡢࡵࡨ࠾ࠥࠨ₿") + str(path) + bstack1l111ll_opy_ (u"ࠧࠦࡅࡳࡴࡲࡶࠥࡀࠢ⃀") + str(bstack1l1111l1l1l_opy_))
def bstack1lllll111111_opy_(driver):
    caps = driver.capabilities
    if caps.get(bstack1l111ll_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡏࡣࡰࡩࠧ⃁")) and str(caps.get(bstack1l111ll_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡐࡤࡱࡪࠨ⃂"))).lower() == bstack1l111ll_opy_ (u"ࠣࡣࡱࡨࡷࡵࡩࡥࠤ⃃"):
        bstack1l1111ll1l1_opy_ = caps.get(bstack1l111ll_opy_ (u"ࠤࡤࡴࡵ࡯ࡵ࡮࠼ࡳࡰࡦࡺࡦࡰࡴࡰ࡚ࡪࡸࡳࡪࡱࡱࠦ⃄")) or caps.get(bstack1l111ll_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠧ⃅"))
        if bstack1l1111ll1l1_opy_ and int(str(bstack1l1111ll1l1_opy_)) < bstack11l11ll1ll1_opy_:
            return False
    return True
def bstack1l1l11l11_opy_(config):
  if bstack1l111ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ⃆") in config:
        return config[bstack1l111ll_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ⃇")]
  for platform in config.get(bstack1l111ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ⃈"), []):
      if bstack1l111ll_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ⃉") in platform:
          return platform[bstack1l111ll_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ⃊")]
  return None
def bstack111l11ll11_opy_(bstack1ll1l1111_opy_):
  try:
    browser_name = bstack1ll1l1111_opy_[bstack1l111ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡲࡦࡳࡥࠨ⃋")]
    browser_version = bstack1ll1l1111_opy_[bstack1l111ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬ⃌")]
    chrome_options = bstack1ll1l1111_opy_[bstack1l111ll_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࡣࡴࡶࡴࡪࡱࡱࡷࠬ⃍")]
    try:
        bstack1llll1ll1111_opy_ = int(browser_version.split(bstack1l111ll_opy_ (u"ࠬ࠴ࠧ⃎"))[0])
    except ValueError as e:
        logger.error(bstack1l111ll_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡽࡨࡪ࡮ࡨࠤࡨࡵ࡮ࡷࡧࡵࡸ࡮ࡴࡧࠡࡤࡵࡳࡼࡹࡥࡳࠢࡹࡩࡷࡹࡩࡰࡰࠥ⃏") + str(e))
        return False
    if not (browser_name and browser_name.lower() == bstack1l111ll_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࠧ⃐")):
        logger.warning(bstack1l111ll_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡽࡩ࡭࡮ࠣࡶࡺࡴࠠࡰࡰ࡯ࡽࠥࡵ࡮ࠡࡅ࡫ࡶࡴࡳࡥࠡࡤࡵࡳࡼࡹࡥࡳࡵ࠱ࠦ⃑"))
        return False
    if bstack1llll1ll1111_opy_ < bstack1llll1l11lll_opy_.bstack1l11111ll11_opy_:
        logger.warning(bstack1lll11lllll_opy_ (u"ࠩࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡲࡦࡳࡸ࡭ࡷ࡫ࡳࠡࡅ࡫ࡶࡴࡳࡥࠡࡸࡨࡶࡸ࡯࡯࡯ࠢࡾࡇࡔࡔࡓࡕࡃࡑࡘࡘ࠴ࡍࡊࡐࡌࡑ࡚ࡓ࡟ࡏࡑࡑࡣࡇ࡙ࡔࡂࡅࡎࡣࡎࡔࡆࡓࡃࡢࡅ࠶࠷࡙ࡠࡕࡘࡔࡕࡕࡒࡕࡇࡇࡣࡈࡎࡒࡐࡏࡈࡣ࡛ࡋࡒࡔࡋࡒࡒࢂࠦ࡯ࡳࠢ࡫࡭࡬࡮ࡥࡳ࠰⃒ࠪ"))
        return False
    if chrome_options and any(bstack1l111ll_opy_ (u"ࠪ࠱࠲࡮ࡥࡢࡦ࡯ࡩࡸࡹ⃓ࠧ") in value for value in chrome_options.values() if isinstance(value, str)):
        logger.warning(bstack1l111ll_opy_ (u"ࠦࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡹ࡬ࡰࡱࠦ࡮ࡰࡶࠣࡶࡺࡴࠠࡰࡰࠣࡰࡪ࡭ࡡࡤࡻࠣ࡬ࡪࡧࡤ࡭ࡧࡶࡷࠥࡳ࡯ࡥࡧ࠱ࠤࡘࡽࡩࡵࡥ࡫ࠤࡹࡵࠠ࡯ࡧࡺࠤ࡭࡫ࡡࡥ࡮ࡨࡷࡸࠦ࡭ࡰࡦࡨࠤࡴࡸࠠࡢࡸࡲ࡭ࡩࠦࡵࡴ࡫ࡱ࡫ࠥ࡮ࡥࡢࡦ࡯ࡩࡸࡹࠠ࡮ࡱࡧࡩ࠳ࠨ⃔"))
        return False
    return True
  except Exception as e:
    logger.error(bstack1l111ll_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡤࡪࡨࡧࡰ࡯࡮ࡨࠢࡳࡰࡦࡺࡦࡰࡴࡰࠤࡸࡻࡰࡱࡱࡵࡸࠥ࡬࡯ࡳࠢ࡯ࡳࡨࡧ࡬ࠡࡅ࡫ࡶࡴࡳࡥ࠻ࠢࠥ⃕") + str(e))
    return False
def bstack1111111ll_opy_(bstack11l111l11l_opy_, config):
    try:
      bstack1l111l1l1l1_opy_ = bstack1l111ll_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭⃖") in config and config[bstack1l111ll_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ⃗")] == True
      bstack1llll1l1l1ll_opy_ = bstack1l111ll_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩ⃘ࠬ") in config and str(config[bstack1l111ll_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ⃙࠭")]).lower() != bstack1l111ll_opy_ (u"ࠪࡪࡦࡲࡳࡦ⃚ࠩ")
      if not (bstack1l111l1l1l1_opy_ and (not bstack1111lllll_opy_(config) or bstack1llll1l1l1ll_opy_)):
        return bstack11l111l11l_opy_
      bstack1llll1ll1lll_opy_ = bstack1ll11l1ll_opy_.bstack1lllll111lll_opy_
      if bstack1llll1ll1lll_opy_ is None:
        logger.debug(bstack1l111ll_opy_ (u"ࠦࡌࡵ࡯ࡨ࡮ࡨࠤࡨ࡮ࡲࡰ࡯ࡨࠤࡴࡶࡴࡪࡱࡱࡷࠥࡧࡲࡦࠢࡑࡳࡳ࡫ࠢ⃛"))
        return bstack11l111l11l_opy_
      bstack1llll1lll1ll_opy_ = int(str(bstack111l11llll1_opy_()).split(bstack1l111ll_opy_ (u"ࠬ࠴ࠧ⃜"))[0])
      logger.debug(bstack1l111ll_opy_ (u"ࠨࡓࡦ࡮ࡨࡲ࡮ࡻ࡭ࠡࡸࡨࡶࡸ࡯࡯࡯ࠢࡧࡩࡹ࡫ࡣࡵࡧࡧ࠾ࠥࠨ⃝") + str(bstack1llll1lll1ll_opy_) + bstack1l111ll_opy_ (u"ࠢࠣ⃞"))
      if bstack1llll1lll1ll_opy_ == 3 and isinstance(bstack11l111l11l_opy_, dict) and bstack1l111ll_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨ⃟") in bstack11l111l11l_opy_ and bstack1llll1ll1lll_opy_ is not None:
        if bstack1l111ll_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ⃠") not in bstack11l111l11l_opy_[bstack1l111ll_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪ⃡")]:
          bstack11l111l11l_opy_[bstack1l111ll_opy_ (u"ࠫࡩ࡫ࡳࡪࡴࡨࡨࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠫ⃢")][bstack1l111ll_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ⃣")] = {}
        if bstack1l111ll_opy_ (u"࠭ࡡࡳࡩࡶࠫ⃤") in bstack1llll1ll1lll_opy_:
          if bstack1l111ll_opy_ (u"ࠧࡢࡴࡪࡷ⃥ࠬ") not in bstack11l111l11l_opy_[bstack1l111ll_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨ⃦")][bstack1l111ll_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ⃧")]:
            bstack11l111l11l_opy_[bstack1l111ll_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵ⃨ࠪ")][bstack1l111ll_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩ⃩")][bstack1l111ll_opy_ (u"ࠬࡧࡲࡨࡵ⃪ࠪ")] = []
          for arg in bstack1llll1ll1lll_opy_[bstack1l111ll_opy_ (u"࠭ࡡࡳࡩࡶ⃫ࠫ")]:
            if arg not in bstack11l111l11l_opy_[bstack1l111ll_opy_ (u"ࠧࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹ⃬ࠧ")][bstack1l111ll_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ⃭࠭")][bstack1l111ll_opy_ (u"ࠩࡤࡶ࡬ࡹ⃮ࠧ")]:
              bstack11l111l11l_opy_[bstack1l111ll_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵ⃯ࠪ")][bstack1l111ll_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩ⃰")][bstack1l111ll_opy_ (u"ࠬࡧࡲࡨࡵࠪ⃱")].append(arg)
        if bstack1l111ll_opy_ (u"࠭ࡥࡹࡶࡨࡲࡸ࡯࡯࡯ࡵࠪ⃲") in bstack1llll1ll1lll_opy_:
          if bstack1l111ll_opy_ (u"ࠧࡦࡺࡷࡩࡳࡹࡩࡰࡰࡶࠫ⃳") not in bstack11l111l11l_opy_[bstack1l111ll_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨ⃴")][bstack1l111ll_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ⃵")]:
            bstack11l111l11l_opy_[bstack1l111ll_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪ⃶")][bstack1l111ll_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩ⃷")][bstack1l111ll_opy_ (u"ࠬ࡫ࡸࡵࡧࡱࡷ࡮ࡵ࡮ࡴࠩ⃸")] = []
          for ext in bstack1llll1ll1lll_opy_[bstack1l111ll_opy_ (u"࠭ࡥࡹࡶࡨࡲࡸ࡯࡯࡯ࡵࠪ⃹")]:
            if ext not in bstack11l111l11l_opy_[bstack1l111ll_opy_ (u"ࠧࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠧ⃺")][bstack1l111ll_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭⃻")][bstack1l111ll_opy_ (u"ࠩࡨࡼࡹ࡫࡮ࡴ࡫ࡲࡲࡸ࠭⃼")]:
              bstack11l111l11l_opy_[bstack1l111ll_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪ⃽")][bstack1l111ll_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩ⃾")][bstack1l111ll_opy_ (u"ࠬ࡫ࡸࡵࡧࡱࡷ࡮ࡵ࡮ࡴࠩ⃿")].append(ext)
        if bstack1l111ll_opy_ (u"࠭ࡰࡳࡧࡩࡷࠬ℀") in bstack1llll1ll1lll_opy_:
          if bstack1l111ll_opy_ (u"ࠧࡱࡴࡨࡪࡸ࠭℁") not in bstack11l111l11l_opy_[bstack1l111ll_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨℂ")][bstack1l111ll_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ℃")]:
            bstack11l111l11l_opy_[bstack1l111ll_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪ℄")][bstack1l111ll_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩ℅")][bstack1l111ll_opy_ (u"ࠬࡶࡲࡦࡨࡶࠫ℆")] = {}
          bstack1111ll11lll_opy_(bstack11l111l11l_opy_[bstack1l111ll_opy_ (u"࠭ࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠭ℇ")][bstack1l111ll_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬ℈")][bstack1l111ll_opy_ (u"ࠨࡲࡵࡩ࡫ࡹࠧ℉")],
                    bstack1llll1ll1lll_opy_[bstack1l111ll_opy_ (u"ࠩࡳࡶࡪ࡬ࡳࠨℊ")])
        os.environ[bstack1l111ll_opy_ (u"ࠪࡍࡘࡥࡎࡐࡐࡢࡆࡘ࡚ࡁࡄࡍࡢࡍࡓࡌࡒࡂࡡࡄ࠵࠶࡟࡟ࡔࡇࡖࡗࡎࡕࡎࠨℋ")] = bstack1l111ll_opy_ (u"ࠫࡹࡸࡵࡦࠩℌ")
        return bstack11l111l11l_opy_
      else:
        chrome_options = None
        if isinstance(bstack11l111l11l_opy_, ChromeOptions):
          chrome_options = bstack11l111l11l_opy_
        elif isinstance(bstack11l111l11l_opy_, dict):
          for value in bstack11l111l11l_opy_.values():
            if isinstance(value, ChromeOptions):
              chrome_options = value
              break
        if chrome_options is None:
          chrome_options = ChromeOptions()
          if isinstance(bstack11l111l11l_opy_, dict):
            bstack11l111l11l_opy_[bstack1l111ll_opy_ (u"ࠬࡵࡰࡵ࡫ࡲࡲࡸ࠭ℍ")] = chrome_options
          else:
            bstack11l111l11l_opy_ = chrome_options
        if bstack1llll1ll1lll_opy_ is not None:
          if bstack1l111ll_opy_ (u"࠭ࡡࡳࡩࡶࠫℎ") in bstack1llll1ll1lll_opy_:
                bstack1llll1llll11_opy_ = chrome_options.arguments or []
                new_args = bstack1llll1ll1lll_opy_[bstack1l111ll_opy_ (u"ࠧࡢࡴࡪࡷࠬℏ")]
                for arg in new_args:
                    if arg not in bstack1llll1llll11_opy_:
                        chrome_options.add_argument(arg)
          if bstack1l111ll_opy_ (u"ࠨࡧࡻࡸࡪࡴࡳࡪࡱࡱࡷࠬℐ") in bstack1llll1ll1lll_opy_:
                existing_extensions = chrome_options.experimental_options.get(bstack1l111ll_opy_ (u"ࠩࡨࡼࡹ࡫࡮ࡴ࡫ࡲࡲࡸ࠭ℑ"), [])
                bstack1llll1l1l1l1_opy_ = bstack1llll1ll1lll_opy_[bstack1l111ll_opy_ (u"ࠪࡩࡽࡺࡥ࡯ࡵ࡬ࡳࡳࡹࠧℒ")]
                for extension in bstack1llll1l1l1l1_opy_:
                    if extension not in existing_extensions:
                        chrome_options.add_encoded_extension(extension)
          if bstack1l111ll_opy_ (u"ࠫࡵࡸࡥࡧࡵࠪℓ") in bstack1llll1ll1lll_opy_:
                bstack1llll1lll111_opy_ = chrome_options.experimental_options.get(bstack1l111ll_opy_ (u"ࠬࡶࡲࡦࡨࡶࠫ℔"), {})
                bstack1llll1ll111l_opy_ = bstack1llll1ll1lll_opy_[bstack1l111ll_opy_ (u"࠭ࡰࡳࡧࡩࡷࠬℕ")]
                bstack1111ll11lll_opy_(bstack1llll1lll111_opy_, bstack1llll1ll111l_opy_)
                chrome_options.add_experimental_option(bstack1l111ll_opy_ (u"ࠧࡱࡴࡨࡪࡸ࠭№"), bstack1llll1lll111_opy_)
        os.environ[bstack1l111ll_opy_ (u"ࠨࡋࡖࡣࡓࡕࡎࡠࡄࡖࡘࡆࡉࡋࡠࡋࡑࡊࡗࡇ࡟ࡂ࠳࠴࡝ࡤ࡙ࡅࡔࡕࡌࡓࡓ࠭℗")] = bstack1l111ll_opy_ (u"ࠩࡷࡶࡺ࡫ࠧ℘")
        return bstack11l111l11l_opy_
    except Exception as e:
      logger.error(bstack1l111ll_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡺ࡬࡮ࡲࡥࠡࡣࡧࡨ࡮ࡴࡧࠡࡰࡲࡲ࠲ࡈࡓࠡ࡫ࡱࡪࡷࡧࠠࡢ࠳࠴ࡽࠥࡩࡨࡳࡱࡰࡩࠥࡵࡰࡵ࡫ࡲࡲࡸࡀࠠࠣℙ") + str(e))
      return bstack11l111l11l_opy_