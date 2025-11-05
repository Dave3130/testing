# coding: UTF-8
import sys
bstack1111l1_opy_ = sys.version_info [0] == 2
bstack1l1ll11_opy_ = 2048
bstack11l11l_opy_ = 7
def bstack11111_opy_ (bstack11lll_opy_):
    global bstack111l1l1_opy_
    bstack1l1l1_opy_ = ord (bstack11lll_opy_ [-1])
    bstack1l111ll_opy_ = bstack11lll_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1l111ll_opy_)
    bstack1l11l11_opy_ = bstack1l111ll_opy_ [:bstack1l1l11_opy_] + bstack1l111ll_opy_ [bstack1l1l11_opy_:]
    if bstack1111l1_opy_:
        bstack1llll11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    else:
        bstack1llll11_opy_ = str () .join ([chr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    return eval (bstack1llll11_opy_)
import json
import os
import threading
from bstack_utils.config import Config
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.helper import bstack11l1lllll11_opy_, bstack1l111l11l1_opy_, bstack1lll1lll_opy_, bstack1ll11l1ll1_opy_, \
    bstack11l1lllll1l_opy_
from bstack_utils.measure import measure
def bstack11l1l1111l_opy_(bstack11l1llll1l1_opy_):
    for driver in bstack11l1llll1l1_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
@measure(event_name=EVENTS.bstack1llll1l11l_opy_, stage=STAGE.bstack111l1l11l_opy_)
def bstack11l1ll1111_opy_(driver, status, reason=bstack11111_opy_ (u"᜴ࠫࠬ")):
    bstack111lll11_opy_ = Config.bstack1111llll_opy_()
    if bstack111lll11_opy_.bstack1111l11l_opy_():
        return
    bstack11ll1ll11l_opy_ = bstack1l1111111l_opy_(bstack11111_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠨ᜵"), bstack11111_opy_ (u"࠭ࠧ᜶"), status, reason, bstack11111_opy_ (u"ࠧࠨ᜷"), bstack11111_opy_ (u"ࠨࠩ᜸"))
    driver.execute_script(bstack11ll1ll11l_opy_)
@measure(event_name=EVENTS.bstack1llll1l11l_opy_, stage=STAGE.bstack111l1l11l_opy_)
def bstack1111l1l11_opy_(page, status, reason=bstack11111_opy_ (u"ࠩࠪ᜹")):
    try:
        if page is None:
            return
        bstack111lll11_opy_ = Config.bstack1111llll_opy_()
        if bstack111lll11_opy_.bstack1111l11l_opy_():
            return
        bstack11ll1ll11l_opy_ = bstack1l1111111l_opy_(bstack11111_opy_ (u"ࠪࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸ࠭᜺"), bstack11111_opy_ (u"ࠫࠬ᜻"), status, reason, bstack11111_opy_ (u"ࠬ࠭᜼"), bstack11111_opy_ (u"࠭ࠧ᜽"))
        page.evaluate(bstack11111_opy_ (u"ࠢࡠࠢࡀࡂࠥࢁࡽࠣ᜾"), bstack11ll1ll11l_opy_)
    except Exception as e:
        print(bstack11111_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡴࡧࡷࡸ࡮ࡴࡧࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡶࡸࡦࡺࡵࡴࠢࡩࡳࡷࠦࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠣࡿࢂࠨ᜿"), e)
def bstack1l1111111l_opy_(type, name, status, reason, bstack1l11l1lll_opy_, bstack11l11l1lll_opy_):
    bstack1l1l111ll_opy_ = {
        bstack11111_opy_ (u"ࠩࡤࡧࡹ࡯࡯࡯ࠩᝀ"): type,
        bstack11111_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ᝁ"): {}
    }
    if type == bstack11111_opy_ (u"ࠫࡦࡴ࡮ࡰࡶࡤࡸࡪ࠭ᝂ"):
        bstack1l1l111ll_opy_[bstack11111_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨᝃ")][bstack11111_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬᝄ")] = bstack1l11l1lll_opy_
        bstack1l1l111ll_opy_[bstack11111_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪᝅ")][bstack11111_opy_ (u"ࠨࡦࡤࡸࡦ࠭ᝆ")] = json.dumps(str(bstack11l11l1lll_opy_))
    if type == bstack11111_opy_ (u"ࠩࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪᝇ"):
        bstack1l1l111ll_opy_[bstack11111_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ᝈ")][bstack11111_opy_ (u"ࠫࡳࡧ࡭ࡦࠩᝉ")] = name
    if type == bstack11111_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠨᝊ"):
        bstack1l1l111ll_opy_[bstack11111_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩᝋ")][bstack11111_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧᝌ")] = status
        if status == bstack11111_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨᝍ") and str(reason) != bstack11111_opy_ (u"ࠤࠥᝎ"):
            bstack1l1l111ll_opy_[bstack11111_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ᝏ")][bstack11111_opy_ (u"ࠫࡷ࡫ࡡࡴࡱࡱࠫᝐ")] = json.dumps(str(reason))
    bstack1l1ll11ll_opy_ = bstack11111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࡿࠪᝑ").format(json.dumps(bstack1l1l111ll_opy_))
    return bstack1l1ll11ll_opy_
def bstack11ll11lll1_opy_(url, config, logger, bstack11llll11ll_opy_=False):
    hostname = bstack1l111l11l1_opy_(url)
    is_private = bstack1ll11l1ll1_opy_(hostname)
    try:
        if is_private or bstack11llll11ll_opy_:
            file_path = bstack11l1lllll11_opy_(bstack11111_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ᝒ"), bstack11111_opy_ (u"ࠧ࠯ࡤࡶࡸࡦࡩ࡫࠮ࡥࡲࡲ࡫࡯ࡧ࠯࡬ࡶࡳࡳ࠭ᝓ"), logger)
            if os.environ.get(bstack11111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡍࡑࡆࡅࡑࡥࡎࡐࡖࡢࡗࡊ࡚࡟ࡆࡔࡕࡓࡗ࠭᝔")) and eval(
                    os.environ.get(bstack11111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡎࡒࡇࡆࡒ࡟ࡏࡑࡗࡣࡘࡋࡔࡠࡇࡕࡖࡔࡘࠧ᝕"))):
                return
            if (bstack11111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧ᝖") in config and not config[bstack11111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨ᝗")]):
                os.environ[bstack11111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡑࡕࡃࡂࡎࡢࡒࡔ࡚࡟ࡔࡇࡗࡣࡊࡘࡒࡐࡔࠪ᝘")] = str(True)
                bstack11l1llll11l_opy_ = {bstack11111_opy_ (u"࠭ࡨࡰࡵࡷࡲࡦࡳࡥࠨ᝙"): hostname}
                bstack11l1lllll1l_opy_(bstack11111_opy_ (u"ࠧ࠯ࡤࡶࡸࡦࡩ࡫࠮ࡥࡲࡲ࡫࡯ࡧ࠯࡬ࡶࡳࡳ࠭᝚"), bstack11111_opy_ (u"ࠨࡰࡸࡨ࡬࡫࡟࡭ࡱࡦࡥࡱ࠭᝛"), bstack11l1llll11l_opy_, logger)
    except Exception as e:
        pass
def bstack111l1l11l1_opy_(caps, bstack11l1llllll1_opy_):
    if bstack11111_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪ᝜") in caps:
        caps[bstack11111_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫ᝝")][bstack11111_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࠪ᝞")] = True
        if bstack11l1llllll1_opy_:
            caps[bstack11111_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭᝟")][bstack11111_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨᝠ")] = bstack11l1llllll1_opy_
    else:
        caps[bstack11111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴࡬ࡰࡥࡤࡰࠬᝡ")] = True
        if bstack11l1llllll1_opy_:
            caps[bstack11111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩᝢ")] = bstack11l1llllll1_opy_
def bstack11l1lllllll_opy_(bstack1ll1111l_opy_):
    bstack11l1llll1ll_opy_ = bstack1lll1lll_opy_(threading.current_thread(), bstack11111_opy_ (u"ࠩࡷࡩࡸࡺࡓࡵࡣࡷࡹࡸ࠭ᝣ"), bstack11111_opy_ (u"ࠪࠫᝤ"))
    if bstack11l1llll1ll_opy_ == bstack11111_opy_ (u"ࠫࠬᝥ") or bstack11l1llll1ll_opy_ == bstack11111_opy_ (u"ࠬࡹ࡫ࡪࡲࡳࡩࡩ࠭ᝦ"):
        threading.current_thread().testStatus = bstack1ll1111l_opy_
    else:
        if bstack1ll1111l_opy_ == bstack11111_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ᝧ"):
            threading.current_thread().testStatus = bstack1ll1111l_opy_