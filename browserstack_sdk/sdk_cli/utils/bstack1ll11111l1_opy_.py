# coding: UTF-8
import sys
bstack1l11l_opy_ = sys.version_info [0] == 2
bstack1111_opy_ = 2048
bstack1lll1_opy_ = 7
def bstack1lllll1l_opy_ (bstack1ll1l11_opy_):
    global bstack11l1ll_opy_
    bstack111lll_opy_ = ord (bstack1ll1l11_opy_ [-1])
    bstack1l111l1_opy_ = bstack1ll1l11_opy_ [:-1]
    bstack1111l_opy_ = bstack111lll_opy_ % len (bstack1l111l1_opy_)
    bstack1111ll_opy_ = bstack1l111l1_opy_ [:bstack1111l_opy_] + bstack1l111l1_opy_ [bstack1111l_opy_:]
    if bstack1l11l_opy_:
        bstack1l1l1_opy_ = unicode () .join ([unichr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    else:
        bstack1l1l1_opy_ = str () .join ([chr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    return eval (bstack1l1l1_opy_)
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
from bstack_utils.helper import bstack1ll1l1ll11l_opy_
bstack11lll1l1111_opy_ = 100 * 1024 * 1024 # 100 bstack11lll11l1l1_opy_
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
bstack1ll11ll1111_opy_ = bstack1ll1l1ll11l_opy_()
bstack1ll11lll11l_opy_ = bstack1lllll1l_opy_ (u"࡚ࠦࡶ࡬ࡰࡣࡧࡩࡩࡇࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࡵ࠰ࠦᘱ")
bstack11llll11l11_opy_ = bstack1lllll1l_opy_ (u"࡚ࠧࡥࡴࡶࡏࡩࡻ࡫࡬ࠣᘲ")
bstack11llll11111_opy_ = bstack1lllll1l_opy_ (u"ࠨࡂࡶ࡫࡯ࡨࡑ࡫ࡶࡦ࡮ࠥᘳ")
bstack11llll111l1_opy_ = bstack1lllll1l_opy_ (u"ࠢࡉࡱࡲ࡯ࡑ࡫ࡶࡦ࡮ࠥᘴ")
bstack11lll11l11l_opy_ = bstack1lllll1l_opy_ (u"ࠣࡄࡸ࡭ࡱࡪࡌࡦࡸࡨࡰࡍࡵ࡯࡬ࡇࡹࡩࡳࡺࠢᘵ")
_11lll111l1l_opy_ = threading.local()
def bstack1l1lll1llll_opy_(test_framework_state, test_hook_state):
    bstack1lllll1l_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࡖࡩࡹࠦࡴࡩࡧࠣࡧࡺࡸࡲࡦࡰࡷࠤࡹ࡫ࡳࡵࠢࡨࡺࡪࡴࡴࠡࡵࡷࡥࡹ࡫ࠠࡪࡰࠣࡸ࡭ࡸࡥࡢࡦ࠰ࡰࡴࡩࡡ࡭ࠢࡶࡸࡴࡸࡡࡨࡧ࠱ࠎࠥࠦࠠࠡࡖ࡫࡭ࡸࠦࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠡࡵ࡫ࡳࡺࡲࡤࠡࡤࡨࠤࡨࡧ࡬࡭ࡧࡧࠤࡧࡿࠠࡵࡪࡨࠤࡪࡼࡥ࡯ࡶࠣ࡬ࡦࡴࡤ࡭ࡧࡵࠤ࠭ࡹࡵࡤࡪࠣࡥࡸࠦࡴࡳࡣࡦ࡯ࡤ࡫ࡶࡦࡰࡷ࠭ࠏࠦࠠࠡࠢࡥࡩ࡫ࡵࡲࡦࠢࡤࡲࡾࠦࡦࡪ࡮ࡨࠤࡺࡶ࡬ࡰࡣࡧࡷࠥࡵࡣࡤࡷࡵ࠲ࠏࠦࠠࠡࠢࠥࠦࠧᘶ")
    _11lll111l1l_opy_.test_framework_state = test_framework_state
    _11lll111l1l_opy_.test_hook_state = test_hook_state
def bstack11lll11ll11_opy_():
    bstack1lllll1l_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࡖࡪࡺࡲࡪࡧࡹࡩࠥࡺࡨࡦࠢࡦࡹࡷࡸࡥ࡯ࡶࠣࡸࡪࡹࡴࠡࡧࡹࡩࡳࡺࠠࡴࡶࡤࡸࡪࠦࡦࡳࡱࡰࠤࡹ࡮ࡲࡦࡣࡧ࠱ࡱࡵࡣࡢ࡮ࠣࡷࡹࡵࡲࡢࡩࡨ࠲ࠏࠦࠠࠡࠢࡕࡩࡹࡻࡲ࡯ࡵࠣࡥࠥࡺࡵࡱ࡮ࡨࠤ࠭ࡺࡥࡴࡶࡢࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩ࠱ࠦࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡡࡶࡸࡦࡺࡥࠪࠢࡲࡶࠥ࠮ࡎࡰࡰࡨ࠰ࠥࡔ࡯࡯ࡧࠬࠤ࡮࡬ࠠ࡯ࡱࡷࠤࡸ࡫ࡴ࠯ࠌࠣࠤࠥࠦࠢࠣࠤᘷ")
    return (
        getattr(_11lll111l1l_opy_, bstack1lllll1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡴࡢࡶࡨࠫᘸ"), None),
        getattr(_11lll111l1l_opy_, bstack1lllll1l_opy_ (u"ࠬࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡠࡵࡷࡥࡹ࡫ࠧᘹ"), None)
    )
class bstack11l111l11l_opy_:
    bstack1lllll1l_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࡆࡪ࡮ࡨ࡙ࡵࡲ࡯ࡢࡦࡨࡶࠥࡶࡲࡰࡸ࡬ࡨࡪࡹࠠࡧࡷࡱࡧࡹ࡯࡯࡯ࡣ࡯࡭ࡹࡿࠠࡵࡱࠣࡹࡵࡲ࡯ࡢࡦࠣࡥࡳࠦࡡࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࠣࡦࡦࡹࡥࡥࠢࡲࡲࠥࡺࡨࡦࠢࡪ࡭ࡻ࡫࡮ࠡࡨ࡬ࡰࡪࠦࡰࡢࡶ࡫࠲ࠏࠦࠠࠡࠢࡌࡸࠥࡹࡵࡱࡲࡲࡶࡹࡹࠠࡣࡱࡷ࡬ࠥࡲ࡯ࡤࡣ࡯ࠤ࡫࡯࡬ࡦࠢࡳࡥࡹ࡮ࡳࠡࡣࡱࡨࠥࡎࡔࡕࡒ࠲ࡌ࡙࡚ࡐࡔࠢࡘࡖࡑࡹࠬࠡࡣࡱࡨࠥࡩ࡯ࡱ࡫ࡨࡷࠥࡺࡨࡦࠢࡩ࡭ࡱ࡫ࠠࡪࡰࡷࡳࠥࡧࠠࡥࡧࡶ࡭࡬ࡴࡡࡵࡧࡧࠎࠥࠦࠠࠡࡦ࡬ࡶࡪࡩࡴࡰࡴࡼࠤࡼ࡯ࡴࡩ࡫ࡱࠤࡹ࡮ࡥࠡࡷࡶࡩࡷ࠭ࡳࠡࡪࡲࡱࡪࠦࡦࡰ࡮ࡧࡩࡷࠦࡵ࡯ࡦࡨࡶࠥࢄ࠯࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠯ࡖࡲ࡯ࡳࡦࡪࡥࡥࡃࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࡸ࠴ࠊࠡࠢࠣࠤࡎ࡬ࠠࡢࡰࠣࡳࡵࡺࡩࡰࡰࡤࡰࠥࡧࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࠢࡳࡥࡷࡧ࡭ࡦࡶࡨࡶࠥ࠮ࡩ࡯ࠢࡍࡗࡔࡔࠠࡧࡱࡵࡱࡦࡺࠩࠡ࡫ࡶࠤࡵࡸ࡯ࡷ࡫ࡧࡩࡩࠦࡡ࡯ࡦࠣࡧࡴࡴࡴࡢ࡫ࡱࡷࠥࡧࠠࡵࡴࡸࡸ࡭ࡿࠠࡷࡣ࡯ࡹࡪࠐࠠࠡࠢࠣࡪࡴࡸࠠࡵࡪࡨࠤࡰ࡫ࡹࠡࠤࡥࡹ࡮ࡲࡤࡂࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࠦ࠱ࠦࡴࡩࡧࠣࡪ࡮ࡲࡥࠡࡹ࡬ࡰࡱࠦࡢࡦࠢࡳࡰࡦࡩࡥࡥࠢ࡬ࡲࠥࡺࡨࡦࠢࠥࡆࡺ࡯࡬ࡥࡎࡨࡺࡪࡲࠢࠡࡨࡲࡰࡩ࡫ࡲ࠼ࠢࡲࡸ࡭࡫ࡲࡸ࡫ࡶࡩ࠱ࠐࠠࠡࠢࠣ࡭ࡹࠦࡤࡦࡨࡤࡹࡱࡺࡳࠡࡶࡲࠤ࡚ࠧࡥࡴࡶࡏࡩࡻ࡫࡬ࠣ࠰ࠍࠤࠥࠦࠠࡕࡪ࡬ࡷࠥࡼࡥࡳࡵ࡬ࡳࡳࠦ࡯ࡧࠢࡤࡨࡩࡥࡡࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࠣ࡭ࡸࠦࡡࠡࡸࡲ࡭ࡩࠦ࡭ࡦࡶ࡫ࡳࡩ⠚ࡩࡵࠢ࡫ࡥࡳࡪ࡬ࡦࡵࠣࡥࡱࡲࠠࡦࡴࡵࡳࡷࡹࠠࡨࡴࡤࡧࡪ࡬ࡵ࡭࡮ࡼࠤࡧࡿࠠ࡭ࡱࡪ࡫࡮ࡴࡧࠋࠢࠣࠤࠥࡺࡨࡦ࡯ࠣࡥࡳࡪࠠࡴ࡫ࡰࡴࡱࡿࠠࡳࡧࡷࡹࡷࡴࡩ࡯ࡩࠣࡻ࡮ࡺࡨࡰࡷࡷࠤࡹ࡮ࡲࡰࡹ࡬ࡲ࡬ࠦࡥࡹࡥࡨࡴࡹ࡯࡯࡯ࡵ࠱ࠎࠥࠦࠠࠡࠤࠥࠦᘺ")
    @staticmethod
    def upload_attachment(bstack11lll1l1l1l_opy_: str, *bstack11lll11llll_opy_) -> None:
        if not bstack11lll1l1l1l_opy_ or not bstack11lll1l1l1l_opy_.strip():
            logger.error(bstack1lllll1l_opy_ (u"ࠢࡢࡦࡧࡣࡦࡺࡴࡢࡥ࡫ࡱࡪࡴࡴࠡࡨࡤ࡭ࡱ࡫ࡤ࠻ࠢࡓࡶࡴࡼࡩࡥࡧࡧࠤ࡫࡯࡬ࡦࠢࡳࡥࡹ࡮ࠠࡪࡵࠣࡩࡲࡶࡴࡺࠢࡲࡶࠥࡔ࡯࡯ࡧ࠱ࠦᘻ"))
            return
        bstack11lll1l11l1_opy_ = bstack11lll11llll_opy_[0] if bstack11lll11llll_opy_ and len(bstack11lll11llll_opy_) > 0 else None
        bstack11lll1l1l11_opy_ = None
        test_framework_state, test_hook_state = bstack11lll11ll11_opy_()
        try:
            if bstack11lll1l1l1l_opy_.startswith(bstack1lllll1l_opy_ (u"ࠣࡪࡷࡸࡵࡀ࠯࠰ࠤᘼ")) or bstack11lll1l1l1l_opy_.startswith(bstack1lllll1l_opy_ (u"ࠤ࡫ࡸࡹࡶࡳ࠻࠱࠲ࠦᘽ")):
                logger.debug(bstack1lllll1l_opy_ (u"ࠥࡔࡦࡺࡨࠡ࡫ࡶࠤ࡮ࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡤࠡࡣࡶࠤ࡚ࡘࡌ࠼ࠢࡧࡳࡼࡴ࡬ࡰࡣࡧ࡭ࡳ࡭ࠠࡵࡪࡨࠤ࡫࡯࡬ࡦ࠰ࠥᘾ"))
                url = bstack11lll1l1l1l_opy_
                bstack11lll1l111l_opy_ = str(uuid.uuid4())
                bstack11lll1l11ll_opy_ = os.path.basename(urllib.request.urlparse(url).path)
                if not bstack11lll1l11ll_opy_ or not bstack11lll1l11ll_opy_.strip():
                    bstack11lll1l11ll_opy_ = bstack11lll1l111l_opy_
                temp_file = tempfile.NamedTemporaryFile(delete=False,
                                                        prefix=bstack1lllll1l_opy_ (u"ࠦࡺࡶ࡬ࡰࡣࡧࡣࠧᘿ") + bstack11lll1l111l_opy_ + bstack1lllll1l_opy_ (u"ࠧࡥࠢᙀ"),
                                                        suffix=bstack1lllll1l_opy_ (u"ࠨ࡟ࠣᙁ") + bstack11lll1l11ll_opy_)
                with urllib.request.urlopen(url) as response, open(temp_file.name, bstack1lllll1l_opy_ (u"ࠧࡸࡤࠪᙂ")) as out_file:
                    shutil.copyfileobj(response, out_file)
                bstack11lll1l1l11_opy_ = Path(temp_file.name)
                logger.debug(bstack1lllll1l_opy_ (u"ࠣࡆࡲࡻࡳࡲ࡯ࡢࡦࡨࡨࠥ࡬ࡩ࡭ࡧࠣࡸࡴࠦࡴࡦ࡯ࡳࡳࡷࡧࡲࡺࠢ࡯ࡳࡨࡧࡴࡪࡱࡱ࠾ࠥࢁࡽࠣᙃ").format(bstack11lll1l1l11_opy_))
            else:
                bstack11lll1l1l11_opy_ = Path(bstack11lll1l1l1l_opy_)
                logger.debug(bstack1lllll1l_opy_ (u"ࠤࡓࡥࡹ࡮ࠠࡪࡵࠣ࡭ࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡪࠠࡢࡵࠣࡰࡴࡩࡡ࡭ࠢࡩ࡭ࡱ࡫࠺ࠡࡽࢀࠦᙄ").format(bstack11lll1l1l11_opy_))
        except Exception as e:
            logger.error(bstack1lllll1l_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦ࡯ࡣࡶࡤ࡭ࡳࠦࡦࡪ࡮ࡨࠤ࡫ࡸ࡯࡮ࠢࡳࡥࡹ࡮࠯ࡖࡔࡏ࠾ࠥࢁࡽࠣᙅ").format(e))
            return
        if bstack11lll1l1l11_opy_ is None or not bstack11lll1l1l11_opy_.exists():
            logger.error(bstack1lllll1l_opy_ (u"ࠦࡘࡵࡵࡳࡥࡨࠤ࡫࡯࡬ࡦࠢࡧࡳࡪࡹࠠ࡯ࡱࡷࠤࡪࡾࡩࡴࡶ࠽ࠤࢀࢃࠢᙆ").format(bstack11lll1l1l11_opy_))
            return
        if bstack11lll1l1l11_opy_.stat().st_size > bstack11lll1l1111_opy_:
            logger.error(bstack1lllll1l_opy_ (u"ࠧࡌࡩ࡭ࡧࠣࡷ࡮ࢀࡥࠡࡧࡻࡧࡪ࡫ࡤࡴࠢࡰࡥࡽ࡯࡭ࡶ࡯ࠣࡥࡱࡲ࡯ࡸࡧࡧࠤࡸ࡯ࡺࡦࠢࡲࡪࠥࢁࡽࠣᙇ").format(bstack11lll1l1111_opy_))
            return
        bstack11lll11ll1l_opy_ = bstack1lllll1l_opy_ (u"ࠨࡔࡦࡵࡷࡐࡪࡼࡥ࡭ࠤᙈ")
        if bstack11lll1l11l1_opy_:
            try:
                params = json.loads(bstack11lll1l11l1_opy_)
                if bstack1lllll1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡇࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࠤᙉ") in params and params.get(bstack1lllll1l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪࡁࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࠥᙊ")) is True:
                    bstack11lll11ll1l_opy_ = bstack1lllll1l_opy_ (u"ࠤࡅࡹ࡮ࡲࡤࡍࡧࡹࡩࡱࠨᙋ")
            except Exception as bstack11lll11l1ll_opy_:
                logger.error(bstack1lllll1l_opy_ (u"ࠥࡎࡘࡕࡎࠡࡲࡤࡶࡸ࡯࡮ࡨࠢࡨࡶࡷࡵࡲࠡ࡫ࡱࠤࡦࡺࡴࡢࡥ࡫ࡱࡪࡴࡴࡑࡣࡵࡥࡲࡹ࠺ࠡࡽࢀࠦᙌ").format(bstack11lll11l1ll_opy_))
        bstack11lll11l111_opy_ = False
        from browserstack_sdk.sdk_cli.bstack1l1l1l1l1l1_opy_ import bstack1l1l1ll111l_opy_
        if test_framework_state in bstack1l1l1ll111l_opy_.bstack1ll11l11l1l_opy_:
            if bstack11lll11ll1l_opy_ == bstack11llll11111_opy_:
                bstack11lll11l111_opy_ = True
            bstack11lll11ll1l_opy_ = bstack11llll111l1_opy_
        try:
            platform_index = os.environ[bstack1lllll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠫᙍ")]
            target_dir = os.path.join(bstack1ll11ll1111_opy_, bstack1ll11lll11l_opy_ + str(platform_index),
                                      bstack11lll11ll1l_opy_)
            if bstack11lll11l111_opy_:
                target_dir = os.path.join(target_dir, bstack11lll11l11l_opy_)
            os.makedirs(target_dir, exist_ok=True)
            logger.debug(bstack1lllll1l_opy_ (u"ࠧࡉࡲࡦࡣࡷࡩࡩ࠵ࡶࡦࡴ࡬ࡪ࡮࡫ࡤࠡࡶࡤࡶ࡬࡫ࡴࠡࡦ࡬ࡶࡪࡩࡴࡰࡴࡼ࠾ࠥࢁࡽࠣᙎ").format(target_dir))
            file_name = os.path.basename(bstack11lll1l1l11_opy_)
            bstack11lll111l11_opy_ = os.path.join(target_dir, file_name)
            if os.path.exists(bstack11lll111l11_opy_):
                base_name, extension = os.path.splitext(file_name)
                bstack11lll111lll_opy_ = 1
                while os.path.exists(os.path.join(target_dir, base_name + str(bstack11lll111lll_opy_) + extension)):
                    bstack11lll111lll_opy_ += 1
                bstack11lll111l11_opy_ = os.path.join(target_dir, base_name + str(bstack11lll111lll_opy_) + extension)
            shutil.copy(bstack11lll1l1l11_opy_, bstack11lll111l11_opy_)
            logger.info(bstack1lllll1l_opy_ (u"ࠨࡆࡪ࡮ࡨࠤࡸࡻࡣࡤࡧࡶࡷ࡫ࡻ࡬࡭ࡻࠣࡧࡴࡶࡩࡦࡦࠣࡸࡴࡀࠠࡼࡿࠥᙏ").format(bstack11lll111l11_opy_))
        except Exception as e:
            logger.error(bstack1lllll1l_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦ࡭ࡰࡸ࡬ࡲ࡬ࠦࡦࡪ࡮ࡨࠤࡹࡵࠠࡵࡣࡵ࡫ࡪࡺࠠࡥ࡫ࡵࡩࡨࡺ࡯ࡳࡻ࠽ࠤࢀࢃࠢᙐ").format(e))
            return
        finally:
            if bstack11lll1l1l1l_opy_.startswith(bstack1lllll1l_opy_ (u"ࠣࡪࡷࡸࡵࡀ࠯࠰ࠤᙑ")) or bstack11lll1l1l1l_opy_.startswith(bstack1lllll1l_opy_ (u"ࠤ࡫ࡸࡹࡶࡳ࠻࠱࠲ࠦᙒ")):
                try:
                    if bstack11lll1l1l11_opy_ is not None and bstack11lll1l1l11_opy_.exists():
                        bstack11lll1l1l11_opy_.unlink()
                        logger.debug(bstack1lllll1l_opy_ (u"ࠥࡘࡪࡳࡰࡰࡴࡤࡶࡾࠦࡦࡪ࡮ࡨࠤࡩ࡫࡬ࡦࡶࡨࡨ࠿ࠦࡻࡾࠤᙓ").format(bstack11lll1l1l11_opy_))
                except Exception as ex:
                    logger.error(bstack1lllll1l_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡨࡪࡲࡥࡵ࡫ࡱ࡫ࠥࡺࡥ࡮ࡲࡲࡶࡦࡸࡹࠡࡨ࡬ࡰࡪࡀࠠࡼࡿࠥᙔ").format(ex))
    @staticmethod
    def bstack11ll1l11l_opy_() -> None:
        bstack1lllll1l_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡇࡩࡱ࡫ࡴࡦࡵࠣࡥࡱࡲࠠࡧࡱ࡯ࡨࡪࡸࡳࠡࡹ࡫ࡳࡸ࡫ࠠ࡯ࡣࡰࡩࡸࠦࡳࡵࡣࡵࡸࠥࡽࡩࡵࡪ࡚ࠣࠦࡶ࡬ࡰࡣࡧࡩࡩࡇࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࡵ࠰ࠦࠥ࡬࡯࡭࡮ࡲࡻࡪࡪࠠࡣࡻࠣࡥࠥࡴࡵ࡮ࡤࡨࡶࠥ࡯࡮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡷ࡬ࡪࠦࡵࡴࡧࡵࠫࡸࠦࡾ࠰࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠡࡦ࡬ࡶࡪࡩࡴࡰࡴࡼ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤᙕ")
        bstack11lll111ll1_opy_ = bstack1ll1l1ll11l_opy_()
        pattern = re.compile(bstack1lllll1l_opy_ (u"ࡸࠢࡖࡲ࡯ࡳࡦࡪࡥࡥࡃࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࡸ࠳࡜ࡥ࠭ࠥᙖ"))
        if os.path.exists(bstack11lll111ll1_opy_):
            for item in os.listdir(bstack11lll111ll1_opy_):
                bstack11lll11lll1_opy_ = os.path.join(bstack11lll111ll1_opy_, item)
                if os.path.isdir(bstack11lll11lll1_opy_) and pattern.fullmatch(item):
                    try:
                        shutil.rmtree(bstack11lll11lll1_opy_)
                    except Exception as e:
                        logger.error(bstack1lllll1l_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡤࡦ࡮ࡨࡸ࡮ࡴࡧࠡࡦ࡬ࡶࡪࡩࡴࡰࡴࡼ࠾ࠥࢁࡽࠣᙗ").format(e))
        else:
            logger.info(bstack1lllll1l_opy_ (u"ࠣࡖ࡫ࡩࠥࡪࡩࡳࡧࡦࡸࡴࡸࡹࠡࡦࡲࡩࡸࠦ࡮ࡰࡶࠣࡩࡽ࡯ࡳࡵ࠼ࠣࡿࢂࠨᙘ").format(bstack11lll111ll1_opy_))