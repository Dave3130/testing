# coding: UTF-8
import sys
bstack11l1ll_opy_ = sys.version_info [0] == 2
bstack1111ll1_opy_ = 2048
bstack11llll_opy_ = 7
def bstack11ll1ll_opy_ (bstack1111l11_opy_):
    global bstack1l111l1_opy_
    bstack1llll11_opy_ = ord (bstack1111l11_opy_ [-1])
    bstack1l1lll1_opy_ = bstack1111l11_opy_ [:-1]
    bstack11111l1_opy_ = bstack1llll11_opy_ % len (bstack1l1lll1_opy_)
    bstack1111l_opy_ = bstack1l1lll1_opy_ [:bstack11111l1_opy_] + bstack1l1lll1_opy_ [bstack11111l1_opy_:]
    if bstack11l1ll_opy_:
        bstack11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    else:
        bstack11l11_opy_ = str () .join ([chr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    return eval (bstack11l11_opy_)
import os
import json
import shutil
import tempfile
import threading
import urllib.request
import uuid
from pathlib import Path
import logging
import re
from bstack_utils.helper import bstack1ll1l1l11l1_opy_
bstack11lll111l11_opy_ = 100 * 1024 * 1024 # 100 bstack11lll11111l_opy_
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
bstack1ll111l1l1l_opy_ = bstack1ll1l1l11l1_opy_()
bstack1l1lll1l1l1_opy_ = bstack11ll1ll_opy_ (u"ࠢࡖࡲ࡯ࡳࡦࡪࡥࡥࡃࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࡸ࠳ࠢᙐ")
bstack11lll1ll1l1_opy_ = bstack11ll1ll_opy_ (u"ࠣࡖࡨࡷࡹࡒࡥࡷࡧ࡯ࠦᙑ")
bstack11lll1ll1ll_opy_ = bstack11ll1ll_opy_ (u"ࠤࡅࡹ࡮ࡲࡤࡍࡧࡹࡩࡱࠨᙒ")
bstack11lll1l1lll_opy_ = bstack11ll1ll_opy_ (u"ࠥࡌࡴࡵ࡫ࡍࡧࡹࡩࡱࠨᙓ")
bstack11ll1llll1l_opy_ = bstack11ll1ll_opy_ (u"ࠦࡇࡻࡩ࡭ࡦࡏࡩࡻ࡫࡬ࡉࡱࡲ࡯ࡊࡼࡥ࡯ࡶࠥᙔ")
_11lll11l11l_opy_ = threading.local()
def bstack1ll11l1l1l1_opy_(test_framework_state, test_hook_state):
    bstack11ll1ll_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤ࡙ࠥࡥࡵࠢࡷ࡬ࡪࠦࡣࡶࡴࡵࡩࡳࡺࠠࡵࡧࡶࡸࠥ࡫ࡶࡦࡰࡷࠤࡸࡺࡡࡵࡧࠣ࡭ࡳࠦࡴࡩࡴࡨࡥࡩ࠳࡬ࡰࡥࡤࡰࠥࡹࡴࡰࡴࡤ࡫ࡪ࠴ࠊࠡࠢࠣࠤ࡙࡮ࡩࡴࠢࡩࡹࡳࡩࡴࡪࡱࡱࠤࡸ࡮࡯ࡶ࡮ࡧࠤࡧ࡫ࠠࡤࡣ࡯ࡰࡪࡪࠠࡣࡻࠣࡸ࡭࡫ࠠࡦࡸࡨࡲࡹࠦࡨࡢࡰࡧࡰࡪࡸࠠࠩࡵࡸࡧ࡭ࠦࡡࡴࠢࡷࡶࡦࡩ࡫ࡠࡧࡹࡩࡳࡺࠩࠋࠢࠣࠤࠥࡨࡥࡧࡱࡵࡩࠥࡧ࡮ࡺࠢࡩ࡭ࡱ࡫ࠠࡶࡲ࡯ࡳࡦࡪࡳࠡࡱࡦࡧࡺࡸ࠮ࠋࠢࠣࠤࠥࠨࠢࠣᙕ")
    _11lll11l11l_opy_.test_framework_state = test_framework_state
    _11lll11l11l_opy_.test_hook_state = test_hook_state
def bstack11ll1llllll_opy_():
    bstack11ll1ll_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࡒࡦࡶࡵ࡭ࡪࡼࡥࠡࡶ࡫ࡩࠥࡩࡵࡳࡴࡨࡲࡹࠦࡴࡦࡵࡷࠤࡪࡼࡥ࡯ࡶࠣࡷࡹࡧࡴࡦࠢࡩࡶࡴࡳࠠࡵࡪࡵࡩࡦࡪ࠭࡭ࡱࡦࡥࡱࠦࡳࡵࡱࡵࡥ࡬࡫࠮ࠋࠢࠣࠤࠥࡘࡥࡵࡷࡵࡲࡸࠦࡡࠡࡶࡸࡴࡱ࡫ࠠࠩࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥ࠭ࠢࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡹࡴࡢࡶࡨ࠭ࠥࡵࡲࠡࠪࡑࡳࡳ࡫ࠬࠡࡐࡲࡲࡪ࠯ࠠࡪࡨࠣࡲࡴࡺࠠࡴࡧࡷ࠲ࠏࠦࠠࠡࠢࠥࠦࠧᙖ")
    return (
        getattr(_11lll11l11l_opy_, bstack11ll1ll_opy_ (u"ࠧࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࠧᙗ"), None),
        getattr(_11lll11l11l_opy_, bstack11ll1ll_opy_ (u"ࠨࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡣࡸࡺࡡࡵࡧࠪᙘ"), None)
    )
class bstack1lll1l1ll1_opy_:
    bstack11ll1ll_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࡉ࡭ࡱ࡫ࡕࡱ࡮ࡲࡥࡩ࡫ࡲࠡࡲࡵࡳࡻ࡯ࡤࡦࡵࠣࡪࡺࡴࡣࡵ࡫ࡲࡲࡦࡲࡩࡵࡻࠣࡸࡴࠦࡵࡱ࡮ࡲࡥࡩࠦࡡ࡯ࠢࡤࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࠦࡢࡢࡵࡨࡨࠥࡵ࡮ࠡࡶ࡫ࡩࠥ࡭ࡩࡷࡧࡱࠤ࡫࡯࡬ࡦࠢࡳࡥࡹ࡮࠮ࠋࠢࠣࠤࠥࡏࡴࠡࡵࡸࡴࡵࡵࡲࡵࡵࠣࡦࡴࡺࡨࠡ࡮ࡲࡧࡦࡲࠠࡧ࡫࡯ࡩࠥࡶࡡࡵࡪࡶࠤࡦࡴࡤࠡࡊࡗࡘࡕ࠵ࡈࡕࡖࡓࡗ࡛ࠥࡒࡍࡵ࠯ࠤࡦࡴࡤࠡࡥࡲࡴ࡮࡫ࡳࠡࡶ࡫ࡩࠥ࡬ࡩ࡭ࡧࠣ࡭ࡳࡺ࡯ࠡࡣࠣࡨࡪࡹࡩࡨࡰࡤࡸࡪࡪࠊࠡࠢࠣࠤࡩ࡯ࡲࡦࡥࡷࡳࡷࡿࠠࡸ࡫ࡷ࡬࡮ࡴࠠࡵࡪࡨࠤࡺࡹࡥࡳࠩࡶࠤ࡭ࡵ࡭ࡦࠢࡩࡳࡱࡪࡥࡳࠢࡸࡲࡩ࡫ࡲࠡࢀ࠲࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠲࡙ࡵࡲ࡯ࡢࡦࡨࡨࡆࡺࡴࡢࡥ࡫ࡱࡪࡴࡴࡴ࠰ࠍࠤࠥࠦࠠࡊࡨࠣࡥࡳࠦ࡯ࡱࡶ࡬ࡳࡳࡧ࡬ࠡࡣࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࠥࡶࡡࡳࡣࡰࡩࡹ࡫ࡲࠡࠪ࡬ࡲࠥࡐࡓࡐࡐࠣࡪࡴࡸ࡭ࡢࡶࠬࠤ࡮ࡹࠠࡱࡴࡲࡺ࡮ࡪࡥࡥࠢࡤࡲࡩࠦࡣࡰࡰࡷࡥ࡮ࡴࡳࠡࡣࠣࡸࡷࡻࡴࡩࡻࠣࡺࡦࡲࡵࡦࠌࠣࠤࠥࠦࡦࡰࡴࠣࡸ࡭࡫ࠠ࡬ࡧࡼࠤࠧࡨࡵࡪ࡮ࡧࡅࡹࡺࡡࡤࡪࡰࡩࡳࡺࠢ࠭ࠢࡷ࡬ࡪࠦࡦࡪ࡮ࡨࠤࡼ࡯࡬࡭ࠢࡥࡩࠥࡶ࡬ࡢࡥࡨࡨࠥ࡯࡮ࠡࡶ࡫ࡩࠥࠨࡂࡶ࡫࡯ࡨࡑ࡫ࡶࡦ࡮ࠥࠤ࡫ࡵ࡬ࡥࡧࡵ࠿ࠥࡵࡴࡩࡧࡵࡻ࡮ࡹࡥ࠭ࠌࠣࠤࠥࠦࡩࡵࠢࡧࡩ࡫ࡧࡵ࡭ࡶࡶࠤࡹࡵࠠࠣࡖࡨࡷࡹࡒࡥࡷࡧ࡯ࠦ࠳ࠐࠠࠡࠢࠣࡘ࡭࡯ࡳࠡࡸࡨࡶࡸ࡯࡯࡯ࠢࡲࡪࠥࡧࡤࡥࡡࡤࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࠦࡩࡴࠢࡤࠤࡻࡵࡩࡥࠢࡰࡩࡹ࡮࡯ࡥ⠖࡬ࡸࠥ࡮ࡡ࡯ࡦ࡯ࡩࡸࠦࡡ࡭࡮ࠣࡩࡷࡸ࡯ࡳࡵࠣ࡫ࡷࡧࡣࡦࡨࡸࡰࡱࡿࠠࡣࡻࠣࡰࡴ࡭ࡧࡪࡰࡪࠎࠥࠦࠠࠡࡶ࡫ࡩࡲࠦࡡ࡯ࡦࠣࡷ࡮ࡳࡰ࡭ࡻࠣࡶࡪࡺࡵࡳࡰ࡬ࡲ࡬ࠦࡷࡪࡶ࡫ࡳࡺࡺࠠࡵࡪࡵࡳࡼ࡯࡮ࡨࠢࡨࡼࡨ࡫ࡰࡵ࡫ࡲࡲࡸ࠴ࠊࠡࠢࠣࠤࠧࠨࠢᙙ")
    @staticmethod
    def upload_attachment(bstack11lll111ll1_opy_: str, *bstack11ll1llll11_opy_) -> None:
        if not bstack11lll111ll1_opy_ or not bstack11lll111ll1_opy_.strip():
            logger.error(bstack11ll1ll_opy_ (u"ࠥࡥࡩࡪ࡟ࡢࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࠤ࡫ࡧࡩ࡭ࡧࡧ࠾ࠥࡖࡲࡰࡸ࡬ࡨࡪࡪࠠࡧ࡫࡯ࡩࠥࡶࡡࡵࡪࠣ࡭ࡸࠦࡥ࡮ࡲࡷࡽࠥࡵࡲࠡࡐࡲࡲࡪ࠴ࠢᙚ"))
            return
        bstack11lll111111_opy_ = bstack11ll1llll11_opy_[0] if bstack11ll1llll11_opy_ and len(bstack11ll1llll11_opy_) > 0 else None
        bstack11ll1lll1ll_opy_ = None
        test_framework_state, test_hook_state = bstack11ll1llllll_opy_()
        try:
            if bstack11lll111ll1_opy_.startswith(bstack11ll1ll_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼࠲࠳ࠧᙛ")) or bstack11lll111ll1_opy_.startswith(bstack11ll1ll_opy_ (u"ࠧ࡮ࡴࡵࡲࡶ࠾࠴࠵ࠢᙜ")):
                logger.debug(bstack11ll1ll_opy_ (u"ࠨࡐࡢࡶ࡫ࠤ࡮ࡹࠠࡪࡦࡨࡲࡹ࡯ࡦࡪࡧࡧࠤࡦࡹࠠࡖࡔࡏ࠿ࠥࡪ࡯ࡸࡰ࡯ࡳࡦࡪࡩ࡯ࡩࠣࡸ࡭࡫ࠠࡧ࡫࡯ࡩ࠳ࠨᙝ"))
                url = bstack11lll111ll1_opy_
                bstack11lll11l1ll_opy_ = str(uuid.uuid4())
                bstack11lll11l1l1_opy_ = os.path.basename(urllib.request.urlparse(url).path)
                if not bstack11lll11l1l1_opy_ or not bstack11lll11l1l1_opy_.strip():
                    bstack11lll11l1l1_opy_ = bstack11lll11l1ll_opy_
                temp_file = tempfile.NamedTemporaryFile(delete=False,
                                                        prefix=bstack11ll1ll_opy_ (u"ࠢࡶࡲ࡯ࡳࡦࡪ࡟ࠣᙞ") + bstack11lll11l1ll_opy_ + bstack11ll1ll_opy_ (u"ࠣࡡࠥᙟ"),
                                                        suffix=bstack11ll1ll_opy_ (u"ࠤࡢࠦᙠ") + bstack11lll11l1l1_opy_)
                with urllib.request.urlopen(url) as response, open(temp_file.name, bstack11ll1ll_opy_ (u"ࠪࡻࡧ࠭ᙡ")) as out_file:
                    shutil.copyfileobj(response, out_file)
                bstack11ll1lll1ll_opy_ = Path(temp_file.name)
                logger.debug(bstack11ll1ll_opy_ (u"ࠦࡉࡵࡷ࡯࡮ࡲࡥࡩ࡫ࡤࠡࡨ࡬ࡰࡪࠦࡴࡰࠢࡷࡩࡲࡶ࡯ࡳࡣࡵࡽࠥࡲ࡯ࡤࡣࡷ࡭ࡴࡴ࠺ࠡࡽࢀࠦᙢ").format(bstack11ll1lll1ll_opy_))
            else:
                bstack11ll1lll1ll_opy_ = Path(bstack11lll111ll1_opy_)
                logger.debug(bstack11ll1ll_opy_ (u"ࠧࡖࡡࡵࡪࠣ࡭ࡸࠦࡩࡥࡧࡱࡸ࡮࡬ࡩࡦࡦࠣࡥࡸࠦ࡬ࡰࡥࡤࡰࠥ࡬ࡩ࡭ࡧ࠽ࠤࢀࢃࠢᙣ").format(bstack11ll1lll1ll_opy_))
        except Exception as e:
            logger.error(bstack11ll1ll_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡲࡦࡹࡧࡩ࡯ࠢࡩ࡭ࡱ࡫ࠠࡧࡴࡲࡱࠥࡶࡡࡵࡪ࠲࡙ࡗࡒ࠺ࠡࡽࢀࠦᙤ").format(e))
            return
        if bstack11ll1lll1ll_opy_ is None or not bstack11ll1lll1ll_opy_.exists():
            logger.error(bstack11ll1ll_opy_ (u"ࠢࡔࡱࡸࡶࡨ࡫ࠠࡧ࡫࡯ࡩࠥࡪ࡯ࡦࡵࠣࡲࡴࡺࠠࡦࡺ࡬ࡷࡹࡀࠠࡼࡿࠥᙥ").format(bstack11ll1lll1ll_opy_))
            return
        if bstack11ll1lll1ll_opy_.stat().st_size > bstack11lll111l11_opy_:
            logger.error(bstack11ll1ll_opy_ (u"ࠣࡈ࡬ࡰࡪࠦࡳࡪࡼࡨࠤࡪࡾࡣࡦࡧࡧࡷࠥࡳࡡࡹ࡫ࡰࡹࡲࠦࡡ࡭࡮ࡲࡻࡪࡪࠠࡴ࡫ࡽࡩࠥࡵࡦࠡࡽࢀࠦᙦ").format(bstack11lll111l11_opy_))
            return
        bstack11lll1111ll_opy_ = bstack11ll1ll_opy_ (u"ࠤࡗࡩࡸࡺࡌࡦࡸࡨࡰࠧᙧ")
        if bstack11lll111111_opy_:
            try:
                params = json.loads(bstack11lll111111_opy_)
                if bstack11ll1ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡃࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࠧᙨ") in params and params.get(bstack11ll1ll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡄࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࠨᙩ")) is True:
                    bstack11lll1111ll_opy_ = bstack11ll1ll_opy_ (u"ࠧࡈࡵࡪ࡮ࡧࡐࡪࡼࡥ࡭ࠤᙪ")
            except Exception as bstack11lll111l1l_opy_:
                logger.error(bstack11ll1ll_opy_ (u"ࠨࡊࡔࡑࡑࠤࡵࡧࡲࡴ࡫ࡱ࡫ࠥ࡫ࡲࡳࡱࡵࠤ࡮ࡴࠠࡢࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࡔࡦࡸࡡ࡮ࡵ࠽ࠤࢀࢃࠢᙫ").format(bstack11lll111l1l_opy_))
        bstack11lll11ll11_opy_ = False
        from browserstack_sdk.sdk_cli.bstack1l1l1lll11l_opy_ import bstack1l11lll1lll_opy_
        if test_framework_state in bstack1l11lll1lll_opy_.bstack1ll1l1l1l1l_opy_:
            if bstack11lll1111ll_opy_ == bstack11lll1ll1ll_opy_:
                bstack11lll11ll11_opy_ = True
            bstack11lll1111ll_opy_ = bstack11lll1l1lll_opy_
        try:
            platform_index = os.environ[bstack11ll1ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠧᙬ")]
            target_dir = os.path.join(bstack1ll111l1l1l_opy_, bstack1l1lll1l1l1_opy_ + str(platform_index),
                                      bstack11lll1111ll_opy_)
            if bstack11lll11ll11_opy_:
                target_dir = os.path.join(target_dir, bstack11ll1llll1l_opy_)
            os.makedirs(target_dir, exist_ok=True)
            logger.debug(bstack11ll1ll_opy_ (u"ࠣࡅࡵࡩࡦࡺࡥࡥ࠱ࡹࡩࡷ࡯ࡦࡪࡧࡧࠤࡹࡧࡲࡨࡧࡷࠤࡩ࡯ࡲࡦࡥࡷࡳࡷࡿ࠺ࠡࡽࢀࠦ᙭").format(target_dir))
            file_name = os.path.basename(bstack11ll1lll1ll_opy_)
            bstack11lll1111l1_opy_ = os.path.join(target_dir, file_name)
            if os.path.exists(bstack11lll1111l1_opy_):
                base_name, extension = os.path.splitext(file_name)
                bstack11lll111lll_opy_ = 1
                while os.path.exists(os.path.join(target_dir, base_name + str(bstack11lll111lll_opy_) + extension)):
                    bstack11lll111lll_opy_ += 1
                bstack11lll1111l1_opy_ = os.path.join(target_dir, base_name + str(bstack11lll111lll_opy_) + extension)
            shutil.copy(bstack11ll1lll1ll_opy_, bstack11lll1111l1_opy_)
            logger.info(bstack11ll1ll_opy_ (u"ࠤࡉ࡭ࡱ࡫ࠠࡴࡷࡦࡧࡪࡹࡳࡧࡷ࡯ࡰࡾࠦࡣࡰࡲ࡬ࡩࡩࠦࡴࡰ࠼ࠣࡿࢂࠨ᙮").format(bstack11lll1111l1_opy_))
        except Exception as e:
            logger.error(bstack11ll1ll_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡰࡳࡻ࡯࡮ࡨࠢࡩ࡭ࡱ࡫ࠠࡵࡱࠣࡸࡦࡸࡧࡦࡶࠣࡨ࡮ࡸࡥࡤࡶࡲࡶࡾࡀࠠࡼࡿࠥᙯ").format(e))
            return
        finally:
            if bstack11lll111ll1_opy_.startswith(bstack11ll1ll_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼࠲࠳ࠧᙰ")) or bstack11lll111ll1_opy_.startswith(bstack11ll1ll_opy_ (u"ࠧ࡮ࡴࡵࡲࡶ࠾࠴࠵ࠢᙱ")):
                try:
                    if bstack11ll1lll1ll_opy_ is not None and bstack11ll1lll1ll_opy_.exists():
                        bstack11ll1lll1ll_opy_.unlink()
                        logger.debug(bstack11ll1ll_opy_ (u"ࠨࡔࡦ࡯ࡳࡳࡷࡧࡲࡺࠢࡩ࡭ࡱ࡫ࠠࡥࡧ࡯ࡩࡹ࡫ࡤ࠻ࠢࡾࢁࠧᙲ").format(bstack11ll1lll1ll_opy_))
                except Exception as ex:
                    logger.error(bstack11ll1ll_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡤࡦ࡮ࡨࡸ࡮ࡴࡧࠡࡶࡨࡱࡵࡵࡲࡢࡴࡼࠤ࡫࡯࡬ࡦ࠼ࠣࡿࢂࠨᙳ").format(ex))
    @staticmethod
    def bstack1l11l11l1l_opy_() -> None:
        bstack11ll1ll_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡊࡥ࡭ࡧࡷࡩࡸࠦࡡ࡭࡮ࠣࡪࡴࡲࡤࡦࡴࡶࠤࡼ࡮࡯ࡴࡧࠣࡲࡦࡳࡥࡴࠢࡶࡸࡦࡸࡴࠡࡹ࡬ࡸ࡭ࠦࠢࡖࡲ࡯ࡳࡦࡪࡥࡥࡃࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࡸ࠳ࠢࠡࡨࡲࡰࡱࡵࡷࡦࡦࠣࡦࡾࠦࡡࠡࡰࡸࡱࡧ࡫ࡲࠡ࡫ࡱࠎࠥࠦࠠࠡࠢࠣࠤࠥࡺࡨࡦࠢࡸࡷࡪࡸࠧࡴࠢࢁ࠳࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡩ࡯ࡲࡦࡥࡷࡳࡷࡿ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧᙴ")
        bstack11lll11l111_opy_ = bstack1ll1l1l11l1_opy_()
        pattern = re.compile(bstack11ll1ll_opy_ (u"ࡴ࡙ࠥࡵࡲ࡯ࡢࡦࡨࡨࡆࡺࡴࡢࡥ࡫ࡱࡪࡴࡴࡴ࠯࡟ࡨ࠰ࠨᙵ"))
        if os.path.exists(bstack11lll11l111_opy_):
            for item in os.listdir(bstack11lll11l111_opy_):
                bstack11ll1lllll1_opy_ = os.path.join(bstack11lll11l111_opy_, item)
                if os.path.isdir(bstack11ll1lllll1_opy_) and pattern.fullmatch(item):
                    try:
                        shutil.rmtree(bstack11ll1lllll1_opy_)
                    except Exception as e:
                        logger.error(bstack11ll1ll_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡧࡩࡱ࡫ࡴࡪࡰࡪࠤࡩ࡯ࡲࡦࡥࡷࡳࡷࡿ࠺ࠡࡽࢀࠦᙶ").format(e))
        else:
            logger.info(bstack11ll1ll_opy_ (u"࡙ࠦ࡮ࡥࠡࡦ࡬ࡶࡪࡩࡴࡰࡴࡼࠤࡩࡵࡥࡴࠢࡱࡳࡹࠦࡥࡹ࡫ࡶࡸ࠿ࠦࡻࡾࠤᙷ").format(bstack11lll11l111_opy_))