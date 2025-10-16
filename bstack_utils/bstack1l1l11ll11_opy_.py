# coding: UTF-8
import sys
bstack11l1_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1llllll1_opy_ = 7
def bstack1l_opy_ (bstack11l1lll_opy_):
    global bstack1ll1ll1_opy_
    bstack1ll1l_opy_ = ord (bstack11l1lll_opy_ [-1])
    bstack1lll11_opy_ = bstack11l1lll_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1l_opy_ % len (bstack1lll11_opy_)
    bstack1ll11l_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l1_opy_:
        bstack1l1ll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    else:
        bstack1l1ll1l_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    return eval (bstack1l1ll1l_opy_)
import os
import json
import logging
import datetime
import threading
from bstack_utils.helper import bstack111l1l1111l_opy_, bstack11ll1111l_opy_, get_host_info, bstack1111ll1ll11_opy_, \
 bstack1l1l11llll_opy_, bstack1llll11l_opy_, error_handler, bstack1111ll111ll_opy_, bstack1ll11l1l_opy_
import bstack_utils.accessibility as bstack11111ll1_opy_
from bstack_utils.bstack1111l11l_opy_ import bstack11111l1l_opy_
from bstack_utils.bstack1ll111l1_opy_ import bstack11lll1l1_opy_
from bstack_utils.percy import bstack1l1lll11ll_opy_
from bstack_utils.config import Config
bstack1lll1ll1l_opy_ = Config.bstack1llll11ll_opy_()
logger = logging.getLogger(__name__)
percy = bstack1l1lll11ll_opy_()
@error_handler(class_method=False)
def bstack1llll1l11l1l_opy_(bs_config, bstack11ll1l1ll1_opy_):
  try:
    data = {
        bstack1l_opy_ (u"࠭ࡦࡰࡴࡰࡥࡹ࠭⇼"): bstack1l_opy_ (u"ࠧ࡫ࡵࡲࡲࠬ⇽"),
        bstack1l_opy_ (u"ࠨࡲࡵࡳ࡯࡫ࡣࡵࡡࡱࡥࡲ࡫ࠧ⇾"): bs_config.get(bstack1l_opy_ (u"ࠩࡳࡶࡴࡰࡥࡤࡶࡑࡥࡲ࡫ࠧ⇿"), bstack1l_opy_ (u"ࠪࠫ∀")),
        bstack1l_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ∁"): bs_config.get(bstack1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ∂"), os.path.basename(os.path.abspath(os.getcwd()))),
        bstack1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡯ࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ∃"): bs_config.get(bstack1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ∄")),
        bstack1l_opy_ (u"ࠨࡦࡨࡷࡨࡸࡩࡱࡶ࡬ࡳࡳ࠭∅"): bs_config.get(bstack1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡅࡧࡶࡧࡷ࡯ࡰࡵ࡫ࡲࡲࠬ∆"), bstack1l_opy_ (u"ࠪࠫ∇")),
        bstack1l_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨ∈"): bstack1ll11l1l_opy_(),
        bstack1l_opy_ (u"ࠬࡺࡡࡨࡵࠪ∉"): bstack1111ll1ll11_opy_(bs_config),
        bstack1l_opy_ (u"࠭ࡨࡰࡵࡷࡣ࡮ࡴࡦࡰࠩ∊"): get_host_info(),
        bstack1l_opy_ (u"ࠧࡤ࡫ࡢ࡭ࡳ࡬࡯ࠨ∋"): bstack11ll1111l_opy_(),
        bstack1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡳࡷࡱࡣ࡮ࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ∌"): os.environ.get(bstack1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡄࡘࡍࡑࡊ࡟ࡓࡗࡑࡣࡎࡊࡅࡏࡖࡌࡊࡎࡋࡒࠨ∍")),
        bstack1l_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࡢࡸࡪࡹࡴࡴࡡࡵࡩࡷࡻ࡮ࠨ∎"): os.environ.get(bstack1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡖࡊࡘࡕࡏࠩ∏"), False),
        bstack1l_opy_ (u"ࠬࡼࡥࡳࡵ࡬ࡳࡳࡥࡣࡰࡰࡷࡶࡴࡲࠧ∐"): bstack111l1l1111l_opy_(),
        bstack1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭∑"): bstack1llll11l11ll_opy_(bs_config),
        bstack1l_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡨࡪࡺࡡࡪ࡮ࡶࠫ−"): bstack1llll111lll1_opy_(bstack11ll1l1ll1_opy_),
        bstack1l_opy_ (u"ࠨࡲࡵࡳࡩࡻࡣࡵࡡࡰࡥࡵ࠭∓"): bstack1llll111llll_opy_(bs_config, bstack11ll1l1ll1_opy_.get(bstack1l_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡻࡳࡦࡦࠪ∔"), bstack1l_opy_ (u"ࠪࠫ∕"))),
        bstack1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭∖"): bstack1l1l11llll_opy_(bs_config),
        bstack1l_opy_ (u"ࠬࡺࡥࡴࡶࡢࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࠪ∗"): bstack1llll11ll1l1_opy_(bs_config)
    }
    return data
  except Exception as error:
    logger.error(bstack1l_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡺ࡬࡮ࡲࡥࠡࡥࡵࡩࡦࡺࡩ࡯ࡩࠣࡴࡦࡿ࡬ࡰࡣࡧࠤ࡫ࡵࡲࠡࡖࡨࡷࡹࡎࡵࡣ࠼ࠣࠤࢀࢃࠢ∘").format(str(error)))
    return None
def bstack1llll111lll1_opy_(framework):
  return {
    bstack1l_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡑࡥࡲ࡫ࠧ∙"): framework.get(bstack1l_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦࠩ√"), bstack1l_opy_ (u"ࠩࡓࡽࡹ࡫ࡳࡵࠩ∛")),
    bstack1l_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࡜ࡥࡳࡵ࡬ࡳࡳ࠭∜"): framework.get(bstack1l_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨ∝")),
    bstack1l_opy_ (u"ࠬࡹࡤ࡬ࡘࡨࡶࡸ࡯࡯࡯ࠩ∞"): framework.get(bstack1l_opy_ (u"࠭ࡳࡥ࡭ࡢࡺࡪࡸࡳࡪࡱࡱࠫ∟")),
    bstack1l_opy_ (u"ࠧ࡭ࡣࡱ࡫ࡺࡧࡧࡦࠩ∠"): bstack1l_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨ∡"),
    bstack1l_opy_ (u"ࠩࡷࡩࡸࡺࡆࡳࡣࡰࡩࡼࡵࡲ࡬ࠩ∢"): framework.get(bstack1l_opy_ (u"ࠪࡸࡪࡹࡴࡇࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪ∣"))
  }
def bstack1llll11ll1l1_opy_(bs_config):
  bstack1l_opy_ (u"ࠦࠧࠨࠊࠡࠢࡕࡩࡹࡻࡲ࡯ࡵࠣࡸ࡭࡫ࠠࡵࡧࡶࡸࠥࡵࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࠥࡪࡡࡵࡣࠣࡪࡴࡸࠠࡣࡷ࡬ࡰࡩࠦࡳࡵࡣࡵࡸ࠳ࠐࠠࠡࠤࠥࠦ∤")
  if not bs_config:
    return {}
  bstack11l111l1l11_opy_ = bstack11111l1l_opy_(bs_config).bstack111lll1llll_opy_(bs_config)
  return bstack11l111l1l11_opy_
def bstack11l1llll11_opy_(bs_config, framework):
  bstack11lll1l1l_opy_ = False
  bstack1111l1111l_opy_ = False
  bstack1llll11l1l11_opy_ = False
  if bstack1l_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩ∥") in bs_config:
    bstack1llll11l1l11_opy_ = True
  elif bstack1l_opy_ (u"࠭ࡡࡱࡲࠪ∦") in bs_config:
    bstack11lll1l1l_opy_ = True
  else:
    bstack1111l1111l_opy_ = True
  bstack1111llll11_opy_ = {
    bstack1l_opy_ (u"ࠧࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠧ∧"): bstack11lll1l1_opy_.bstack11l11l1ll1l_opy_(bs_config, framework),
    bstack1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ∨"): bstack11111ll1_opy_.bstack11111111l_opy_(bs_config),
    bstack1l_opy_ (u"ࠩࡳࡩࡷࡩࡹࠨ∩"): bs_config.get(bstack1l_opy_ (u"ࠪࡴࡪࡸࡣࡺࠩ∪"), False),
    bstack1l_opy_ (u"ࠫࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭∫"): bstack1111l1111l_opy_,
    bstack1l_opy_ (u"ࠬࡧࡰࡱࡡࡤࡹࡹࡵ࡭ࡢࡶࡨࠫ∬"): bstack11lll1l1l_opy_,
    bstack1l_opy_ (u"࠭ࡴࡶࡴࡥࡳࡸࡩࡡ࡭ࡧࠪ∭"): bstack1llll11l1l11_opy_
  }
  return bstack1111llll11_opy_
@error_handler(class_method=False)
def bstack1llll11l11ll_opy_(bs_config):
  try:
    bstack1llll11l1lll_opy_ = json.loads(os.getenv(bstack1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡣࡆࡉࡃࡆࡕࡖࡍࡇࡏࡌࡊࡖ࡜ࡣࡈࡕࡎࡇࡋࡊ࡙ࡗࡇࡔࡊࡑࡑࡣ࡞ࡓࡌࠨ∮"), bstack1l_opy_ (u"ࠨࡽࢀࠫ∯")))
    bstack1llll11l1lll_opy_ = bstack1llll11ll11l_opy_(bs_config, bstack1llll11l1lll_opy_)
    return {
        bstack1l_opy_ (u"ࠩࡶࡩࡹࡺࡩ࡯ࡩࡶࠫ∰"): bstack1llll11l1lll_opy_
    }
  except Exception as error:
    logger.error(bstack1l_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡷࡩ࡫࡯ࡩࠥࡩࡲࡦࡣࡷ࡭ࡳ࡭ࠠࡨࡧࡷࡣࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡣࡸ࡫ࡴࡵ࡫ࡱ࡫ࡸࠦࡦࡰࡴࠣࡘࡪࡹࡴࡉࡷࡥ࠾ࠥࠦࡻࡾࠤ∱").format(str(error)))
    return {}
def bstack1llll11ll11l_opy_(bs_config, bstack1llll11l1lll_opy_):
  if ((bstack1l_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨ∲") in bs_config or not bstack1l1l11llll_opy_(bs_config)) and bstack11111ll1_opy_.bstack11111111l_opy_(bs_config)):
    bstack1llll11l1lll_opy_[bstack1l_opy_ (u"ࠧ࡯࡮ࡤ࡮ࡸࡨࡪࡋ࡮ࡤࡱࡧࡩࡩࡋࡸࡵࡧࡱࡷ࡮ࡵ࡮ࠣ∳")] = True
  return bstack1llll11l1lll_opy_
def bstack1llll11lll1l_opy_(array, bstack1llll11l1111_opy_, bstack1llll11ll111_opy_):
  result = {}
  for o in array:
    key = o[bstack1llll11l1111_opy_]
    result[key] = o[bstack1llll11ll111_opy_]
  return result
def bstack1llll11ll1ll_opy_(bstack1l1llllll1_opy_=bstack1l_opy_ (u"࠭ࠧ∴")):
  bstack1llll11l11l1_opy_ = bstack11111ll1_opy_.on()
  bstack1llll11l111l_opy_ = bstack11lll1l1_opy_.on()
  bstack1llll11l1ll1_opy_ = percy.bstack111l11ll1l_opy_()
  if bstack1llll11l1ll1_opy_ and not bstack1llll11l111l_opy_ and not bstack1llll11l11l1_opy_:
    return bstack1l1llllll1_opy_ not in [bstack1l_opy_ (u"ࠧࡄࡄࡗࡗࡪࡹࡳࡪࡱࡱࡇࡷ࡫ࡡࡵࡧࡧࠫ∵"), bstack1l_opy_ (u"ࠨࡎࡲ࡫ࡈࡸࡥࡢࡶࡨࡨࠬ∶")]
  elif bstack1llll11l11l1_opy_ and not bstack1llll11l111l_opy_:
    return bstack1l1llllll1_opy_ not in [bstack1l_opy_ (u"ࠩࡋࡳࡴࡱࡒࡶࡰࡖࡸࡦࡸࡴࡦࡦࠪ∷"), bstack1l_opy_ (u"ࠪࡌࡴࡵ࡫ࡓࡷࡱࡊ࡮ࡴࡩࡴࡪࡨࡨࠬ∸"), bstack1l_opy_ (u"ࠫࡑࡵࡧࡄࡴࡨࡥࡹ࡫ࡤࠨ∹")]
  return bstack1llll11l11l1_opy_ or bstack1llll11l111l_opy_ or bstack1llll11l1ll1_opy_
@error_handler(class_method=False)
def bstack1llll1l1l111_opy_(bstack1l1llllll1_opy_, test=None):
  bstack1llll11l1l1l_opy_ = bstack11111ll1_opy_.on()
  if not bstack1llll11l1l1l_opy_ or bstack1l1llllll1_opy_ not in [bstack1l_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳࡌࡩ࡯࡫ࡶ࡬ࡪࡪࠧ∺")] or test == None:
    return None
  return {
    bstack1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭∻"): bstack1llll11l1l1l_opy_ and bstack1llll11l_opy_(threading.current_thread(), bstack1l_opy_ (u"ࠧࡢ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭∼"), None) == True and bstack11111ll1_opy_.bstack111l11l11_opy_(test[bstack1l_opy_ (u"ࠨࡶࡤ࡫ࡸ࠭∽")])
  }
def bstack1llll111llll_opy_(bs_config, framework):
  bstack11lll1l1l_opy_ = False
  bstack1111l1111l_opy_ = False
  bstack1llll11l1l11_opy_ = False
  if bstack1l_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭∾") in bs_config:
    bstack1llll11l1l11_opy_ = True
  elif bstack1l_opy_ (u"ࠪࡥࡵࡶࠧ∿") in bs_config:
    bstack11lll1l1l_opy_ = True
  else:
    bstack1111l1111l_opy_ = True
  bstack1111llll11_opy_ = {
    bstack1l_opy_ (u"ࠫࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠫ≀"): bstack11lll1l1_opy_.bstack11l11l1ll1l_opy_(bs_config, framework),
    bstack1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ≁"): bstack11111ll1_opy_.bstack1llll1ll1l_opy_(bs_config),
    bstack1l_opy_ (u"࠭ࡰࡦࡴࡦࡽࠬ≂"): bs_config.get(bstack1l_opy_ (u"ࠧࡱࡧࡵࡧࡾ࠭≃"), False),
    bstack1l_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵࡧࠪ≄"): bstack1111l1111l_opy_,
    bstack1l_opy_ (u"ࠩࡤࡴࡵࡥࡡࡶࡶࡲࡱࡦࡺࡥࠨ≅"): bstack11lll1l1l_opy_,
    bstack1l_opy_ (u"ࠪࡸࡺࡸࡢࡰࡵࡦࡥࡱ࡫ࠧ≆"): bstack1llll11l1l11_opy_
  }
  return bstack1111llll11_opy_