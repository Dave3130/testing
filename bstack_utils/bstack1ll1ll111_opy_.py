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
import logging
import datetime
import threading
from bstack_utils.helper import bstack111l1ll1l11_opy_, bstack1ll11llll_opy_, get_host_info, bstack1111l1l1111_opy_, \
 bstack1lllllll11_opy_, bstack11lll111_opy_, error_handler, bstack111l1ll1l1l_opy_, bstack1l1ll11l_opy_
import bstack_utils.accessibility as bstack11l1111l_opy_
from bstack_utils.bstack1111ll11_opy_ import bstack111lll1l_opy_
from bstack_utils.bstack1l1l1l1l_opy_ import bstack1l111ll1_opy_
from bstack_utils.percy import bstack111llll1l_opy_
from bstack_utils.config import Config
bstack11l11111_opy_ = Config.bstack1111ll1l_opy_()
logger = logging.getLogger(__name__)
percy = bstack111llll1l_opy_()
@error_handler(class_method=False)
def bstack1llll11ll11l_opy_(bs_config, bstack1l1ll1llll_opy_):
  try:
    data = {
        bstack1l1_opy_ (u"࠭ࡦࡰࡴࡰࡥࡹ࠭∑"): bstack1l1_opy_ (u"ࠧ࡫ࡵࡲࡲࠬ−"),
        bstack1l1_opy_ (u"ࠨࡲࡵࡳ࡯࡫ࡣࡵࡡࡱࡥࡲ࡫ࠧ∓"): bs_config.get(bstack1l1_opy_ (u"ࠩࡳࡶࡴࡰࡥࡤࡶࡑࡥࡲ࡫ࠧ∔"), bstack1l1_opy_ (u"ࠪࠫ∕")),
        bstack1l1_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ∖"): bs_config.get(bstack1l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ∗"), os.path.basename(os.path.abspath(os.getcwd()))),
        bstack1l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡯ࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ∘"): bs_config.get(bstack1l1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ∙")),
        bstack1l1_opy_ (u"ࠨࡦࡨࡷࡨࡸࡩࡱࡶ࡬ࡳࡳ࠭√"): bs_config.get(bstack1l1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡅࡧࡶࡧࡷ࡯ࡰࡵ࡫ࡲࡲࠬ∛"), bstack1l1_opy_ (u"ࠪࠫ∜")),
        bstack1l1_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨ∝"): bstack1l1ll11l_opy_(),
        bstack1l1_opy_ (u"ࠬࡺࡡࡨࡵࠪ∞"): bstack1111l1l1111_opy_(bs_config),
        bstack1l1_opy_ (u"࠭ࡨࡰࡵࡷࡣ࡮ࡴࡦࡰࠩ∟"): get_host_info(),
        bstack1l1_opy_ (u"ࠧࡤ࡫ࡢ࡭ࡳ࡬࡯ࠨ∠"): bstack1ll11llll_opy_(),
        bstack1l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡳࡷࡱࡣ࡮ࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ∡"): os.environ.get(bstack1l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡄࡘࡍࡑࡊ࡟ࡓࡗࡑࡣࡎࡊࡅࡏࡖࡌࡊࡎࡋࡒࠨ∢")),
        bstack1l1_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࡢࡸࡪࡹࡴࡴࡡࡵࡩࡷࡻ࡮ࠨ∣"): os.environ.get(bstack1l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡖࡊࡘࡕࡏࠩ∤"), False),
        bstack1l1_opy_ (u"ࠬࡼࡥࡳࡵ࡬ࡳࡳࡥࡣࡰࡰࡷࡶࡴࡲࠧ∥"): bstack111l1ll1l11_opy_(),
        bstack1l1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭∦"): bstack1llll111l1ll_opy_(bs_config),
        bstack1l1_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡨࡪࡺࡡࡪ࡮ࡶࠫ∧"): bstack1llll1111l1l_opy_(bstack1l1ll1llll_opy_),
        bstack1l1_opy_ (u"ࠨࡲࡵࡳࡩࡻࡣࡵࡡࡰࡥࡵ࠭∨"): bstack1llll111ll11_opy_(bs_config, bstack1l1ll1llll_opy_.get(bstack1l1_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡻࡳࡦࡦࠪ∩"), bstack1l1_opy_ (u"ࠪࠫ∪"))),
        bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭∫"): bstack1lllllll11_opy_(bs_config),
        bstack1l1_opy_ (u"ࠬࡺࡥࡴࡶࡢࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࠪ∬"): bstack1llll111l111_opy_(bs_config)
    }
    return data
  except Exception as error:
    logger.error(bstack1l1_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡺ࡬࡮ࡲࡥࠡࡥࡵࡩࡦࡺࡩ࡯ࡩࠣࡴࡦࡿ࡬ࡰࡣࡧࠤ࡫ࡵࡲࠡࡖࡨࡷࡹࡎࡵࡣ࠼ࠣࠤࢀࢃࠢ∭").format(str(error)))
    return None
def bstack1llll1111l1l_opy_(framework):
  return {
    bstack1l1_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡑࡥࡲ࡫ࠧ∮"): framework.get(bstack1l1_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦࠩ∯"), bstack1l1_opy_ (u"ࠩࡓࡽࡹ࡫ࡳࡵࠩ∰")),
    bstack1l1_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࡜ࡥࡳࡵ࡬ࡳࡳ࠭∱"): framework.get(bstack1l1_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨ∲")),
    bstack1l1_opy_ (u"ࠬࡹࡤ࡬ࡘࡨࡶࡸ࡯࡯࡯ࠩ∳"): framework.get(bstack1l1_opy_ (u"࠭ࡳࡥ࡭ࡢࡺࡪࡸࡳࡪࡱࡱࠫ∴")),
    bstack1l1_opy_ (u"ࠧ࡭ࡣࡱ࡫ࡺࡧࡧࡦࠩ∵"): bstack1l1_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨ∶"),
    bstack1l1_opy_ (u"ࠩࡷࡩࡸࡺࡆࡳࡣࡰࡩࡼࡵࡲ࡬ࠩ∷"): framework.get(bstack1l1_opy_ (u"ࠪࡸࡪࡹࡴࡇࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪ∸"))
  }
def bstack1llll111l111_opy_(bs_config):
  bstack1l1_opy_ (u"ࠦࠧࠨࠊࠡࠢࡕࡩࡹࡻࡲ࡯ࡵࠣࡸ࡭࡫ࠠࡵࡧࡶࡸࠥࡵࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࠥࡪࡡࡵࡣࠣࡪࡴࡸࠠࡣࡷ࡬ࡰࡩࠦࡳࡵࡣࡵࡸ࠳ࠐࠠࠡࠤࠥࠦ∹")
  if not bs_config:
    return {}
  bstack111llll1lll_opy_ = bstack111lll1l_opy_(bs_config).bstack111lllll1l1_opy_(bs_config)
  return bstack111llll1lll_opy_
def bstack1lllll1111_opy_(bs_config, framework):
  bstack1l1lll1l1_opy_ = False
  bstack1ll111l1ll_opy_ = False
  bstack1llll111l11l_opy_ = False
  if bstack1l1_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩ∺") in bs_config:
    bstack1llll111l11l_opy_ = True
  elif bstack1l1_opy_ (u"࠭ࡡࡱࡲࠪ∻") in bs_config:
    bstack1l1lll1l1_opy_ = True
  else:
    bstack1ll111l1ll_opy_ = True
  bstack11lllllll_opy_ = {
    bstack1l1_opy_ (u"ࠧࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠧ∼"): bstack1l111ll1_opy_.bstack11l11l11l1l_opy_(bs_config, framework),
    bstack1l1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ∽"): bstack11l1111l_opy_.bstack1l1l1llll_opy_(bs_config),
    bstack1l1_opy_ (u"ࠩࡳࡩࡷࡩࡹࠨ∾"): bs_config.get(bstack1l1_opy_ (u"ࠪࡴࡪࡸࡣࡺࠩ∿"), False),
    bstack1l1_opy_ (u"ࠫࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭≀"): bstack1ll111l1ll_opy_,
    bstack1l1_opy_ (u"ࠬࡧࡰࡱࡡࡤࡹࡹࡵ࡭ࡢࡶࡨࠫ≁"): bstack1l1lll1l1_opy_,
    bstack1l1_opy_ (u"࠭ࡴࡶࡴࡥࡳࡸࡩࡡ࡭ࡧࠪ≂"): bstack1llll111l11l_opy_
  }
  return bstack11lllllll_opy_
@error_handler(class_method=False)
def bstack1llll111l1ll_opy_(bs_config):
  try:
    bstack1llll111lll1_opy_ = json.loads(os.getenv(bstack1l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡣࡆࡉࡃࡆࡕࡖࡍࡇࡏࡌࡊࡖ࡜ࡣࡈࡕࡎࡇࡋࡊ࡙ࡗࡇࡔࡊࡑࡑࡣ࡞ࡓࡌࠨ≃"), bstack1l1_opy_ (u"ࠨࡽࢀࠫ≄")))
    bstack1llll111lll1_opy_ = bstack1llll111l1l1_opy_(bs_config, bstack1llll111lll1_opy_)
    return {
        bstack1l1_opy_ (u"ࠩࡶࡩࡹࡺࡩ࡯ࡩࡶࠫ≅"): bstack1llll111lll1_opy_
    }
  except Exception as error:
    logger.error(bstack1l1_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡷࡩ࡫࡯ࡩࠥࡩࡲࡦࡣࡷ࡭ࡳ࡭ࠠࡨࡧࡷࡣࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡣࡸ࡫ࡴࡵ࡫ࡱ࡫ࡸࠦࡦࡰࡴࠣࡘࡪࡹࡴࡉࡷࡥ࠾ࠥࠦࡻࡾࠤ≆").format(str(error)))
    return {}
def bstack1llll111l1l1_opy_(bs_config, bstack1llll111lll1_opy_):
  if ((bstack1l1_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨ≇") in bs_config or not bstack1lllllll11_opy_(bs_config)) and bstack11l1111l_opy_.bstack1l1l1llll_opy_(bs_config)):
    bstack1llll111lll1_opy_[bstack1l1_opy_ (u"ࠧ࡯࡮ࡤ࡮ࡸࡨࡪࡋ࡮ࡤࡱࡧࡩࡩࡋࡸࡵࡧࡱࡷ࡮ࡵ࡮ࠣ≈")] = True
  return bstack1llll111lll1_opy_
def bstack1llll11ll111_opy_(array, bstack1llll1111ll1_opy_, bstack1llll11l1111_opy_):
  result = {}
  for o in array:
    key = o[bstack1llll1111ll1_opy_]
    result[key] = o[bstack1llll11l1111_opy_]
  return result
def bstack1llll1l11ll1_opy_(bstack11ll11l11_opy_=bstack1l1_opy_ (u"࠭ࠧ≉")):
  bstack1llll111llll_opy_ = bstack11l1111l_opy_.on()
  bstack1llll11l111l_opy_ = bstack1l111ll1_opy_.on()
  bstack1llll1111lll_opy_ = percy.bstack1l11l11l1l_opy_()
  if bstack1llll1111lll_opy_ and not bstack1llll11l111l_opy_ and not bstack1llll111llll_opy_:
    return bstack11ll11l11_opy_ not in [bstack1l1_opy_ (u"ࠧࡄࡄࡗࡗࡪࡹࡳࡪࡱࡱࡇࡷ࡫ࡡࡵࡧࡧࠫ≊"), bstack1l1_opy_ (u"ࠨࡎࡲ࡫ࡈࡸࡥࡢࡶࡨࡨࠬ≋")]
  elif bstack1llll111llll_opy_ and not bstack1llll11l111l_opy_:
    return bstack11ll11l11_opy_ not in [bstack1l1_opy_ (u"ࠩࡋࡳࡴࡱࡒࡶࡰࡖࡸࡦࡸࡴࡦࡦࠪ≌"), bstack1l1_opy_ (u"ࠪࡌࡴࡵ࡫ࡓࡷࡱࡊ࡮ࡴࡩࡴࡪࡨࡨࠬ≍"), bstack1l1_opy_ (u"ࠫࡑࡵࡧࡄࡴࡨࡥࡹ࡫ࡤࠨ≎")]
  return bstack1llll111llll_opy_ or bstack1llll11l111l_opy_ or bstack1llll1111lll_opy_
@error_handler(class_method=False)
def bstack1llll11l1ll1_opy_(bstack11ll11l11_opy_, test=None):
  bstack1llll111ll1l_opy_ = bstack11l1111l_opy_.on()
  if not bstack1llll111ll1l_opy_ or bstack11ll11l11_opy_ not in [bstack1l1_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳࡌࡩ࡯࡫ࡶ࡬ࡪࡪࠧ≏")] or test == None:
    return None
  return {
    bstack1l1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭≐"): bstack1llll111ll1l_opy_ and bstack11lll111_opy_(threading.current_thread(), bstack1l1_opy_ (u"ࠧࡢ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭≑"), None) == True and bstack11l1111l_opy_.bstack1lll1111ll_opy_(test[bstack1l1_opy_ (u"ࠨࡶࡤ࡫ࡸ࠭≒")])
  }
def bstack1llll111ll11_opy_(bs_config, framework):
  bstack1l1lll1l1_opy_ = False
  bstack1ll111l1ll_opy_ = False
  bstack1llll111l11l_opy_ = False
  if bstack1l1_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭≓") in bs_config:
    bstack1llll111l11l_opy_ = True
  elif bstack1l1_opy_ (u"ࠪࡥࡵࡶࠧ≔") in bs_config:
    bstack1l1lll1l1_opy_ = True
  else:
    bstack1ll111l1ll_opy_ = True
  bstack11lllllll_opy_ = {
    bstack1l1_opy_ (u"ࠫࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠫ≕"): bstack1l111ll1_opy_.bstack11l11l11l1l_opy_(bs_config, framework),
    bstack1l1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ≖"): bstack11l1111l_opy_.bstack11111llll_opy_(bs_config),
    bstack1l1_opy_ (u"࠭ࡰࡦࡴࡦࡽࠬ≗"): bs_config.get(bstack1l1_opy_ (u"ࠧࡱࡧࡵࡧࡾ࠭≘"), False),
    bstack1l1_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵࡧࠪ≙"): bstack1ll111l1ll_opy_,
    bstack1l1_opy_ (u"ࠩࡤࡴࡵࡥࡡࡶࡶࡲࡱࡦࡺࡥࠨ≚"): bstack1l1lll1l1_opy_,
    bstack1l1_opy_ (u"ࠪࡸࡺࡸࡢࡰࡵࡦࡥࡱ࡫ࠧ≛"): bstack1llll111l11l_opy_
  }
  return bstack11lllllll_opy_