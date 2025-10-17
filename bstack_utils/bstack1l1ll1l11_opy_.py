# coding: UTF-8
import sys
bstack1111l11_opy_ = sys.version_info [0] == 2
bstack11111l_opy_ = 2048
bstack1111111_opy_ = 7
def bstack11l111_opy_ (bstack1ll1l1_opy_):
    global bstack1llll1_opy_
    bstack1l1l1_opy_ = ord (bstack1ll1l1_opy_ [-1])
    bstack1lll1_opy_ = bstack1ll1l1_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1lll1_opy_)
    bstack1l1l111_opy_ = bstack1lll1_opy_ [:bstack1l1l11_opy_] + bstack1lll1_opy_ [bstack1l1l11_opy_:]
    if bstack1111l11_opy_:
        bstack1111lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11111l_opy_ - (bstack1llllll_opy_ + bstack1l1l1_opy_) % bstack1111111_opy_) for bstack1llllll_opy_, char in enumerate (bstack1l1l111_opy_)])
    else:
        bstack1111lll_opy_ = str () .join ([chr (ord (char) - bstack11111l_opy_ - (bstack1llllll_opy_ + bstack1l1l1_opy_) % bstack1111111_opy_) for bstack1llllll_opy_, char in enumerate (bstack1l1l111_opy_)])
    return eval (bstack1111lll_opy_)
import os
import json
import logging
import datetime
import threading
from bstack_utils.helper import bstack111l1ll1l1l_opy_, bstack1l11l111l_opy_, get_host_info, bstack111l1l1lll1_opy_, \
 bstack1ll1l1l1ll_opy_, bstack1l11lll1_opy_, error_handler, bstack1111l1l11l1_opy_, bstack1llll111_opy_
import bstack_utils.accessibility as bstack11l111l1_opy_
from bstack_utils.bstack1lll1l1l1_opy_ import bstack1llllllll_opy_
from bstack_utils.bstack1l111111_opy_ import bstack1l1l11l1_opy_
from bstack_utils.percy import bstack1ll1l1ll1l_opy_
from bstack_utils.config import Config
bstack111ll111_opy_ = Config.bstack111ll1ll_opy_()
logger = logging.getLogger(__name__)
percy = bstack1ll1l1ll1l_opy_()
@error_handler(class_method=False)
def bstack1llll11lllll_opy_(bs_config, bstack1l11ll1ll_opy_):
  try:
    data = {
        bstack11l111_opy_ (u"ࠩࡩࡳࡷࡳࡡࡵࠩ⇪"): bstack11l111_opy_ (u"ࠪ࡮ࡸࡵ࡮ࠨ⇫"),
        bstack11l111_opy_ (u"ࠫࡵࡸ࡯࡫ࡧࡦࡸࡤࡴࡡ࡮ࡧࠪ⇬"): bs_config.get(bstack11l111_opy_ (u"ࠬࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࠪ⇭"), bstack11l111_opy_ (u"࠭ࠧ⇮")),
        bstack11l111_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ⇯"): bs_config.get(bstack11l111_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫ⇰"), os.path.basename(os.path.abspath(os.getcwd()))),
        bstack11l111_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠ࡫ࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ⇱"): bs_config.get(bstack11l111_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ⇲")),
        bstack11l111_opy_ (u"ࠫࡩ࡫ࡳࡤࡴ࡬ࡴࡹ࡯࡯࡯ࠩ⇳"): bs_config.get(bstack11l111_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡈࡪࡹࡣࡳ࡫ࡳࡸ࡮ࡵ࡮ࠨ⇴"), bstack11l111_opy_ (u"࠭ࠧ⇵")),
        bstack11l111_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫ⇶"): bstack1llll111_opy_(),
        bstack11l111_opy_ (u"ࠨࡶࡤ࡫ࡸ࠭⇷"): bstack111l1l1lll1_opy_(bs_config),
        bstack11l111_opy_ (u"ࠩ࡫ࡳࡸࡺ࡟ࡪࡰࡩࡳࠬ⇸"): get_host_info(),
        bstack11l111_opy_ (u"ࠪࡧ࡮ࡥࡩ࡯ࡨࡲࠫ⇹"): bstack1l11l111l_opy_(),
        bstack11l111_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢࡶࡺࡴ࡟ࡪࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ⇺"): os.environ.get(bstack11l111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡇ࡛ࡉࡍࡆࡢࡖ࡚ࡔ࡟ࡊࡆࡈࡒ࡙ࡏࡆࡊࡇࡕࠫ⇻")),
        bstack11l111_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩࡥࡴࡦࡵࡷࡷࡤࡸࡥࡳࡷࡱࠫ⇼"): os.environ.get(bstack11l111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡒࡆࡔࡘࡒࠬ⇽"), False),
        bstack11l111_opy_ (u"ࠨࡸࡨࡶࡸ࡯࡯࡯ࡡࡦࡳࡳࡺࡲࡰ࡮ࠪ⇾"): bstack111l1ll1l1l_opy_(),
        bstack11l111_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ⇿"): bstack1llll111l1ll_opy_(bs_config),
        bstack11l111_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡤࡦࡶࡤ࡭ࡱࡹࠧ∀"): bstack1llll111llll_opy_(bstack1l11ll1ll_opy_),
        bstack11l111_opy_ (u"ࠫࡵࡸ࡯ࡥࡷࡦࡸࡤࡳࡡࡱࠩ∁"): bstack1llll111ll11_opy_(bs_config, bstack1l11ll1ll_opy_.get(bstack11l111_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡷࡶࡩࡩ࠭∂"), bstack11l111_opy_ (u"࠭ࠧ∃"))),
        bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠩ∄"): bstack1ll1l1l1ll_opy_(bs_config),
        bstack11l111_opy_ (u"ࠨࡶࡨࡷࡹࡥ࡯ࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳ࠭∅"): bstack1llll111l1l1_opy_(bs_config)
    }
    return data
  except Exception as error:
    logger.error(bstack11l111_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡽࡨࡪ࡮ࡨࠤࡨࡸࡥࡢࡶ࡬ࡲ࡬ࠦࡰࡢࡻ࡯ࡳࡦࡪࠠࡧࡱࡵࠤ࡙࡫ࡳࡵࡊࡸࡦ࠿ࠦࠠࡼࡿࠥ∆").format(str(error)))
    return None
def bstack1llll111llll_opy_(framework):
  return {
    bstack11l111_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡔࡡ࡮ࡧࠪ∇"): framework.get(bstack11l111_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࠬ∈"), bstack11l111_opy_ (u"ࠬࡖࡹࡵࡧࡶࡸࠬ∉")),
    bstack11l111_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡘࡨࡶࡸ࡯࡯࡯ࠩ∊"): framework.get(bstack11l111_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡺࡪࡸࡳࡪࡱࡱࠫ∋")),
    bstack11l111_opy_ (u"ࠨࡵࡧ࡯࡛࡫ࡲࡴ࡫ࡲࡲࠬ∌"): framework.get(bstack11l111_opy_ (u"ࠩࡶࡨࡰࡥࡶࡦࡴࡶ࡭ࡴࡴࠧ∍")),
    bstack11l111_opy_ (u"ࠪࡰࡦࡴࡧࡶࡣࡪࡩࠬ∎"): bstack11l111_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫ∏"),
    bstack11l111_opy_ (u"ࠬࡺࡥࡴࡶࡉࡶࡦࡳࡥࡸࡱࡵ࡯ࠬ∐"): framework.get(bstack11l111_opy_ (u"࠭ࡴࡦࡵࡷࡊࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭∑"))
  }
def bstack1llll111l1l1_opy_(bs_config):
  bstack11l111_opy_ (u"ࠢࠣࠤࠍࠤࠥࡘࡥࡵࡷࡵࡲࡸࠦࡴࡩࡧࠣࡸࡪࡹࡴࠡࡱࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࠡࡦࡤࡸࡦࠦࡦࡰࡴࠣࡦࡺ࡯࡬ࡥࠢࡶࡸࡦࡸࡴ࠯ࠌࠣࠤࠧࠨࠢ−")
  if not bs_config:
    return {}
  bstack111llll1111_opy_ = bstack1llllllll_opy_(bs_config).bstack11l1111lll1_opy_(bs_config)
  return bstack111llll1111_opy_
def bstack1ll11lll1_opy_(bs_config, framework):
  bstack111ll1ll11_opy_ = False
  bstack1ll111lll_opy_ = False
  bstack1llll11l1ll1_opy_ = False
  if bstack11l111_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬ∓") in bs_config:
    bstack1llll11l1ll1_opy_ = True
  elif bstack11l111_opy_ (u"ࠩࡤࡴࡵ࠭∔") in bs_config:
    bstack111ll1ll11_opy_ = True
  else:
    bstack1ll111lll_opy_ = True
  bstack11l1ll1l1_opy_ = {
    bstack11l111_opy_ (u"ࠪࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪ∕"): bstack1l1l11l1_opy_.bstack11l11l1l1l1_opy_(bs_config, framework),
    bstack11l111_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ∖"): bstack11l111l1_opy_.bstack1l1111llll_opy_(bs_config),
    bstack11l111_opy_ (u"ࠬࡶࡥࡳࡥࡼࠫ∗"): bs_config.get(bstack11l111_opy_ (u"࠭ࡰࡦࡴࡦࡽࠬ∘"), False),
    bstack11l111_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡦࠩ∙"): bstack1ll111lll_opy_,
    bstack11l111_opy_ (u"ࠨࡣࡳࡴࡤࡧࡵࡵࡱࡰࡥࡹ࡫ࠧ√"): bstack111ll1ll11_opy_,
    bstack11l111_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡴࡥࡤࡰࡪ࠭∛"): bstack1llll11l1ll1_opy_
  }
  return bstack11l1ll1l1_opy_
@error_handler(class_method=False)
def bstack1llll111l1ll_opy_(bs_config):
  try:
    bstack1llll111ll1l_opy_ = json.loads(os.getenv(bstack11l111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚࡟ࡂࡅࡆࡉࡘ࡙ࡉࡃࡋࡏࡍ࡙࡟࡟ࡄࡑࡑࡊࡎࡍࡕࡓࡃࡗࡍࡔࡔ࡟࡚ࡏࡏࠫ∜"), bstack11l111_opy_ (u"ࠫࢀࢃࠧ∝")))
    bstack1llll111ll1l_opy_ = bstack1llll11l11l1_opy_(bs_config, bstack1llll111ll1l_opy_)
    return {
        bstack11l111_opy_ (u"ࠬࡹࡥࡵࡶ࡬ࡲ࡬ࡹࠧ∞"): bstack1llll111ll1l_opy_
    }
  except Exception as error:
    logger.error(bstack11l111_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡺ࡬࡮ࡲࡥࠡࡥࡵࡩࡦࡺࡩ࡯ࡩࠣ࡫ࡪࡺ࡟ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿ࡟ࡴࡧࡷࡸ࡮ࡴࡧࡴࠢࡩࡳࡷࠦࡔࡦࡵࡷࡌࡺࡨ࠺ࠡࠢࡾࢁࠧ∟").format(str(error)))
    return {}
def bstack1llll11l11l1_opy_(bs_config, bstack1llll111ll1l_opy_):
  if ((bstack11l111_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫ∠") in bs_config or not bstack1ll1l1l1ll_opy_(bs_config)) and bstack11l111l1_opy_.bstack1l1111llll_opy_(bs_config)):
    bstack1llll111ll1l_opy_[bstack11l111_opy_ (u"ࠣ࡫ࡱࡧࡱࡻࡤࡦࡇࡱࡧࡴࡪࡥࡥࡇࡻࡸࡪࡴࡳࡪࡱࡱࠦ∡")] = True
  return bstack1llll111ll1l_opy_
def bstack1llll11ll111_opy_(array, bstack1llll11l1l1l_opy_, bstack1llll11l111l_opy_):
  result = {}
  for o in array:
    key = o[bstack1llll11l1l1l_opy_]
    result[key] = o[bstack1llll11l111l_opy_]
  return result
def bstack1llll11l1lll_opy_(bstack1ll1ll1lll_opy_=bstack11l111_opy_ (u"ࠩࠪ∢")):
  bstack1llll11l1l11_opy_ = bstack11l111l1_opy_.on()
  bstack1llll11l1111_opy_ = bstack1l1l11l1_opy_.on()
  bstack1llll111lll1_opy_ = percy.bstack1111l11lll_opy_()
  if bstack1llll111lll1_opy_ and not bstack1llll11l1111_opy_ and not bstack1llll11l1l11_opy_:
    return bstack1ll1ll1lll_opy_ not in [bstack11l111_opy_ (u"ࠪࡇࡇ࡚ࡓࡦࡵࡶ࡭ࡴࡴࡃࡳࡧࡤࡸࡪࡪࠧ∣"), bstack11l111_opy_ (u"ࠫࡑࡵࡧࡄࡴࡨࡥࡹ࡫ࡤࠨ∤")]
  elif bstack1llll11l1l11_opy_ and not bstack1llll11l1111_opy_:
    return bstack1ll1ll1lll_opy_ not in [bstack11l111_opy_ (u"ࠬࡎ࡯ࡰ࡭ࡕࡹࡳ࡙ࡴࡢࡴࡷࡩࡩ࠭∥"), bstack11l111_opy_ (u"࠭ࡈࡰࡱ࡮ࡖࡺࡴࡆࡪࡰ࡬ࡷ࡭࡫ࡤࠨ∦"), bstack11l111_opy_ (u"ࠧࡍࡱࡪࡇࡷ࡫ࡡࡵࡧࡧࠫ∧")]
  return bstack1llll11l1l11_opy_ or bstack1llll11l1111_opy_ or bstack1llll111lll1_opy_
@error_handler(class_method=False)
def bstack1llll1l1lll1_opy_(bstack1ll1ll1lll_opy_, test=None):
  bstack1llll11l11ll_opy_ = bstack11l111l1_opy_.on()
  if not bstack1llll11l11ll_opy_ or bstack1ll1ll1lll_opy_ not in [bstack11l111_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪ∨")] or test == None:
    return None
  return {
    bstack11l111_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ∩"): bstack1llll11l11ll_opy_ and bstack1l11lll1_opy_(threading.current_thread(), bstack11l111_opy_ (u"ࠪࡥ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩ∪"), None) == True and bstack11l111l1_opy_.bstack1l11111ll_opy_(test[bstack11l111_opy_ (u"ࠫࡹࡧࡧࡴࠩ∫")])
  }
def bstack1llll111ll11_opy_(bs_config, framework):
  bstack111ll1ll11_opy_ = False
  bstack1ll111lll_opy_ = False
  bstack1llll11l1ll1_opy_ = False
  if bstack11l111_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩ∬") in bs_config:
    bstack1llll11l1ll1_opy_ = True
  elif bstack11l111_opy_ (u"࠭ࡡࡱࡲࠪ∭") in bs_config:
    bstack111ll1ll11_opy_ = True
  else:
    bstack1ll111lll_opy_ = True
  bstack11l1ll1l1_opy_ = {
    bstack11l111_opy_ (u"ࠧࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠧ∮"): bstack1l1l11l1_opy_.bstack11l11l1l1l1_opy_(bs_config, framework),
    bstack11l111_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ∯"): bstack11l111l1_opy_.bstack1lll1l1lll_opy_(bs_config),
    bstack11l111_opy_ (u"ࠩࡳࡩࡷࡩࡹࠨ∰"): bs_config.get(bstack11l111_opy_ (u"ࠪࡴࡪࡸࡣࡺࠩ∱"), False),
    bstack11l111_opy_ (u"ࠫࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭∲"): bstack1ll111lll_opy_,
    bstack11l111_opy_ (u"ࠬࡧࡰࡱࡡࡤࡹࡹࡵ࡭ࡢࡶࡨࠫ∳"): bstack111ll1ll11_opy_,
    bstack11l111_opy_ (u"࠭ࡴࡶࡴࡥࡳࡸࡩࡡ࡭ࡧࠪ∴"): bstack1llll11l1ll1_opy_
  }
  return bstack11l1ll1l1_opy_