# coding: UTF-8
import sys
bstack1ll1111_opy_ = sys.version_info [0] == 2
bstack1ll_opy_ = 2048
bstack1ll1l1_opy_ = 7
def bstack11l111_opy_ (bstack1ll1_opy_):
    global bstack11l1l_opy_
    bstack11l1l1_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack111ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack11111ll_opy_ = bstack11l1l1_opy_ % len (bstack111ll_opy_)
    bstack1l1lll_opy_ = bstack111ll_opy_ [:bstack11111ll_opy_] + bstack111ll_opy_ [bstack11111ll_opy_:]
    if bstack1ll1111_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    return eval (bstack1lll1ll_opy_)
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
from bstack_utils.helper import bstack1ll1l1ll111_opy_
bstack11lll1l1111_opy_ = 100 * 1024 * 1024 # 100 bstack11lll111l11_opy_
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
bstack1ll1l1l1l1l_opy_ = bstack1ll1l1ll111_opy_()
bstack1ll111ll111_opy_ = bstack11l111_opy_ (u"ࠨࡕࡱ࡮ࡲࡥࡩ࡫ࡤࡂࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࡷ࠲ࠨᘳ")
bstack11llll11l11_opy_ = bstack11l111_opy_ (u"ࠢࡕࡧࡶࡸࡑ࡫ࡶࡦ࡮ࠥᘴ")
bstack11llll111ll_opy_ = bstack11l111_opy_ (u"ࠣࡄࡸ࡭ࡱࡪࡌࡦࡸࡨࡰࠧᘵ")
bstack11llll1111l_opy_ = bstack11l111_opy_ (u"ࠤࡋࡳࡴࡱࡌࡦࡸࡨࡰࠧᘶ")
bstack11lll1l111l_opy_ = bstack11l111_opy_ (u"ࠥࡆࡺ࡯࡬ࡥࡎࡨࡺࡪࡲࡈࡰࡱ࡮ࡉࡻ࡫࡮ࡵࠤᘷ")
_11lll111ll1_opy_ = threading.local()
def bstack1ll1l111111_opy_(test_framework_state, test_hook_state):
    bstack11l111_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࡘ࡫ࡴࠡࡶ࡫ࡩࠥࡩࡵࡳࡴࡨࡲࡹࠦࡴࡦࡵࡷࠤࡪࡼࡥ࡯ࡶࠣࡷࡹࡧࡴࡦࠢ࡬ࡲࠥࡺࡨࡳࡧࡤࡨ࠲ࡲ࡯ࡤࡣ࡯ࠤࡸࡺ࡯ࡳࡣࡪࡩ࠳ࠐࠠࠡࠢࠣࡘ࡭࡯ࡳࠡࡨࡸࡲࡨࡺࡩࡰࡰࠣࡷ࡭ࡵࡵ࡭ࡦࠣࡦࡪࠦࡣࡢ࡮࡯ࡩࡩࠦࡢࡺࠢࡷ࡬ࡪࠦࡥࡷࡧࡱࡸࠥ࡮ࡡ࡯ࡦ࡯ࡩࡷࠦࠨࡴࡷࡦ࡬ࠥࡧࡳࠡࡶࡵࡥࡨࡱ࡟ࡦࡸࡨࡲࡹ࠯ࠊࠡࠢࠣࠤࡧ࡫ࡦࡰࡴࡨࠤࡦࡴࡹࠡࡨ࡬ࡰࡪࠦࡵࡱ࡮ࡲࡥࡩࡹࠠࡰࡥࡦࡹࡷ࠴ࠊࠡࠢࠣࠤࠧࠨࠢᘸ")
    _11lll111ll1_opy_.test_framework_state = test_framework_state
    _11lll111ll1_opy_.test_hook_state = test_hook_state
def bstack11lll11l11l_opy_():
    bstack11l111_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࡘࡥࡵࡴ࡬ࡩࡻ࡫ࠠࡵࡪࡨࠤࡨࡻࡲࡳࡧࡱࡸࠥࡺࡥࡴࡶࠣࡩࡻ࡫࡮ࡵࠢࡶࡸࡦࡺࡥࠡࡨࡵࡳࡲࠦࡴࡩࡴࡨࡥࡩ࠳࡬ࡰࡥࡤࡰࠥࡹࡴࡰࡴࡤ࡫ࡪ࠴ࠊࠡࠢࠣࠤࡗ࡫ࡴࡶࡴࡱࡷࠥࡧࠠࡵࡷࡳࡰࡪࠦࠨࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࠬࠡࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡣࡸࡺࡡࡵࡧࠬࠤࡴࡸࠠࠩࡐࡲࡲࡪ࠲ࠠࡏࡱࡱࡩ࠮ࠦࡩࡧࠢࡱࡳࡹࠦࡳࡦࡶ࠱ࠎࠥࠦࠠࠡࠤࠥࠦᘹ")
    return (
        getattr(_11lll111ll1_opy_, bstack11l111_opy_ (u"࠭ࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪ࠭ᘺ"), None),
        getattr(_11lll111ll1_opy_, bstack11l111_opy_ (u"ࠧࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡢࡷࡹࡧࡴࡦࠩᘻ"), None)
    )
class bstack1ll1ll1l1_opy_:
    bstack11l111_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࡈ࡬ࡰࡪ࡛ࡰ࡭ࡱࡤࡨࡪࡸࠠࡱࡴࡲࡺ࡮ࡪࡥࡴࠢࡩࡹࡳࡩࡴࡪࡱࡱࡥࡱ࡯ࡴࡺࠢࡷࡳࠥࡻࡰ࡭ࡱࡤࡨࠥࡧ࡮ࠡࡣࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࠥࡨࡡࡴࡧࡧࠤࡴࡴࠠࡵࡪࡨࠤ࡬࡯ࡶࡦࡰࠣࡪ࡮ࡲࡥࠡࡲࡤࡸ࡭࠴ࠊࠡࠢࠣࠤࡎࡺࠠࡴࡷࡳࡴࡴࡸࡴࡴࠢࡥࡳࡹ࡮ࠠ࡭ࡱࡦࡥࡱࠦࡦࡪ࡮ࡨࠤࡵࡧࡴࡩࡵࠣࡥࡳࡪࠠࡉࡖࡗࡔ࠴ࡎࡔࡕࡒࡖࠤ࡚ࡘࡌࡴ࠮ࠣࡥࡳࡪࠠࡤࡱࡳ࡭ࡪࡹࠠࡵࡪࡨࠤ࡫࡯࡬ࡦࠢ࡬ࡲࡹࡵࠠࡢࠢࡧࡩࡸ࡯ࡧ࡯ࡣࡷࡩࡩࠐࠠࠡࠢࠣࡨ࡮ࡸࡥࡤࡶࡲࡶࡾࠦࡷࡪࡶ࡫࡭ࡳࠦࡴࡩࡧࠣࡹࡸ࡫ࡲࠨࡵࠣ࡬ࡴࡳࡥࠡࡨࡲࡰࡩ࡫ࡲࠡࡷࡱࡨࡪࡸࠠࡿ࠱࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠱ࡘࡴࡱࡵࡡࡥࡧࡧࡅࡹࡺࡡࡤࡪࡰࡩࡳࡺࡳ࠯ࠌࠣࠤࠥࠦࡉࡧࠢࡤࡲࠥࡵࡰࡵ࡫ࡲࡲࡦࡲࠠࡢࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࠤࡵࡧࡲࡢ࡯ࡨࡸࡪࡸࠠࠩ࡫ࡱࠤࡏ࡙ࡏࡏࠢࡩࡳࡷࡳࡡࡵࠫࠣ࡭ࡸࠦࡰࡳࡱࡹ࡭ࡩ࡫ࡤࠡࡣࡱࡨࠥࡩ࡯࡯ࡶࡤ࡭ࡳࡹࠠࡢࠢࡷࡶࡺࡺࡨࡺࠢࡹࡥࡱࡻࡥࠋࠢࠣࠤࠥ࡬࡯ࡳࠢࡷ࡬ࡪࠦ࡫ࡦࡻࠣࠦࡧࡻࡩ࡭ࡦࡄࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࠨࠬࠡࡶ࡫ࡩࠥ࡬ࡩ࡭ࡧࠣࡻ࡮ࡲ࡬ࠡࡤࡨࠤࡵࡲࡡࡤࡧࡧࠤ࡮ࡴࠠࡵࡪࡨࠤࠧࡈࡵࡪ࡮ࡧࡐࡪࡼࡥ࡭ࠤࠣࡪࡴࡲࡤࡦࡴ࠾ࠤࡴࡺࡨࡦࡴࡺ࡭ࡸ࡫ࠬࠋࠢࠣࠤࠥ࡯ࡴࠡࡦࡨࡪࡦࡻ࡬ࡵࡵࠣࡸࡴࠦࠢࡕࡧࡶࡸࡑ࡫ࡶࡦ࡮ࠥ࠲ࠏࠦࠠࠡࠢࡗ࡬࡮ࡹࠠࡷࡧࡵࡷ࡮ࡵ࡮ࠡࡱࡩࠤࡦࡪࡤࡠࡣࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࠥ࡯ࡳࠡࡣࠣࡺࡴ࡯ࡤࠡ࡯ࡨࡸ࡭ࡵࡤ⠕࡫ࡷࠤ࡭ࡧ࡮ࡥ࡮ࡨࡷࠥࡧ࡬࡭ࠢࡨࡶࡷࡵࡲࡴࠢࡪࡶࡦࡩࡥࡧࡷ࡯ࡰࡾࠦࡢࡺࠢ࡯ࡳ࡬࡭ࡩ࡯ࡩࠍࠤࠥࠦࠠࡵࡪࡨࡱࠥࡧ࡮ࡥࠢࡶ࡭ࡲࡶ࡬ࡺࠢࡵࡩࡹࡻࡲ࡯࡫ࡱ࡫ࠥࡽࡩࡵࡪࡲࡹࡹࠦࡴࡩࡴࡲࡻ࡮ࡴࡧࠡࡧࡻࡧࡪࡶࡴࡪࡱࡱࡷ࠳ࠐࠠࠡࠢࠣࠦࠧࠨᘼ")
    @staticmethod
    def upload_attachment(bstack11lll1l11ll_opy_: str, *bstack11lll1l1l11_opy_) -> None:
        if not bstack11lll1l11ll_opy_ or not bstack11lll1l11ll_opy_.strip():
            logger.error(bstack11l111_opy_ (u"ࠤࡤࡨࡩࡥࡡࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࠣࡪࡦ࡯࡬ࡦࡦ࠽ࠤࡕࡸ࡯ࡷ࡫ࡧࡩࡩࠦࡦࡪ࡮ࡨࠤࡵࡧࡴࡩࠢ࡬ࡷࠥ࡫࡭ࡱࡶࡼࠤࡴࡸࠠࡏࡱࡱࡩ࠳ࠨᘽ"))
            return
        bstack11lll111l1l_opy_ = bstack11lll1l1l11_opy_[0] if bstack11lll1l1l11_opy_ and len(bstack11lll1l1l11_opy_) > 0 else None
        bstack11lll1l1l1l_opy_ = None
        test_framework_state, test_hook_state = bstack11lll11l11l_opy_()
        try:
            if bstack11lll1l11ll_opy_.startswith(bstack11l111_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻࠱࠲ࠦᘾ")) or bstack11lll1l11ll_opy_.startswith(bstack11l111_opy_ (u"ࠦ࡭ࡺࡴࡱࡵ࠽࠳࠴ࠨᘿ")):
                logger.debug(bstack11l111_opy_ (u"ࠧࡖࡡࡵࡪࠣ࡭ࡸࠦࡩࡥࡧࡱࡸ࡮࡬ࡩࡦࡦࠣࡥࡸࠦࡕࡓࡎ࠾ࠤࡩࡵࡷ࡯࡮ࡲࡥࡩ࡯࡮ࡨࠢࡷ࡬ࡪࠦࡦࡪ࡮ࡨ࠲ࠧᙀ"))
                url = bstack11lll1l11ll_opy_
                bstack11lll111lll_opy_ = str(uuid.uuid4())
                bstack11lll11l1l1_opy_ = os.path.basename(urllib.request.urlparse(url).path)
                if not bstack11lll11l1l1_opy_ or not bstack11lll11l1l1_opy_.strip():
                    bstack11lll11l1l1_opy_ = bstack11lll111lll_opy_
                temp_file = tempfile.NamedTemporaryFile(delete=False,
                                                        prefix=bstack11l111_opy_ (u"ࠨࡵࡱ࡮ࡲࡥࡩࡥࠢᙁ") + bstack11lll111lll_opy_ + bstack11l111_opy_ (u"ࠢࡠࠤᙂ"),
                                                        suffix=bstack11l111_opy_ (u"ࠣࡡࠥᙃ") + bstack11lll11l1l1_opy_)
                with urllib.request.urlopen(url) as response, open(temp_file.name, bstack11l111_opy_ (u"ࠩࡺࡦࠬᙄ")) as out_file:
                    shutil.copyfileobj(response, out_file)
                bstack11lll1l1l1l_opy_ = Path(temp_file.name)
                logger.debug(bstack11l111_opy_ (u"ࠥࡈࡴࡽ࡮࡭ࡱࡤࡨࡪࡪࠠࡧ࡫࡯ࡩࠥࡺ࡯ࠡࡶࡨࡱࡵࡵࡲࡢࡴࡼࠤࡱࡵࡣࡢࡶ࡬ࡳࡳࡀࠠࡼࡿࠥᙅ").format(bstack11lll1l1l1l_opy_))
            else:
                bstack11lll1l1l1l_opy_ = Path(bstack11lll1l11ll_opy_)
                logger.debug(bstack11l111_opy_ (u"ࠦࡕࡧࡴࡩࠢ࡬ࡷࠥ࡯ࡤࡦࡰࡷ࡭࡫࡯ࡥࡥࠢࡤࡷࠥࡲ࡯ࡤࡣ࡯ࠤ࡫࡯࡬ࡦ࠼ࠣࡿࢂࠨᙆ").format(bstack11lll1l1l1l_opy_))
        except Exception as e:
            logger.error(bstack11l111_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡱࡥࡸࡦ࡯࡮ࠡࡨ࡬ࡰࡪࠦࡦࡳࡱࡰࠤࡵࡧࡴࡩ࠱ࡘࡖࡑࡀࠠࡼࡿࠥᙇ").format(e))
            return
        if bstack11lll1l1l1l_opy_ is None or not bstack11lll1l1l1l_opy_.exists():
            logger.error(bstack11l111_opy_ (u"ࠨࡓࡰࡷࡵࡧࡪࠦࡦࡪ࡮ࡨࠤࡩࡵࡥࡴࠢࡱࡳࡹࠦࡥࡹ࡫ࡶࡸ࠿ࠦࡻࡾࠤᙈ").format(bstack11lll1l1l1l_opy_))
            return
        if bstack11lll1l1l1l_opy_.stat().st_size > bstack11lll1l1111_opy_:
            logger.error(bstack11l111_opy_ (u"ࠢࡇ࡫࡯ࡩࠥࡹࡩࡻࡧࠣࡩࡽࡩࡥࡦࡦࡶࠤࡲࡧࡸࡪ࡯ࡸࡱࠥࡧ࡬࡭ࡱࡺࡩࡩࠦࡳࡪࡼࡨࠤࡴ࡬ࠠࡼࡿࠥᙉ").format(bstack11lll1l1111_opy_))
            return
        bstack11lll11lll1_opy_ = bstack11l111_opy_ (u"ࠣࡖࡨࡷࡹࡒࡥࡷࡧ࡯ࠦᙊ")
        if bstack11lll111l1l_opy_:
            try:
                params = json.loads(bstack11lll111l1l_opy_)
                if bstack11l111_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡂࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࠦᙋ") in params and params.get(bstack11l111_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡃࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࠧᙌ")) is True:
                    bstack11lll11lll1_opy_ = bstack11l111_opy_ (u"ࠦࡇࡻࡩ࡭ࡦࡏࡩࡻ࡫࡬ࠣᙍ")
            except Exception as bstack11lll11ll1l_opy_:
                logger.error(bstack11l111_opy_ (u"ࠧࡐࡓࡐࡐࠣࡴࡦࡸࡳࡪࡰࡪࠤࡪࡸࡲࡰࡴࠣ࡭ࡳࠦࡡࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࡓࡥࡷࡧ࡭ࡴ࠼ࠣࡿࢂࠨᙎ").format(bstack11lll11ll1l_opy_))
        bstack11lll11l1ll_opy_ = False
        from browserstack_sdk.sdk_cli.bstack1l1l1l11ll1_opy_ import bstack1l11lll11ll_opy_
        if test_framework_state in bstack1l11lll11ll_opy_.bstack1l1lll1lll1_opy_:
            if bstack11lll11lll1_opy_ == bstack11llll111ll_opy_:
                bstack11lll11l1ll_opy_ = True
            bstack11lll11lll1_opy_ = bstack11llll1111l_opy_
        try:
            platform_index = os.environ[bstack11l111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭ᙏ")]
            target_dir = os.path.join(bstack1ll1l1l1l1l_opy_, bstack1ll111ll111_opy_ + str(platform_index),
                                      bstack11lll11lll1_opy_)
            if bstack11lll11l1ll_opy_:
                target_dir = os.path.join(target_dir, bstack11lll1l111l_opy_)
            os.makedirs(target_dir, exist_ok=True)
            logger.debug(bstack11l111_opy_ (u"ࠢࡄࡴࡨࡥࡹ࡫ࡤ࠰ࡸࡨࡶ࡮࡬ࡩࡦࡦࠣࡸࡦࡸࡧࡦࡶࠣࡨ࡮ࡸࡥࡤࡶࡲࡶࡾࡀࠠࡼࡿࠥᙐ").format(target_dir))
            file_name = os.path.basename(bstack11lll1l1l1l_opy_)
            bstack11lll1l11l1_opy_ = os.path.join(target_dir, file_name)
            if os.path.exists(bstack11lll1l11l1_opy_):
                base_name, extension = os.path.splitext(file_name)
                bstack11lll11ll11_opy_ = 1
                while os.path.exists(os.path.join(target_dir, base_name + str(bstack11lll11ll11_opy_) + extension)):
                    bstack11lll11ll11_opy_ += 1
                bstack11lll1l11l1_opy_ = os.path.join(target_dir, base_name + str(bstack11lll11ll11_opy_) + extension)
            shutil.copy(bstack11lll1l1l1l_opy_, bstack11lll1l11l1_opy_)
            logger.info(bstack11l111_opy_ (u"ࠣࡈ࡬ࡰࡪࠦࡳࡶࡥࡦࡩࡸࡹࡦࡶ࡮࡯ࡽࠥࡩ࡯ࡱ࡫ࡨࡨࠥࡺ࡯࠻ࠢࡾࢁࠧᙑ").format(bstack11lll1l11l1_opy_))
        except Exception as e:
            logger.error(bstack11l111_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡ࡯ࡲࡺ࡮ࡴࡧࠡࡨ࡬ࡰࡪࠦࡴࡰࠢࡷࡥࡷ࡭ࡥࡵࠢࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽ࠿ࠦࡻࡾࠤᙒ").format(e))
            return
        finally:
            if bstack11lll1l11ll_opy_.startswith(bstack11l111_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻࠱࠲ࠦᙓ")) or bstack11lll1l11ll_opy_.startswith(bstack11l111_opy_ (u"ࠦ࡭ࡺࡴࡱࡵ࠽࠳࠴ࠨᙔ")):
                try:
                    if bstack11lll1l1l1l_opy_ is not None and bstack11lll1l1l1l_opy_.exists():
                        bstack11lll1l1l1l_opy_.unlink()
                        logger.debug(bstack11l111_opy_ (u"࡚ࠧࡥ࡮ࡲࡲࡶࡦࡸࡹࠡࡨ࡬ࡰࡪࠦࡤࡦ࡮ࡨࡸࡪࡪ࠺ࠡࡽࢀࠦᙕ").format(bstack11lll1l1l1l_opy_))
                except Exception as ex:
                    logger.error(bstack11l111_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡪࡥ࡭ࡧࡷ࡭ࡳ࡭ࠠࡵࡧࡰࡴࡴࡸࡡࡳࡻࠣࡪ࡮ࡲࡥ࠻ࠢࡾࢁࠧᙖ").format(ex))
    @staticmethod
    def bstack1111llll1l_opy_() -> None:
        bstack11l111_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤࡉ࡫࡬ࡦࡶࡨࡷࠥࡧ࡬࡭ࠢࡩࡳࡱࡪࡥࡳࡵࠣࡻ࡭ࡵࡳࡦࠢࡱࡥࡲ࡫ࡳࠡࡵࡷࡥࡷࡺࠠࡸ࡫ࡷ࡬ࠥࠨࡕࡱ࡮ࡲࡥࡩ࡫ࡤࡂࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࡷ࠲ࠨࠠࡧࡱ࡯ࡰࡴࡽࡥࡥࠢࡥࡽࠥࡧࠠ࡯ࡷࡰࡦࡪࡸࠠࡪࡰࠍࠤࠥࠦࠠࠡࠢࠣࠤࡹ࡮ࡥࠡࡷࡶࡩࡷ࠭ࡳࠡࢀ࠲࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠣࡨ࡮ࡸࡥࡤࡶࡲࡶࡾ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦᙗ")
        bstack11lll11llll_opy_ = bstack1ll1l1ll111_opy_()
        pattern = re.compile(bstack11l111_opy_ (u"ࡳࠤࡘࡴࡱࡵࡡࡥࡧࡧࡅࡹࡺࡡࡤࡪࡰࡩࡳࡺࡳ࠮࡞ࡧ࠯ࠧᙘ"))
        if os.path.exists(bstack11lll11llll_opy_):
            for item in os.listdir(bstack11lll11llll_opy_):
                bstack11lll11l111_opy_ = os.path.join(bstack11lll11llll_opy_, item)
                if os.path.isdir(bstack11lll11l111_opy_) and pattern.fullmatch(item):
                    try:
                        shutil.rmtree(bstack11lll11l111_opy_)
                    except Exception as e:
                        logger.error(bstack11l111_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡦࡨࡰࡪࡺࡩ࡯ࡩࠣࡨ࡮ࡸࡥࡤࡶࡲࡶࡾࡀࠠࡼࡿࠥᙙ").format(e))
        else:
            logger.info(bstack11l111_opy_ (u"ࠥࡘ࡭࡫ࠠࡥ࡫ࡵࡩࡨࡺ࡯ࡳࡻࠣࡨࡴ࡫ࡳࠡࡰࡲࡸࠥ࡫ࡸࡪࡵࡷ࠾ࠥࢁࡽࠣᙚ").format(bstack11lll11llll_opy_))