# coding: UTF-8
import sys
bstack1lll1l_opy_ = sys.version_info [0] == 2
bstack111l11l_opy_ = 2048
bstack1l1llll_opy_ = 7
def bstack111111l_opy_ (bstack1ll1_opy_):
    global bstack11l1ll_opy_
    bstack11ll1l_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack11ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack1lllll1_opy_ = bstack11ll1l_opy_ % len (bstack11ll_opy_)
    bstack111l1l1_opy_ = bstack11ll_opy_ [:bstack1lllll1_opy_] + bstack11ll_opy_ [bstack1lllll1_opy_:]
    if bstack1lll1l_opy_:
        bstack1111_opy_ = unicode () .join ([unichr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    else:
        bstack1111_opy_ = str () .join ([chr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    return eval (bstack1111_opy_)
import os
import json
import logging
import datetime
import threading
from bstack_utils.helper import bstack111ll1111l1_opy_, bstack111l11lll1_opy_, get_host_info, bstack1111llll11l_opy_, \
 bstack11l1l1l1ll_opy_, bstack1lll111l_opy_, error_handler, bstack111l1111ll1_opy_, bstack1llll1ll_opy_
import bstack_utils.accessibility as bstack1llll111l_opy_
from bstack_utils.bstack1111l1l1_opy_ import bstack1lll1ll11_opy_
from bstack_utils.bstack1l1111l1_opy_ import bstack1ll1l1ll_opy_
from bstack_utils.percy import bstack11lll11l1_opy_
from bstack_utils.config import Config
bstack11111lll_opy_ = Config.bstack111l111l_opy_()
logger = logging.getLogger(__name__)
percy = bstack11lll11l1_opy_()
@error_handler(class_method=False)
def bstack1llll1l1ll1l_opy_(bs_config, bstack11l1lll11_opy_):
  try:
    data = {
        bstack111111l_opy_ (u"ࠧࡧࡱࡵࡱࡦࡺࠧ⇯"): bstack111111l_opy_ (u"ࠨ࡬ࡶࡳࡳ࠭⇰"),
        bstack111111l_opy_ (u"ࠩࡳࡶࡴࡰࡥࡤࡶࡢࡲࡦࡳࡥࠨ⇱"): bs_config.get(bstack111111l_opy_ (u"ࠪࡴࡷࡵࡪࡦࡥࡷࡒࡦࡳࡥࠨ⇲"), bstack111111l_opy_ (u"ࠫࠬ⇳")),
        bstack111111l_opy_ (u"ࠬࡴࡡ࡮ࡧࠪ⇴"): bs_config.get(bstack111111l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩ⇵"), os.path.basename(os.path.abspath(os.getcwd()))),
        bstack111111l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥࡩࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ⇶"): bs_config.get(bstack111111l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ⇷")),
        bstack111111l_opy_ (u"ࠩࡧࡩࡸࡩࡲࡪࡲࡷ࡭ࡴࡴࠧ⇸"): bs_config.get(bstack111111l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡆࡨࡷࡨࡸࡩࡱࡶ࡬ࡳࡳ࠭⇹"), bstack111111l_opy_ (u"ࠫࠬ⇺")),
        bstack111111l_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩ⇻"): bstack1llll1ll_opy_(),
        bstack111111l_opy_ (u"࠭ࡴࡢࡩࡶࠫ⇼"): bstack1111llll11l_opy_(bs_config),
        bstack111111l_opy_ (u"ࠧࡩࡱࡶࡸࡤ࡯࡮ࡧࡱࠪ⇽"): get_host_info(),
        bstack111111l_opy_ (u"ࠨࡥ࡬ࡣ࡮ࡴࡦࡰࠩ⇾"): bstack111l11lll1_opy_(),
        bstack111111l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡴࡸࡲࡤ࡯ࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ⇿"): os.environ.get(bstack111111l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡅ࡙ࡎࡒࡄࡠࡔࡘࡒࡤࡏࡄࡆࡐࡗࡍࡋࡏࡅࡓࠩ∀")),
        bstack111111l_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࡣࡹ࡫ࡳࡵࡵࡢࡶࡪࡸࡵ࡯ࠩ∁"): os.environ.get(bstack111111l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡗࡋࡒࡖࡐࠪ∂"), False),
        bstack111111l_opy_ (u"࠭ࡶࡦࡴࡶ࡭ࡴࡴ࡟ࡤࡱࡱࡸࡷࡵ࡬ࠨ∃"): bstack111ll1111l1_opy_(),
        bstack111111l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ∄"): bstack1llll11ll11l_opy_(bs_config),
        bstack111111l_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡩ࡫ࡴࡢ࡫࡯ࡷࠬ∅"): bstack1llll11l1l1l_opy_(bstack11l1lll11_opy_),
        bstack111111l_opy_ (u"ࠩࡳࡶࡴࡪࡵࡤࡶࡢࡱࡦࡶࠧ∆"): bstack1llll11l1l11_opy_(bs_config, bstack11l1lll11_opy_.get(bstack111111l_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡵࡴࡧࡧࠫ∇"), bstack111111l_opy_ (u"ࠫࠬ∈"))),
        bstack111111l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠧ∉"): bstack11l1l1l1ll_opy_(bs_config),
        bstack111111l_opy_ (u"࠭ࡴࡦࡵࡷࡣࡴࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࠫ∊"): bstack1llll11l1ll1_opy_(bs_config)
    }
    return data
  except Exception as error:
    logger.error(bstack111111l_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡻ࡭࡯࡬ࡦࠢࡦࡶࡪࡧࡴࡪࡰࡪࠤࡵࡧࡹ࡭ࡱࡤࡨࠥ࡬࡯ࡳࠢࡗࡩࡸࡺࡈࡶࡤ࠽ࠤࠥࢁࡽࠣ∋").format(str(error)))
    return None
def bstack1llll11l1l1l_opy_(framework):
  return {
    bstack111111l_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡒࡦࡳࡥࠨ∌"): framework.get(bstack111111l_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࠪ∍"), bstack111111l_opy_ (u"ࠪࡔࡾࡺࡥࡴࡶࠪ∎")),
    bstack111111l_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࡖࡦࡴࡶ࡭ࡴࡴࠧ∏"): framework.get(bstack111111l_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡸࡨࡶࡸ࡯࡯࡯ࠩ∐")),
    bstack111111l_opy_ (u"࠭ࡳࡥ࡭࡙ࡩࡷࡹࡩࡰࡰࠪ∑"): framework.get(bstack111111l_opy_ (u"ࠧࡴࡦ࡮ࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬ−")),
    bstack111111l_opy_ (u"ࠨ࡮ࡤࡲ࡬ࡻࡡࡨࡧࠪ∓"): bstack111111l_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩ∔"),
    bstack111111l_opy_ (u"ࠪࡸࡪࡹࡴࡇࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪ∕"): framework.get(bstack111111l_opy_ (u"ࠫࡹ࡫ࡳࡵࡈࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫ∖"))
  }
def bstack1llll11l1ll1_opy_(bs_config):
  bstack111111l_opy_ (u"ࠧࠨࠢࠋࠢࠣࡖࡪࡺࡵࡳࡰࡶࠤࡹ࡮ࡥࠡࡶࡨࡷࡹࠦ࡯ࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࠦࡤࡢࡶࡤࠤ࡫ࡵࡲࠡࡤࡸ࡭ࡱࡪࠠࡴࡶࡤࡶࡹ࠴ࠊࠡࠢࠥࠦࠧ∗")
  if not bs_config:
    return {}
  bstack111llll1l1l_opy_ = bstack1lll1ll11_opy_(bs_config).bstack11l111l1l1l_opy_(bs_config)
  return bstack111llll1l1l_opy_
def bstack1111111ll_opy_(bs_config, framework):
  bstack1l11lll1ll_opy_ = False
  bstack111111ll1_opy_ = False
  bstack1llll11l11ll_opy_ = False
  if bstack111111l_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪ∘") in bs_config:
    bstack1llll11l11ll_opy_ = True
  elif bstack111111l_opy_ (u"ࠧࡢࡲࡳࠫ∙") in bs_config:
    bstack1l11lll1ll_opy_ = True
  else:
    bstack111111ll1_opy_ = True
  bstack1l1l1l1ll_opy_ = {
    bstack111111l_opy_ (u"ࠨࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨ√"): bstack1ll1l1ll_opy_.bstack11l11l1ll1l_opy_(bs_config, framework),
    bstack111111l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ∛"): bstack1llll111l_opy_.bstack11ll1l11ll_opy_(bs_config),
    bstack111111l_opy_ (u"ࠪࡴࡪࡸࡣࡺࠩ∜"): bs_config.get(bstack111111l_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࠪ∝"), False),
    bstack111111l_opy_ (u"ࠬࡧࡵࡵࡱࡰࡥࡹ࡫ࠧ∞"): bstack111111ll1_opy_,
    bstack111111l_opy_ (u"࠭ࡡࡱࡲࡢࡥࡺࡺ࡯࡮ࡣࡷࡩࠬ∟"): bstack1l11lll1ll_opy_,
    bstack111111l_opy_ (u"ࠧࡵࡷࡵࡦࡴࡹࡣࡢ࡮ࡨࠫ∠"): bstack1llll11l11ll_opy_
  }
  return bstack1l1l1l1ll_opy_
@error_handler(class_method=False)
def bstack1llll11ll11l_opy_(bs_config):
  try:
    bstack1llll111ll1l_opy_ = json.loads(os.getenv(bstack111111l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡤࡇࡃࡄࡇࡖࡗࡎࡈࡉࡍࡋࡗ࡝ࡤࡉࡏࡏࡈࡌࡋ࡚ࡘࡁࡕࡋࡒࡒࡤ࡟ࡍࡍࠩ∡"), bstack111111l_opy_ (u"ࠩࡾࢁࠬ∢")))
    bstack1llll111ll1l_opy_ = bstack1llll11l1111_opy_(bs_config, bstack1llll111ll1l_opy_)
    return {
        bstack111111l_opy_ (u"ࠪࡷࡪࡺࡴࡪࡰࡪࡷࠬ∣"): bstack1llll111ll1l_opy_
    }
  except Exception as error:
    logger.error(bstack111111l_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡸࡪ࡬ࡰࡪࠦࡣࡳࡧࡤࡸ࡮ࡴࡧࠡࡩࡨࡸࡤࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡤࡹࡥࡵࡶ࡬ࡲ࡬ࡹࠠࡧࡱࡵࠤ࡙࡫ࡳࡵࡊࡸࡦ࠿ࠦࠠࡼࡿࠥ∤").format(str(error)))
    return {}
def bstack1llll11l1111_opy_(bs_config, bstack1llll111ll1l_opy_):
  if ((bstack111111l_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩ∥") in bs_config or not bstack11l1l1l1ll_opy_(bs_config)) and bstack1llll111l_opy_.bstack11ll1l11ll_opy_(bs_config)):
    bstack1llll111ll1l_opy_[bstack111111l_opy_ (u"ࠨࡩ࡯ࡥ࡯ࡹࡩ࡫ࡅ࡯ࡥࡲࡨࡪࡪࡅࡹࡶࡨࡲࡸ࡯࡯࡯ࠤ∦")] = True
  return bstack1llll111ll1l_opy_
def bstack1llll1l11l11_opy_(array, bstack1llll111lll1_opy_, bstack1llll11l11l1_opy_):
  result = {}
  for o in array:
    key = o[bstack1llll111lll1_opy_]
    result[key] = o[bstack1llll11l11l1_opy_]
  return result
def bstack1llll1l1111l_opy_(bstack1111ll1l1_opy_=bstack111111l_opy_ (u"ࠧࠨ∧")):
  bstack1llll11l111l_opy_ = bstack1llll111l_opy_.on()
  bstack1llll111llll_opy_ = bstack1ll1l1ll_opy_.on()
  bstack1llll11ll111_opy_ = percy.bstack1111l1111_opy_()
  if bstack1llll11ll111_opy_ and not bstack1llll111llll_opy_ and not bstack1llll11l111l_opy_:
    return bstack1111ll1l1_opy_ not in [bstack111111l_opy_ (u"ࠨࡅࡅࡘࡘ࡫ࡳࡴ࡫ࡲࡲࡈࡸࡥࡢࡶࡨࡨࠬ∨"), bstack111111l_opy_ (u"ࠩࡏࡳ࡬ࡉࡲࡦࡣࡷࡩࡩ࠭∩")]
  elif bstack1llll11l111l_opy_ and not bstack1llll111llll_opy_:
    return bstack1111ll1l1_opy_ not in [bstack111111l_opy_ (u"ࠪࡌࡴࡵ࡫ࡓࡷࡱࡗࡹࡧࡲࡵࡧࡧࠫ∪"), bstack111111l_opy_ (u"ࠫࡍࡵ࡯࡬ࡔࡸࡲࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭∫"), bstack111111l_opy_ (u"ࠬࡒ࡯ࡨࡅࡵࡩࡦࡺࡥࡥࠩ∬")]
  return bstack1llll11l111l_opy_ or bstack1llll111llll_opy_ or bstack1llll11ll111_opy_
@error_handler(class_method=False)
def bstack1llll1l1l1l1_opy_(bstack1111ll1l1_opy_, test=None):
  bstack1llll11l1lll_opy_ = bstack1llll111l_opy_.on()
  if not bstack1llll11l1lll_opy_ or bstack1111ll1l1_opy_ not in [bstack111111l_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡆࡪࡰ࡬ࡷ࡭࡫ࡤࠨ∭")] or test == None:
    return None
  return {
    bstack111111l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ∮"): bstack1llll11l1lll_opy_ and bstack1lll111l_opy_(threading.current_thread(), bstack111111l_opy_ (u"ࠨࡣ࠴࠵ࡾࡖ࡬ࡢࡶࡩࡳࡷࡳࠧ∯"), None) == True and bstack1llll111l_opy_.bstack11l11ll11l_opy_(test[bstack111111l_opy_ (u"ࠩࡷࡥ࡬ࡹࠧ∰")])
  }
def bstack1llll11l1l11_opy_(bs_config, framework):
  bstack1l11lll1ll_opy_ = False
  bstack111111ll1_opy_ = False
  bstack1llll11l11ll_opy_ = False
  if bstack111111l_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧ∱") in bs_config:
    bstack1llll11l11ll_opy_ = True
  elif bstack111111l_opy_ (u"ࠫࡦࡶࡰࠨ∲") in bs_config:
    bstack1l11lll1ll_opy_ = True
  else:
    bstack111111ll1_opy_ = True
  bstack1l1l1l1ll_opy_ = {
    bstack111111l_opy_ (u"ࠬࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬ∳"): bstack1ll1l1ll_opy_.bstack11l11l1ll1l_opy_(bs_config, framework),
    bstack111111l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭∴"): bstack1llll111l_opy_.bstack11llll1l11_opy_(bs_config),
    bstack111111l_opy_ (u"ࠧࡱࡧࡵࡧࡾ࠭∵"): bs_config.get(bstack111111l_opy_ (u"ࠨࡲࡨࡶࡨࡿࠧ∶"), False),
    bstack111111l_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶࡨࠫ∷"): bstack111111ll1_opy_,
    bstack111111l_opy_ (u"ࠪࡥࡵࡶ࡟ࡢࡷࡷࡳࡲࡧࡴࡦࠩ∸"): bstack1l11lll1ll_opy_,
    bstack111111l_opy_ (u"ࠫࡹࡻࡲࡣࡱࡶࡧࡦࡲࡥࠨ∹"): bstack1llll11l11ll_opy_
  }
  return bstack1l1l1l1ll_opy_