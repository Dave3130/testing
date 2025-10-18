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
from bstack_utils.constants import *
from browserstack_sdk.sdk_cli.cli import cli
from bstack_utils.bstack11ll1ll1ll1_opy_ import bstack11lll1111ll_opy_
from bstack_utils.bstack1111ll1l_opy_ import bstack1lll1l1ll_opy_
from bstack_utils.helper import bstack1l1lll1ll1_opy_
import json
class bstack11111lll_opy_:
    _1ll1ll111ll_opy_ = None
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.bstack11111llll1l_opy_ = bstack11lll1111ll_opy_(self.config, logger)
        self.bstack1111ll1l_opy_ = bstack1lll1l1ll_opy_.bstack111l11l1_opy_(config=self.config)
        self.bstack1111l111111_opy_ = {}
        self.bstack1llllll1l_opy_ = False
        self.bstack1111l1111l1_opy_ = (
            self.__11111llll11_opy_()
            and self.bstack1111ll1l_opy_ is not None
            and self.bstack1111ll1l_opy_.bstack1llllll11_opy_()
            and config.get(bstack11l111_opy_ (u"ࠫࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠩẫ"), None) is not None
            and config.get(bstack11l111_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨẬ"), os.path.basename(os.getcwd())) is not None
        )
    @classmethod
    def bstack111l11l1_opy_(cls, config, logger):
        if cls._1ll1ll111ll_opy_ is None and config is not None:
            cls._1ll1ll111ll_opy_ = bstack11111lll_opy_(config, logger)
        return cls._1ll1ll111ll_opy_
    def bstack1llllll11_opy_(self):
        bstack11l111_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࡈࡴࠦ࡮ࡰࡶࠣࡥࡵࡶ࡬ࡺࠢࡷࡩࡸࡺࠠࡰࡴࡧࡩࡷ࡯࡮ࡨࠢࡺ࡬ࡪࡴ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࠲ࠦࡏ࠲࠳ࡼࠤ࡮ࡹࠠ࡯ࡱࡷࠤࡪࡴࡡࡣ࡮ࡨࡨࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡ࠯ࠣࡓࡷࡪࡥࡳ࡫ࡱ࡫ࠥ࡯ࡳࠡࡰࡲࡸࠥ࡫࡮ࡢࡤ࡯ࡩࡩࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࠰ࠤࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠢ࡬ࡷࠥࡔ࡯࡯ࡧࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠭ࠡࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠤ࡮ࡹࠠࡏࡱࡱࡩࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤậ")
        return self.bstack1111l1111l1_opy_ and self.bstack11111lll1ll_opy_()
    def bstack11111lll1ll_opy_(self):
        bstack11111llllll_opy_ = os.getenv(bstack11l111_opy_ (u"ࠧࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࡢ࡙ࡘࡋࡄࠨẮ"), self.config.get(bstack11l111_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫắ"), None))
        return bstack11111llllll_opy_ in bstack11l11llll1l_opy_
    def __11111llll11_opy_(self):
        bstack11ll11lll11_opy_ = False
        for fw in bstack11l11ll1lll_opy_:
            if fw in self.config.get(bstack11l111_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬẰ"), bstack11l111_opy_ (u"ࠪࠫằ")):
                bstack11ll11lll11_opy_ = True
        return bstack1l1lll1ll1_opy_(self.config.get(bstack11l111_opy_ (u"ࠫࡹ࡫ࡳࡵࡑࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨẲ"), bstack11ll11lll11_opy_))
    def bstack1111l11111l_opy_(self):
        return (not self.bstack1llllll11_opy_() and
                self.bstack1111ll1l_opy_ is not None and self.bstack1111ll1l_opy_.bstack1llllll11_opy_())
    def bstack11111lll1l1_opy_(self):
        if not self.bstack1111l11111l_opy_():
            return
        if self.config.get(bstack11l111_opy_ (u"ࠬࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࠪẳ"), None) is None or self.config.get(bstack11l111_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩẴ"), os.path.basename(os.getcwd())) is None:
            self.logger.info(bstack11l111_opy_ (u"ࠢࡕࡧࡶࡸࠥࡘࡥࡰࡴࡧࡩࡷ࡯࡮ࡨࠢࡦࡥࡳ࠭ࡴࠡࡹࡲࡶࡰࠦࡡࡴࠢࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠥࡵࡲࠡࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪࠦࡩࡴࠢࡱࡹࡱࡲ࠮ࠡࡒ࡯ࡩࡦࡹࡥࠡࡵࡨࡸࠥࡧࠠ࡯ࡱࡱ࠱ࡳࡻ࡬࡭ࠢࡹࡥࡱࡻࡥ࠯ࠤẵ"))
        if not self.__11111llll11_opy_():
            self.logger.info(bstack11l111_opy_ (u"ࠣࡖࡨࡷࡹࠦࡒࡦࡱࡵࡨࡪࡸࡩ࡯ࡩࠣࡧࡦࡴࠧࡵࠢࡺࡳࡷࡱࠠࡢࡵࠣࡸࡪࡹࡴࡓࡧࡳࡳࡷࡺࡩ࡯ࡩࠣ࡭ࡸࠦࡤࡪࡵࡤࡦࡱ࡫ࡤ࠯ࠢࡓࡰࡪࡧࡳࡦࠢࡨࡲࡦࡨ࡬ࡦࠢ࡬ࡸࠥ࡬ࡲࡰ࡯ࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡼࡱࡱࠦࡦࡪ࡮ࡨ࠲ࠧẶ"))
    def bstack11111lllll1_opy_(self):
        return self.bstack1llllll1l_opy_
    def bstack111ll1ll_opy_(self, bstack11111lll11l_opy_):
        self.bstack1llllll1l_opy_ = bstack11111lll11l_opy_
        self.bstack11111l1l_opy_(bstack11l111_opy_ (u"ࠤࡤࡴࡵࡲࡩࡦࡦࠥặ"), bstack11111lll11l_opy_)
    def bstack1lll1l11l_opy_(self, test_files):
        try:
            if test_files is None:
                self.logger.debug(bstack11l111_opy_ (u"ࠥ࡟ࡷ࡫࡯ࡳࡦࡨࡶࡤࡺࡥࡴࡶࡢࡪ࡮ࡲࡥࡴ࡟ࠣࡒࡴࠦࡴࡦࡵࡷࠤ࡫࡯࡬ࡦࡵࠣࡴࡷࡵࡶࡪࡦࡨࡨࠥ࡬࡯ࡳࠢࡲࡶࡩ࡫ࡲࡪࡰࡪ࠲ࠧẸ"))
                return None
            orchestration_strategy = None
            orchestration_metadata = self.bstack1111ll1l_opy_.bstack11l1111l11l_opy_()
            if self.bstack1111ll1l_opy_ is not None:
                orchestration_strategy = self.bstack1111ll1l_opy_.bstack11ll1l11ll_opy_()
            if orchestration_strategy is None:
                self.logger.error(bstack11l111_opy_ (u"ࠦࡔࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࠤࡸࡺࡲࡢࡶࡨ࡫ࡾࠦࡩࡴࠢࡑࡳࡳ࡫࠮ࠡࡅࡤࡲࡳࡵࡴࠡࡲࡵࡳࡨ࡫ࡥࡥࠢࡺ࡭ࡹ࡮ࠠࡵࡧࡶࡸࠥࡵࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࠥࡹࡥࡴࡵ࡬ࡳࡳ࠴ࠢẹ"))
                return None
            self.logger.info(bstack11l111_opy_ (u"ࠧࡘࡥࡰࡴࡧࡩࡷ࡯࡮ࡨࠢࡷࡩࡸࡺࠠࡧ࡫࡯ࡩࡸࠦࡷࡪࡶ࡫ࠤࡴࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࠤࡸࡺࡲࡢࡶࡨ࡫ࡾࡀࠠࡼࡿࠥẺ").format(orchestration_strategy))
            if cli.is_running():
                self.logger.debug(bstack11l111_opy_ (u"ࠨࡕࡴ࡫ࡱ࡫ࠥࡉࡌࡊࠢࡩࡰࡴࡽࠠࡧࡱࡵࠤࡹ࡫ࡳࡵࠢࡩ࡭ࡱ࡫ࡳࠡࡱࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮࠯ࠤẻ"))
                ordered_test_files = cli.test_orchestration_session(test_files, orchestration_strategy, json.dumps(orchestration_metadata))
            else:
                self.logger.debug(bstack11l111_opy_ (u"ࠢࡖࡵ࡬ࡲ࡬ࠦࡳࡥ࡭ࠣࡪࡱࡵࡷࠡࡨࡲࡶࠥࡺࡥࡴࡶࠣࡪ࡮ࡲࡥࡴࠢࡲࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯࠰ࠥẼ"))
                self.bstack11111llll1l_opy_.bstack11ll1lll1ll_opy_(test_files, orchestration_strategy, orchestration_metadata)
                ordered_test_files = self.bstack11111llll1l_opy_.bstack11lll11111l_opy_()
            if not ordered_test_files:
                return None
            self.bstack11111l1l_opy_(bstack11l111_opy_ (u"ࠣࡷࡳࡰࡴࡧࡤࡦࡦࡗࡩࡸࡺࡆࡪ࡮ࡨࡷࡈࡵࡵ࡯ࡶࠥẽ"), len(test_files))
            self.bstack11111l1l_opy_(bstack11l111_opy_ (u"ࠤࡱࡳࡩ࡫ࡉ࡯ࡦࡨࡼࠧẾ"), int(os.environ.get(bstack11l111_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡑࡓࡉࡋ࡟ࡊࡐࡇࡉ࡝ࠨế")) or bstack11l111_opy_ (u"ࠦ࠵ࠨỀ")))
            self.bstack11111l1l_opy_(bstack11l111_opy_ (u"ࠧࡺ࡯ࡵࡣ࡯ࡒࡴࡪࡥࡴࠤề"), int(os.environ.get(bstack11l111_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡔࡏࡅࡇࡢࡇࡔ࡛ࡎࡕࠤỂ")) or bstack11l111_opy_ (u"ࠢ࠲ࠤể")))
            self.bstack11111l1l_opy_(bstack11l111_opy_ (u"ࠣࡦࡲࡻࡳࡲ࡯ࡢࡦࡨࡨ࡙࡫ࡳࡵࡈ࡬ࡰࡪࡹࡃࡰࡷࡱࡸࠧỄ"), len(ordered_test_files))
            self.bstack11111l1l_opy_(bstack11l111_opy_ (u"ࠤࡶࡴࡱ࡯ࡴࡕࡧࡶࡸࡸࡇࡐࡊࡅࡤࡰࡱࡉ࡯ࡶࡰࡷࠦễ"), self.bstack11111llll1l_opy_.bstack11ll1lll111_opy_())
            return ordered_test_files
        except Exception as e:
            self.logger.debug(bstack11l111_opy_ (u"ࠥ࡟ࡷ࡫࡯ࡳࡦࡨࡶࡤࡺࡥࡴࡶࡢࡪ࡮ࡲࡥࡴ࡟ࠣࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡵࡲࡥࡧࡵ࡭ࡳ࡭ࠠࡵࡧࡶࡸࠥࡩ࡬ࡢࡵࡶࡩࡸࡀࠠࡼࡿࠥỆ").format(e))
        return None
    def bstack11111l1l_opy_(self, key, value):
        self.bstack1111l111111_opy_[key] = value
    def bstack1111lll1ll_opy_(self):
        return self.bstack1111l111111_opy_