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
import logging
import datetime
import threading
from bstack_utils.helper import bstack111l1111ll1_opy_, bstack11ll111lll_opy_, get_host_info, bstack111l1l1ll11_opy_, \
 bstack1111lllll_opy_, bstack1l1111ll_opy_, error_handler, bstack111l1l11lll_opy_, bstack1ll11lll_opy_
import bstack_utils.accessibility as bstack11111111_opy_
from bstack_utils.bstack1llll11ll_opy_ import bstack1lll1ll1l_opy_
from bstack_utils.bstack1l1l1l11_opy_ import bstack1l11llll_opy_
from bstack_utils.percy import bstack111l111ll_opy_
from bstack_utils.config import Config
bstack111l11ll_opy_ = Config.bstack111l11l1_opy_()
logger = logging.getLogger(__name__)
percy = bstack111l111ll_opy_()
@error_handler(class_method=False)
def bstack1llll11lll11_opy_(bs_config, bstack11l11ll111_opy_):
  try:
    data = {
        bstack1l111ll_opy_ (u"ࠬ࡬࡯ࡳ࡯ࡤࡸࠬ∗"): bstack1l111ll_opy_ (u"࠭ࡪࡴࡱࡱࠫ∘"),
        bstack1l111ll_opy_ (u"ࠧࡱࡴࡲ࡮ࡪࡩࡴࡠࡰࡤࡱࡪ࠭∙"): bs_config.get(bstack1l111ll_opy_ (u"ࠨࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪ࠭√"), bstack1l111ll_opy_ (u"ࠩࠪ∛")),
        bstack1l111ll_opy_ (u"ࠪࡲࡦࡳࡥࠨ∜"): bs_config.get(bstack1l111ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧ∝"), os.path.basename(os.path.abspath(os.getcwd()))),
        bstack1l111ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡮ࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ∞"): bs_config.get(bstack1l111ll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ∟")),
        bstack1l111ll_opy_ (u"ࠧࡥࡧࡶࡧࡷ࡯ࡰࡵ࡫ࡲࡲࠬ∠"): bs_config.get(bstack1l111ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡄࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࠫ∡"), bstack1l111ll_opy_ (u"ࠩࠪ∢")),
        bstack1l111ll_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧ∣"): bstack1ll11lll_opy_(),
        bstack1l111ll_opy_ (u"ࠫࡹࡧࡧࡴࠩ∤"): bstack111l1l1ll11_opy_(bs_config),
        bstack1l111ll_opy_ (u"ࠬ࡮࡯ࡴࡶࡢ࡭ࡳ࡬࡯ࠨ∥"): get_host_info(),
        bstack1l111ll_opy_ (u"࠭ࡣࡪࡡ࡬ࡲ࡫ࡵࠧ∦"): bstack11ll111lll_opy_(),
        bstack1l111ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥࡲࡶࡰࡢ࡭ࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ∧"): os.environ.get(bstack1l111ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡃࡗࡌࡐࡉࡥࡒࡖࡐࡢࡍࡉࡋࡎࡕࡋࡉࡍࡊࡘࠧ∨")),
        bstack1l111ll_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࡡࡷࡩࡸࡺࡳࡠࡴࡨࡶࡺࡴࠧ∩"): os.environ.get(bstack1l111ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡕࡉࡗ࡛ࡎࠨ∪"), False),
        bstack1l111ll_opy_ (u"ࠫࡻ࡫ࡲࡴ࡫ࡲࡲࡤࡩ࡯࡯ࡶࡵࡳࡱ࠭∫"): bstack111l1111ll1_opy_(),
        bstack1l111ll_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ∬"): bstack1llll1111lll_opy_(bs_config),
        bstack1l111ll_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡧࡩࡹࡧࡩ࡭ࡵࠪ∭"): bstack1llll111l1l1_opy_(bstack11l11ll111_opy_),
        bstack1l111ll_opy_ (u"ࠧࡱࡴࡲࡨࡺࡩࡴࡠ࡯ࡤࡴࠬ∮"): bstack1llll1111ll1_opy_(bs_config, bstack11l11ll111_opy_.get(bstack1l111ll_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡺࡹࡥࡥࠩ∯"), bstack1l111ll_opy_ (u"ࠩࠪ∰"))),
        bstack1l111ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬ∱"): bstack1111lllll_opy_(bs_config),
        bstack1l111ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡲࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯ࠩ∲"): bstack1llll111111l_opy_(bs_config)
    }
    return data
  except Exception as error:
    logger.error(bstack1l111ll_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡹ࡫࡭ࡱ࡫ࠠࡤࡴࡨࡥࡹ࡯࡮ࡨࠢࡳࡥࡾࡲ࡯ࡢࡦࠣࡪࡴࡸࠠࡕࡧࡶࡸࡍࡻࡢ࠻ࠢࠣࡿࢂࠨ∳").format(str(error)))
    return None
def bstack1llll111l1l1_opy_(framework):
  return {
    bstack1l111ll_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡐࡤࡱࡪ࠭∴"): framework.get(bstack1l111ll_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥࠨ∵"), bstack1l111ll_opy_ (u"ࠨࡒࡼࡸࡪࡹࡴࠨ∶")),
    bstack1l111ll_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯࡛࡫ࡲࡴ࡫ࡲࡲࠬ∷"): framework.get(bstack1l111ll_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡶࡦࡴࡶ࡭ࡴࡴࠧ∸")),
    bstack1l111ll_opy_ (u"ࠫࡸࡪ࡫ࡗࡧࡵࡷ࡮ࡵ࡮ࠨ∹"): framework.get(bstack1l111ll_opy_ (u"ࠬࡹࡤ࡬ࡡࡹࡩࡷࡹࡩࡰࡰࠪ∺")),
    bstack1l111ll_opy_ (u"࠭࡬ࡢࡰࡪࡹࡦ࡭ࡥࠨ∻"): bstack1l111ll_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧ∼"),
    bstack1l111ll_opy_ (u"ࠨࡶࡨࡷࡹࡌࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨ∽"): framework.get(bstack1l111ll_opy_ (u"ࠩࡷࡩࡸࡺࡆࡳࡣࡰࡩࡼࡵࡲ࡬ࠩ∾"))
  }
def bstack1llll111111l_opy_(bs_config):
  bstack1l111ll_opy_ (u"ࠥࠦࠧࠐࠠࠡࡔࡨࡸࡺࡸ࡮ࡴࠢࡷ࡬ࡪࠦࡴࡦࡵࡷࠤࡴࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࠤࡩࡧࡴࡢࠢࡩࡳࡷࠦࡢࡶ࡫࡯ࡨࠥࡹࡴࡢࡴࡷ࠲ࠏࠦࠠࠣࠤࠥ∿")
  if not bs_config:
    return {}
  bstack11l11111lll_opy_ = bstack1lll1ll1l_opy_(bs_config).bstack111ll1ll1ll_opy_(bs_config)
  return bstack11l11111lll_opy_
def bstack11ll1ll1ll_opy_(bs_config, framework):
  bstack1l1ll11l1l_opy_ = False
  bstack11l111l111_opy_ = False
  bstack1llll11111ll_opy_ = False
  if bstack1l111ll_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨ≀") in bs_config:
    bstack1llll11111ll_opy_ = True
  elif bstack1l111ll_opy_ (u"ࠬࡧࡰࡱࠩ≁") in bs_config:
    bstack1l1ll11l1l_opy_ = True
  else:
    bstack11l111l111_opy_ = True
  bstack11lll1l11l_opy_ = {
    bstack1l111ll_opy_ (u"࠭࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭≂"): bstack1l11llll_opy_.bstack11l11l1111l_opy_(bs_config, framework),
    bstack1l111ll_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ≃"): bstack11111111_opy_.bstack11ll1llll_opy_(bs_config),
    bstack1l111ll_opy_ (u"ࠨࡲࡨࡶࡨࡿࠧ≄"): bs_config.get(bstack1l111ll_opy_ (u"ࠩࡳࡩࡷࡩࡹࠨ≅"), False),
    bstack1l111ll_opy_ (u"ࠪࡥࡺࡺ࡯࡮ࡣࡷࡩࠬ≆"): bstack11l111l111_opy_,
    bstack1l111ll_opy_ (u"ࠫࡦࡶࡰࡠࡣࡸࡸࡴࡳࡡࡵࡧࠪ≇"): bstack1l1ll11l1l_opy_,
    bstack1l111ll_opy_ (u"ࠬࡺࡵࡳࡤࡲࡷࡨࡧ࡬ࡦࠩ≈"): bstack1llll11111ll_opy_
  }
  return bstack11lll1l11l_opy_
@error_handler(class_method=False)
def bstack1llll1111lll_opy_(bs_config):
  try:
    bstack1llll111l11l_opy_ = json.loads(os.getenv(bstack1l111ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡢࡅࡈࡉࡅࡔࡕࡌࡆࡎࡒࡉࡕ࡛ࡢࡇࡔࡔࡆࡊࡉࡘࡖࡆ࡚ࡉࡐࡐࡢ࡝ࡒࡒࠧ≉"), bstack1l111ll_opy_ (u"ࠧࡼࡿࠪ≊")))
    bstack1llll111l11l_opy_ = bstack1llll111l1ll_opy_(bs_config, bstack1llll111l11l_opy_)
    return {
        bstack1l111ll_opy_ (u"ࠨࡵࡨࡸࡹ࡯࡮ࡨࡵࠪ≋"): bstack1llll111l11l_opy_
    }
  except Exception as error:
    logger.error(bstack1l111ll_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡽࡨࡪ࡮ࡨࠤࡨࡸࡥࡢࡶ࡬ࡲ࡬ࠦࡧࡦࡶࡢࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡢࡷࡪࡺࡴࡪࡰࡪࡷࠥ࡬࡯ࡳࠢࡗࡩࡸࡺࡈࡶࡤ࠽ࠤࠥࢁࡽࠣ≌").format(str(error)))
    return {}
def bstack1llll111l1ll_opy_(bs_config, bstack1llll111l11l_opy_):
  if ((bstack1l111ll_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧ≍") in bs_config or not bstack1111lllll_opy_(bs_config)) and bstack11111111_opy_.bstack11ll1llll_opy_(bs_config)):
    bstack1llll111l11l_opy_[bstack1l111ll_opy_ (u"ࠦ࡮ࡴࡣ࡭ࡷࡧࡩࡊࡴࡣࡰࡦࡨࡨࡊࡾࡴࡦࡰࡶ࡭ࡴࡴࠢ≎")] = True
  return bstack1llll111l11l_opy_
def bstack1llll11ll111_opy_(array, bstack1llll1111l11_opy_, bstack1llll111ll11_opy_):
  result = {}
  for o in array:
    key = o[bstack1llll1111l11_opy_]
    result[key] = o[bstack1llll111ll11_opy_]
  return result
def bstack1llll11l1lll_opy_(bstack1ll1l111ll_opy_=bstack1l111ll_opy_ (u"ࠬ࠭≏")):
  bstack1llll111ll1l_opy_ = bstack11111111_opy_.on()
  bstack1llll111l111_opy_ = bstack1l11llll_opy_.on()
  bstack1llll1111l1l_opy_ = percy.bstack1ll1l111l_opy_()
  if bstack1llll1111l1l_opy_ and not bstack1llll111l111_opy_ and not bstack1llll111ll1l_opy_:
    return bstack1ll1l111ll_opy_ not in [bstack1l111ll_opy_ (u"࠭ࡃࡃࡖࡖࡩࡸࡹࡩࡰࡰࡆࡶࡪࡧࡴࡦࡦࠪ≐"), bstack1l111ll_opy_ (u"ࠧࡍࡱࡪࡇࡷ࡫ࡡࡵࡧࡧࠫ≑")]
  elif bstack1llll111ll1l_opy_ and not bstack1llll111l111_opy_:
    return bstack1ll1l111ll_opy_ not in [bstack1l111ll_opy_ (u"ࠨࡊࡲࡳࡰࡘࡵ࡯ࡕࡷࡥࡷࡺࡥࡥࠩ≒"), bstack1l111ll_opy_ (u"ࠩࡋࡳࡴࡱࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫ≓"), bstack1l111ll_opy_ (u"ࠪࡐࡴ࡭ࡃࡳࡧࡤࡸࡪࡪࠧ≔")]
  return bstack1llll111ll1l_opy_ or bstack1llll111l111_opy_ or bstack1llll1111l1l_opy_
@error_handler(class_method=False)
def bstack1llll1l11l11_opy_(bstack1ll1l111ll_opy_, test=None):
  bstack1llll11111l1_opy_ = bstack11111111_opy_.on()
  if not bstack1llll11111l1_opy_ or bstack1ll1l111ll_opy_ not in [bstack1l111ll_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭≕")] or test == None:
    return None
  return {
    bstack1l111ll_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ≖"): bstack1llll11111l1_opy_ and bstack1l1111ll_opy_(threading.current_thread(), bstack1l111ll_opy_ (u"࠭ࡡ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬ≗"), None) == True and bstack11111111_opy_.bstack1ll1ll1ll_opy_(test[bstack1l111ll_opy_ (u"ࠧࡵࡣࡪࡷࠬ≘")])
  }
def bstack1llll1111ll1_opy_(bs_config, framework):
  bstack1l1ll11l1l_opy_ = False
  bstack11l111l111_opy_ = False
  bstack1llll11111ll_opy_ = False
  if bstack1l111ll_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬ≙") in bs_config:
    bstack1llll11111ll_opy_ = True
  elif bstack1l111ll_opy_ (u"ࠩࡤࡴࡵ࠭≚") in bs_config:
    bstack1l1ll11l1l_opy_ = True
  else:
    bstack11l111l111_opy_ = True
  bstack11lll1l11l_opy_ = {
    bstack1l111ll_opy_ (u"ࠪࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪ≛"): bstack1l11llll_opy_.bstack11l11l1111l_opy_(bs_config, framework),
    bstack1l111ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ≜"): bstack11111111_opy_.bstack1l1l11l11_opy_(bs_config),
    bstack1l111ll_opy_ (u"ࠬࡶࡥࡳࡥࡼࠫ≝"): bs_config.get(bstack1l111ll_opy_ (u"࠭ࡰࡦࡴࡦࡽࠬ≞"), False),
    bstack1l111ll_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡦࠩ≟"): bstack11l111l111_opy_,
    bstack1l111ll_opy_ (u"ࠨࡣࡳࡴࡤࡧࡵࡵࡱࡰࡥࡹ࡫ࠧ≠"): bstack1l1ll11l1l_opy_,
    bstack1l111ll_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡴࡥࡤࡰࡪ࠭≡"): bstack1llll11111ll_opy_
  }
  return bstack11lll1l11l_opy_