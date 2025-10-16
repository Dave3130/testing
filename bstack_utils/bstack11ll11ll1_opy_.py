# coding: UTF-8
import sys
bstack1llllll_opy_ = sys.version_info [0] == 2
bstack11l1l1l_opy_ = 2048
bstack1111ll_opy_ = 7
def bstack1lllll1_opy_ (bstack1l1_opy_):
    global bstack111ll11_opy_
    bstackl_opy_ = ord (bstack1l1_opy_ [-1])
    bstack1l1l_opy_ = bstack1l1_opy_ [:-1]
    bstack111ll_opy_ = bstackl_opy_ % len (bstack1l1l_opy_)
    bstack111l_opy_ = bstack1l1l_opy_ [:bstack111ll_opy_] + bstack1l1l_opy_ [bstack111ll_opy_:]
    if bstack1llllll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
import os
import json
import logging
import datetime
import threading
from bstack_utils.helper import bstack111l1llll1l_opy_, bstack1ll111111l_opy_, get_host_info, bstack1111l1l1ll1_opy_, \
 bstack11ll11111_opy_, bstack1lll1l11_opy_, error_handler, bstack1111lll11l1_opy_, bstack1llll11l_opy_
import bstack_utils.accessibility as bstack1lll1lll1_opy_
from bstack_utils.bstack1111l1l1_opy_ import bstack11l111ll_opy_
from bstack_utils.bstack1ll1ll1l_opy_ import bstack1llll111_opy_
from bstack_utils.percy import bstack1ll1l1ll1l_opy_
from bstack_utils.config import Config
bstack11l1111l_opy_ = Config.bstack11111l1l_opy_()
logger = logging.getLogger(__name__)
percy = bstack1ll1l1ll1l_opy_()
@error_handler(class_method=False)
def bstack1llll1l11lll_opy_(bs_config, bstack1llll111l1_opy_):
  try:
    data = {
        bstack1lllll1_opy_ (u"ࠫ࡫ࡵࡲ࡮ࡣࡷࠫ⇺"): bstack1lllll1_opy_ (u"ࠬࡰࡳࡰࡰࠪ⇻"),
        bstack1lllll1_opy_ (u"࠭ࡰࡳࡱ࡭ࡩࡨࡺ࡟࡯ࡣࡰࡩࠬ⇼"): bs_config.get(bstack1lllll1_opy_ (u"ࠧࡱࡴࡲ࡮ࡪࡩࡴࡏࡣࡰࡩࠬ⇽"), bstack1lllll1_opy_ (u"ࠨࠩ⇾")),
        bstack1lllll1_opy_ (u"ࠩࡱࡥࡲ࡫ࠧ⇿"): bs_config.get(bstack1lllll1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭∀"), os.path.basename(os.path.abspath(os.getcwd()))),
        bstack1lllll1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢ࡭ࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ∁"): bs_config.get(bstack1lllll1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ∂")),
        bstack1lllll1_opy_ (u"࠭ࡤࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࠫ∃"): bs_config.get(bstack1lllll1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡊࡥࡴࡥࡵ࡭ࡵࡺࡩࡰࡰࠪ∄"), bstack1lllll1_opy_ (u"ࠨࠩ∅")),
        bstack1lllll1_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭∆"): bstack1llll11l_opy_(),
        bstack1lllll1_opy_ (u"ࠪࡸࡦ࡭ࡳࠨ∇"): bstack1111l1l1ll1_opy_(bs_config),
        bstack1lllll1_opy_ (u"ࠫ࡭ࡵࡳࡵࡡ࡬ࡲ࡫ࡵࠧ∈"): get_host_info(),
        bstack1lllll1_opy_ (u"ࠬࡩࡩࡠ࡫ࡱࡪࡴ࠭∉"): bstack1ll111111l_opy_(),
        bstack1lllll1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤࡸࡵ࡯ࡡ࡬ࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭∊"): os.environ.get(bstack1lllll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡂࡖࡋࡏࡈࡤࡘࡕࡏࡡࡌࡈࡊࡔࡔࡊࡈࡌࡉࡗ࠭∋")),
        bstack1lllll1_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࡠࡶࡨࡷࡹࡹ࡟ࡳࡧࡵࡹࡳ࠭∌"): os.environ.get(bstack1lllll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡔࡈࡖ࡚ࡔࠧ∍"), False),
        bstack1lllll1_opy_ (u"ࠪࡺࡪࡸࡳࡪࡱࡱࡣࡨࡵ࡮ࡵࡴࡲࡰࠬ∎"): bstack111l1llll1l_opy_(),
        bstack1lllll1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ∏"): bstack1llll11ll1l1_opy_(bs_config),
        bstack1lllll1_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡦࡨࡸࡦ࡯࡬ࡴࠩ∐"): bstack1llll111lll1_opy_(bstack1llll111l1_opy_),
        bstack1lllll1_opy_ (u"࠭ࡰࡳࡱࡧࡹࡨࡺ࡟࡮ࡣࡳࠫ∑"): bstack1llll11l11l1_opy_(bs_config, bstack1llll111l1_opy_.get(bstack1lllll1_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡹࡸ࡫ࡤࠨ−"), bstack1lllll1_opy_ (u"ࠨࠩ∓"))),
        bstack1lllll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫ∔"): bstack11ll11111_opy_(bs_config),
        bstack1lllll1_opy_ (u"ࠪࡸࡪࡹࡴࡠࡱࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࠨ∕"): bstack1llll11l1111_opy_(bs_config)
    }
    return data
  except Exception as error:
    logger.error(bstack1lllll1_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡸࡪ࡬ࡰࡪࠦࡣࡳࡧࡤࡸ࡮ࡴࡧࠡࡲࡤࡽࡱࡵࡡࡥࠢࡩࡳࡷࠦࡔࡦࡵࡷࡌࡺࡨ࠺ࠡࠢࡾࢁࠧ∖").format(str(error)))
    return None
def bstack1llll111lll1_opy_(framework):
  return {
    bstack1lllll1_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡏࡣࡰࡩࠬ∗"): framework.get(bstack1lllll1_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫ࠧ∘"), bstack1lllll1_opy_ (u"ࠧࡑࡻࡷࡩࡸࡺࠧ∙")),
    bstack1lllll1_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮࡚ࡪࡸࡳࡪࡱࡱࠫ√"): framework.get(bstack1lllll1_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭∛")),
    bstack1lllll1_opy_ (u"ࠪࡷࡩࡱࡖࡦࡴࡶ࡭ࡴࡴࠧ∜"): framework.get(bstack1lllll1_opy_ (u"ࠫࡸࡪ࡫ࡠࡸࡨࡶࡸ࡯࡯࡯ࠩ∝")),
    bstack1lllll1_opy_ (u"ࠬࡲࡡ࡯ࡩࡸࡥ࡬࡫ࠧ∞"): bstack1lllll1_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭∟"),
    bstack1lllll1_opy_ (u"ࠧࡵࡧࡶࡸࡋࡸࡡ࡮ࡧࡺࡳࡷࡱࠧ∠"): framework.get(bstack1lllll1_opy_ (u"ࠨࡶࡨࡷࡹࡌࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨ∡"))
  }
def bstack1llll11l1111_opy_(bs_config):
  bstack1lllll1_opy_ (u"ࠤࠥࠦࠏࠦࠠࡓࡧࡷࡹࡷࡴࡳࠡࡶ࡫ࡩࠥࡺࡥࡴࡶࠣࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࠣࡨࡦࡺࡡࠡࡨࡲࡶࠥࡨࡵࡪ࡮ࡧࠤࡸࡺࡡࡳࡶ࠱ࠎࠥࠦࠢࠣࠤ∢")
  if not bs_config:
    return {}
  bstack11l111ll1l1_opy_ = bstack11l111ll_opy_(bs_config).bstack11l111l11ll_opy_(bs_config)
  return bstack11l111ll1l1_opy_
def bstack1lll1111ll_opy_(bs_config, framework):
  bstack1l11l11ll1_opy_ = False
  bstack11ll1ll11_opy_ = False
  bstack1llll11ll11l_opy_ = False
  if bstack1lllll1_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧ∣") in bs_config:
    bstack1llll11ll11l_opy_ = True
  elif bstack1lllll1_opy_ (u"ࠫࡦࡶࡰࠨ∤") in bs_config:
    bstack1l11l11ll1_opy_ = True
  else:
    bstack11ll1ll11_opy_ = True
  bstack1l1l1l1l11_opy_ = {
    bstack1lllll1_opy_ (u"ࠬࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬ∥"): bstack1llll111_opy_.bstack11l11l1l11l_opy_(bs_config, framework),
    bstack1lllll1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭∦"): bstack1lll1lll1_opy_.bstack1l1lllll1_opy_(bs_config),
    bstack1lllll1_opy_ (u"ࠧࡱࡧࡵࡧࡾ࠭∧"): bs_config.get(bstack1lllll1_opy_ (u"ࠨࡲࡨࡶࡨࡿࠧ∨"), False),
    bstack1lllll1_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶࡨࠫ∩"): bstack11ll1ll11_opy_,
    bstack1lllll1_opy_ (u"ࠪࡥࡵࡶ࡟ࡢࡷࡷࡳࡲࡧࡴࡦࠩ∪"): bstack1l11l11ll1_opy_,
    bstack1lllll1_opy_ (u"ࠫࡹࡻࡲࡣࡱࡶࡧࡦࡲࡥࠨ∫"): bstack1llll11ll11l_opy_
  }
  return bstack1l1l1l1l11_opy_
@error_handler(class_method=False)
def bstack1llll11ll1l1_opy_(bs_config):
  try:
    bstack1llll11l1ll1_opy_ = json.loads(os.getenv(bstack1lllll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡡࡄࡇࡈࡋࡓࡔࡋࡅࡍࡑࡏࡔ࡚ࡡࡆࡓࡓࡌࡉࡈࡗࡕࡅ࡙ࡏࡏࡏࡡ࡜ࡑࡑ࠭∬"), bstack1lllll1_opy_ (u"࠭ࡻࡾࠩ∭")))
    bstack1llll11l1ll1_opy_ = bstack1llll11ll111_opy_(bs_config, bstack1llll11l1ll1_opy_)
    return {
        bstack1lllll1_opy_ (u"ࠧࡴࡧࡷࡸ࡮ࡴࡧࡴࠩ∮"): bstack1llll11l1ll1_opy_
    }
  except Exception as error:
    logger.error(bstack1lllll1_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡼ࡮ࡩ࡭ࡧࠣࡧࡷ࡫ࡡࡵ࡫ࡱ࡫ࠥ࡭ࡥࡵࡡࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡡࡶࡩࡹࡺࡩ࡯ࡩࡶࠤ࡫ࡵࡲࠡࡖࡨࡷࡹࡎࡵࡣ࠼ࠣࠤࢀࢃࠢ∯").format(str(error)))
    return {}
def bstack1llll11ll111_opy_(bs_config, bstack1llll11l1ll1_opy_):
  if ((bstack1lllll1_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭∰") in bs_config or not bstack11ll11111_opy_(bs_config)) and bstack1lll1lll1_opy_.bstack1l1lllll1_opy_(bs_config)):
    bstack1llll11l1ll1_opy_[bstack1lllll1_opy_ (u"ࠥ࡭ࡳࡩ࡬ࡶࡦࡨࡉࡳࡩ࡯ࡥࡧࡧࡉࡽࡺࡥ࡯ࡵ࡬ࡳࡳࠨ∱")] = True
  return bstack1llll11l1ll1_opy_
def bstack1llll1l111l1_opy_(array, bstack1llll11l11ll_opy_, bstack1llll11l111l_opy_):
  result = {}
  for o in array:
    key = o[bstack1llll11l11ll_opy_]
    result[key] = o[bstack1llll11l111l_opy_]
  return result
def bstack1llll1l1lll1_opy_(bstack11ll1lll1l_opy_=bstack1lllll1_opy_ (u"ࠫࠬ∲")):
  bstack1llll11l1l11_opy_ = bstack1lll1lll1_opy_.on()
  bstack1llll11l1l1l_opy_ = bstack1llll111_opy_.on()
  bstack1llll11l1lll_opy_ = percy.bstack11lll11lll_opy_()
  if bstack1llll11l1lll_opy_ and not bstack1llll11l1l1l_opy_ and not bstack1llll11l1l11_opy_:
    return bstack11ll1lll1l_opy_ not in [bstack1lllll1_opy_ (u"ࠬࡉࡂࡕࡕࡨࡷࡸ࡯࡯࡯ࡅࡵࡩࡦࡺࡥࡥࠩ∳"), bstack1lllll1_opy_ (u"࠭ࡌࡰࡩࡆࡶࡪࡧࡴࡦࡦࠪ∴")]
  elif bstack1llll11l1l11_opy_ and not bstack1llll11l1l1l_opy_:
    return bstack11ll1lll1l_opy_ not in [bstack1lllll1_opy_ (u"ࠧࡉࡱࡲ࡯ࡗࡻ࡮ࡔࡶࡤࡶࡹ࡫ࡤࠨ∵"), bstack1lllll1_opy_ (u"ࠨࡊࡲࡳࡰࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪ∶"), bstack1lllll1_opy_ (u"ࠩࡏࡳ࡬ࡉࡲࡦࡣࡷࡩࡩ࠭∷")]
  return bstack1llll11l1l11_opy_ or bstack1llll11l1l1l_opy_ or bstack1llll11l1lll_opy_
@error_handler(class_method=False)
def bstack1llll11llll1_opy_(bstack11ll1lll1l_opy_, test=None):
  bstack1llll111llll_opy_ = bstack1lll1lll1_opy_.on()
  if not bstack1llll111llll_opy_ or bstack11ll1lll1l_opy_ not in [bstack1lllll1_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡊ࡮ࡴࡩࡴࡪࡨࡨࠬ∸")] or test == None:
    return None
  return {
    bstack1lllll1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ∹"): bstack1llll111llll_opy_ and bstack1lll1l11_opy_(threading.current_thread(), bstack1lllll1_opy_ (u"ࠬࡧ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫ∺"), None) == True and bstack1lll1lll1_opy_.bstack11l1ll1lll_opy_(test[bstack1lllll1_opy_ (u"࠭ࡴࡢࡩࡶࠫ∻")])
  }
def bstack1llll11l11l1_opy_(bs_config, framework):
  bstack1l11l11ll1_opy_ = False
  bstack11ll1ll11_opy_ = False
  bstack1llll11ll11l_opy_ = False
  if bstack1lllll1_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫ∼") in bs_config:
    bstack1llll11ll11l_opy_ = True
  elif bstack1lllll1_opy_ (u"ࠨࡣࡳࡴࠬ∽") in bs_config:
    bstack1l11l11ll1_opy_ = True
  else:
    bstack11ll1ll11_opy_ = True
  bstack1l1l1l1l11_opy_ = {
    bstack1lllll1_opy_ (u"ࠩࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩ∾"): bstack1llll111_opy_.bstack11l11l1l11l_opy_(bs_config, framework),
    bstack1lllll1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ∿"): bstack1lll1lll1_opy_.bstack111ll111l1_opy_(bs_config),
    bstack1lllll1_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࠪ≀"): bs_config.get(bstack1lllll1_opy_ (u"ࠬࡶࡥࡳࡥࡼࠫ≁"), False),
    bstack1lllll1_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡥࠨ≂"): bstack11ll1ll11_opy_,
    bstack1lllll1_opy_ (u"ࠧࡢࡲࡳࡣࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭≃"): bstack1l11l11ll1_opy_,
    bstack1lllll1_opy_ (u"ࠨࡶࡸࡶࡧࡵࡳࡤࡣ࡯ࡩࠬ≄"): bstack1llll11ll11l_opy_
  }
  return bstack1l1l1l1l11_opy_