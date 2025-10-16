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
import logging
import datetime
import threading
from bstack_utils.helper import bstack1111ll111ll_opy_, bstack1l11l1l11l_opy_, get_host_info, bstack111l1ll11ll_opy_, \
 bstack111lll111l_opy_, bstack1ll1ll11_opy_, error_handler, bstack111ll11111l_opy_, bstack1lll1111_opy_
import bstack_utils.accessibility as bstack11l11lll_opy_
from bstack_utils.bstack1lll1ll1l_opy_ import bstack11l11l1l_opy_
from bstack_utils.bstack1llll1l1_opy_ import bstack1l11l1ll_opy_
from bstack_utils.percy import bstack1l1l11l1l_opy_
from bstack_utils.config import Config
bstack1111ll11_opy_ = Config.bstack1llll11l1_opy_()
logger = logging.getLogger(__name__)
percy = bstack1l1l11l1l_opy_()
@error_handler(class_method=False)
def bstack1llll1l1111l_opy_(bs_config, bstack111l1l1l1l_opy_):
  try:
    data = {
        bstack1ll11_opy_ (u"ࠪࡪࡴࡸ࡭ࡢࡶࠪ⇹"): bstack1ll11_opy_ (u"ࠫ࡯ࡹ࡯࡯ࠩ⇺"),
        bstack1ll11_opy_ (u"ࠬࡶࡲࡰ࡬ࡨࡧࡹࡥ࡮ࡢ࡯ࡨࠫ⇻"): bs_config.get(bstack1ll11_opy_ (u"࠭ࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠫ⇼"), bstack1ll11_opy_ (u"ࠧࠨ⇽")),
        bstack1ll11_opy_ (u"ࠨࡰࡤࡱࡪ࠭⇾"): bs_config.get(bstack1ll11_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ⇿"), os.path.basename(os.path.abspath(os.getcwd()))),
        bstack1ll11_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡ࡬ࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭∀"): bs_config.get(bstack1ll11_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭∁")),
        bstack1ll11_opy_ (u"ࠬࡪࡥࡴࡥࡵ࡭ࡵࡺࡩࡰࡰࠪ∂"): bs_config.get(bstack1ll11_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡉ࡫ࡳࡤࡴ࡬ࡴࡹ࡯࡯࡯ࠩ∃"), bstack1ll11_opy_ (u"ࠧࠨ∄")),
        bstack1ll11_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬ∅"): bstack1lll1111_opy_(),
        bstack1ll11_opy_ (u"ࠩࡷࡥ࡬ࡹࠧ∆"): bstack111l1ll11ll_opy_(bs_config),
        bstack1ll11_opy_ (u"ࠪ࡬ࡴࡹࡴࡠ࡫ࡱࡪࡴ࠭∇"): get_host_info(),
        bstack1ll11_opy_ (u"ࠫࡨ࡯࡟ࡪࡰࡩࡳࠬ∈"): bstack1l11l1l11l_opy_(),
        bstack1ll11_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣࡷࡻ࡮ࡠ࡫ࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ∉"): os.environ.get(bstack1ll11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡈࡕࡊࡎࡇࡣࡗ࡛ࡎࡠࡋࡇࡉࡓ࡚ࡉࡇࡋࡈࡖࠬ∊")),
        bstack1ll11_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪ࡟ࡵࡧࡶࡸࡸࡥࡲࡦࡴࡸࡲࠬ∋"): os.environ.get(bstack1ll11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡓࡇࡕ࡙ࡓ࠭∌"), False),
        bstack1ll11_opy_ (u"ࠩࡹࡩࡷࡹࡩࡰࡰࡢࡧࡴࡴࡴࡳࡱ࡯ࠫ∍"): bstack1111ll111ll_opy_(),
        bstack1ll11_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ∎"): bstack1llll111lll1_opy_(bs_config),
        bstack1ll11_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡥࡧࡷࡥ࡮ࡲࡳࠨ∏"): bstack1llll111llll_opy_(bstack111l1l1l1l_opy_),
        bstack1ll11_opy_ (u"ࠬࡶࡲࡰࡦࡸࡧࡹࡥ࡭ࡢࡲࠪ∐"): bstack1llll11l1111_opy_(bs_config, bstack111l1l1l1l_opy_.get(bstack1ll11_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡸࡷࡪࡪࠧ∑"), bstack1ll11_opy_ (u"ࠧࠨ−"))),
        bstack1ll11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠪ∓"): bstack111lll111l_opy_(bs_config),
        bstack1ll11_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡰࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴࠧ∔"): bstack1llll11ll1l1_opy_(bs_config)
    }
    return data
  except Exception as error:
    logger.error(bstack1ll11_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡷࡩ࡫࡯ࡩࠥࡩࡲࡦࡣࡷ࡭ࡳ࡭ࠠࡱࡣࡼࡰࡴࡧࡤࠡࡨࡲࡶ࡚ࠥࡥࡴࡶࡋࡹࡧࡀࠠࠡࡽࢀࠦ∕").format(str(error)))
    return None
def bstack1llll111llll_opy_(framework):
  return {
    bstack1ll11_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࡎࡢ࡯ࡨࠫ∖"): framework.get(bstack1ll11_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪ࠭∗"), bstack1ll11_opy_ (u"࠭ࡐࡺࡶࡨࡷࡹ࠭∘")),
    bstack1ll11_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭࡙ࡩࡷࡹࡩࡰࡰࠪ∙"): framework.get(bstack1ll11_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬ√")),
    bstack1ll11_opy_ (u"ࠩࡶࡨࡰ࡜ࡥࡳࡵ࡬ࡳࡳ࠭∛"): framework.get(bstack1ll11_opy_ (u"ࠪࡷࡩࡱ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨ∜")),
    bstack1ll11_opy_ (u"ࠫࡱࡧ࡮ࡨࡷࡤ࡫ࡪ࠭∝"): bstack1ll11_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬ∞"),
    bstack1ll11_opy_ (u"࠭ࡴࡦࡵࡷࡊࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭∟"): framework.get(bstack1ll11_opy_ (u"ࠧࡵࡧࡶࡸࡋࡸࡡ࡮ࡧࡺࡳࡷࡱࠧ∠"))
  }
def bstack1llll11ll1l1_opy_(bs_config):
  bstack1ll11_opy_ (u"ࠣࠤࠥࠎࠥࠦࡒࡦࡶࡸࡶࡳࡹࠠࡵࡪࡨࠤࡹ࡫ࡳࡵࠢࡲࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯ࠢࡧࡥࡹࡧࠠࡧࡱࡵࠤࡧࡻࡩ࡭ࡦࠣࡷࡹࡧࡲࡵ࠰ࠍࠤࠥࠨࠢࠣ∡")
  if not bs_config:
    return {}
  bstack11l1111llll_opy_ = bstack11l11l1l_opy_(bs_config).bstack11l111ll11l_opy_(bs_config)
  return bstack11l1111llll_opy_
def bstack1111l1lll_opy_(bs_config, framework):
  bstack11l11ll11l_opy_ = False
  bstack111ll11l1_opy_ = False
  bstack1llll11l1ll1_opy_ = False
  if bstack1ll11_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭∢") in bs_config:
    bstack1llll11l1ll1_opy_ = True
  elif bstack1ll11_opy_ (u"ࠪࡥࡵࡶࠧ∣") in bs_config:
    bstack11l11ll11l_opy_ = True
  else:
    bstack111ll11l1_opy_ = True
  bstack11llll1ll1_opy_ = {
    bstack1ll11_opy_ (u"ࠫࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠫ∤"): bstack1l11l1ll_opy_.bstack11l11l1llll_opy_(bs_config, framework),
    bstack1ll11_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ∥"): bstack11l11lll_opy_.bstack1ll1llll11_opy_(bs_config),
    bstack1ll11_opy_ (u"࠭ࡰࡦࡴࡦࡽࠬ∦"): bs_config.get(bstack1ll11_opy_ (u"ࠧࡱࡧࡵࡧࡾ࠭∧"), False),
    bstack1ll11_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵࡧࠪ∨"): bstack111ll11l1_opy_,
    bstack1ll11_opy_ (u"ࠩࡤࡴࡵࡥࡡࡶࡶࡲࡱࡦࡺࡥࠨ∩"): bstack11l11ll11l_opy_,
    bstack1ll11_opy_ (u"ࠪࡸࡺࡸࡢࡰࡵࡦࡥࡱ࡫ࠧ∪"): bstack1llll11l1ll1_opy_
  }
  return bstack11llll1ll1_opy_
@error_handler(class_method=False)
def bstack1llll111lll1_opy_(bs_config):
  try:
    bstack1llll11ll11l_opy_ = json.loads(os.getenv(bstack1ll11_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡠࡃࡆࡇࡊ࡙ࡓࡊࡄࡌࡐࡎ࡚࡙ࡠࡅࡒࡒࡋࡏࡇࡖࡔࡄࡘࡎࡕࡎࡠ࡛ࡐࡐࠬ∫"), bstack1ll11_opy_ (u"ࠬࢁࡽࠨ∬")))
    bstack1llll11ll11l_opy_ = bstack1llll11l11ll_opy_(bs_config, bstack1llll11ll11l_opy_)
    return {
        bstack1ll11_opy_ (u"࠭ࡳࡦࡶࡷ࡭ࡳ࡭ࡳࠨ∭"): bstack1llll11ll11l_opy_
    }
  except Exception as error:
    logger.error(bstack1ll11_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡻ࡭࡯࡬ࡦࠢࡦࡶࡪࡧࡴࡪࡰࡪࠤ࡬࡫ࡴࡠࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡠࡵࡨࡸࡹ࡯࡮ࡨࡵࠣࡪࡴࡸࠠࡕࡧࡶࡸࡍࡻࡢ࠻ࠢࠣࡿࢂࠨ∮").format(str(error)))
    return {}
def bstack1llll11l11ll_opy_(bs_config, bstack1llll11ll11l_opy_):
  if ((bstack1ll11_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬ∯") in bs_config or not bstack111lll111l_opy_(bs_config)) and bstack11l11lll_opy_.bstack1ll1llll11_opy_(bs_config)):
    bstack1llll11ll11l_opy_[bstack1ll11_opy_ (u"ࠤ࡬ࡲࡨࡲࡵࡥࡧࡈࡲࡨࡵࡤࡦࡦࡈࡼࡹ࡫࡮ࡴ࡫ࡲࡲࠧ∰")] = True
  return bstack1llll11ll11l_opy_
def bstack1llll11lll11_opy_(array, bstack1llll11l11l1_opy_, bstack1llll11l1l1l_opy_):
  result = {}
  for o in array:
    key = o[bstack1llll11l11l1_opy_]
    result[key] = o[bstack1llll11l1l1l_opy_]
  return result
def bstack1llll11lll1l_opy_(bstack1l11ll11ll_opy_=bstack1ll11_opy_ (u"ࠪࠫ∱")):
  bstack1llll11l1l11_opy_ = bstack11l11lll_opy_.on()
  bstack1llll11l1lll_opy_ = bstack1l11l1ll_opy_.on()
  bstack1llll11l111l_opy_ = percy.bstack1l1l1llll_opy_()
  if bstack1llll11l111l_opy_ and not bstack1llll11l1lll_opy_ and not bstack1llll11l1l11_opy_:
    return bstack1l11ll11ll_opy_ not in [bstack1ll11_opy_ (u"ࠫࡈࡈࡔࡔࡧࡶࡷ࡮ࡵ࡮ࡄࡴࡨࡥࡹ࡫ࡤࠨ∲"), bstack1ll11_opy_ (u"ࠬࡒ࡯ࡨࡅࡵࡩࡦࡺࡥࡥࠩ∳")]
  elif bstack1llll11l1l11_opy_ and not bstack1llll11l1lll_opy_:
    return bstack1l11ll11ll_opy_ not in [bstack1ll11_opy_ (u"࠭ࡈࡰࡱ࡮ࡖࡺࡴࡓࡵࡣࡵࡸࡪࡪࠧ∴"), bstack1ll11_opy_ (u"ࠧࡉࡱࡲ࡯ࡗࡻ࡮ࡇ࡫ࡱ࡭ࡸ࡮ࡥࡥࠩ∵"), bstack1ll11_opy_ (u"ࠨࡎࡲ࡫ࡈࡸࡥࡢࡶࡨࡨࠬ∶")]
  return bstack1llll11l1l11_opy_ or bstack1llll11l1lll_opy_ or bstack1llll11l111l_opy_
@error_handler(class_method=False)
def bstack1llll11ll1ll_opy_(bstack1l11ll11ll_opy_, test=None):
  bstack1llll11ll111_opy_ = bstack11l11lll_opy_.on()
  if not bstack1llll11ll111_opy_ or bstack1l11ll11ll_opy_ not in [bstack1ll11_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫ∷")] or test == None:
    return None
  return {
    bstack1ll11_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ∸"): bstack1llll11ll111_opy_ and bstack1ll1ll11_opy_(threading.current_thread(), bstack1ll11_opy_ (u"ࠫࡦ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪ∹"), None) == True and bstack11l11lll_opy_.bstack1llllll1l1_opy_(test[bstack1ll11_opy_ (u"ࠬࡺࡡࡨࡵࠪ∺")])
  }
def bstack1llll11l1111_opy_(bs_config, framework):
  bstack11l11ll11l_opy_ = False
  bstack111ll11l1_opy_ = False
  bstack1llll11l1ll1_opy_ = False
  if bstack1ll11_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪ∻") in bs_config:
    bstack1llll11l1ll1_opy_ = True
  elif bstack1ll11_opy_ (u"ࠧࡢࡲࡳࠫ∼") in bs_config:
    bstack11l11ll11l_opy_ = True
  else:
    bstack111ll11l1_opy_ = True
  bstack11llll1ll1_opy_ = {
    bstack1ll11_opy_ (u"ࠨࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨ∽"): bstack1l11l1ll_opy_.bstack11l11l1llll_opy_(bs_config, framework),
    bstack1ll11_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ∾"): bstack11l11lll_opy_.bstack11l11ll11_opy_(bs_config),
    bstack1ll11_opy_ (u"ࠪࡴࡪࡸࡣࡺࠩ∿"): bs_config.get(bstack1ll11_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࠪ≀"), False),
    bstack1ll11_opy_ (u"ࠬࡧࡵࡵࡱࡰࡥࡹ࡫ࠧ≁"): bstack111ll11l1_opy_,
    bstack1ll11_opy_ (u"࠭ࡡࡱࡲࡢࡥࡺࡺ࡯࡮ࡣࡷࡩࠬ≂"): bstack11l11ll11l_opy_,
    bstack1ll11_opy_ (u"ࠧࡵࡷࡵࡦࡴࡹࡣࡢ࡮ࡨࠫ≃"): bstack1llll11l1ll1_opy_
  }
  return bstack11llll1ll1_opy_