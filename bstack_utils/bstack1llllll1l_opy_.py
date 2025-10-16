# coding: UTF-8
import sys
bstack11llll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1l1l1l1_opy_ = 7
def bstack1ll11_opy_ (bstack11l11ll_opy_):
    global bstack11l1lll_opy_
    bstack1l1l111_opy_ = ord (bstack11l11ll_opy_ [-1])
    bstack11_opy_ = bstack11l11ll_opy_ [:-1]
    bstack1l1llll_opy_ = bstack1l1l111_opy_ % len (bstack11_opy_)
    bstack11111_opy_ = bstack11_opy_ [:bstack1l1llll_opy_] + bstack11_opy_ [bstack1l1llll_opy_:]
    if bstack11llll1_opy_:
        bstack111_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    else:
        bstack111_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    return eval (bstack111_opy_)
import os
from bstack_utils.constants import *
from browserstack_sdk.sdk_cli.cli import cli
from bstack_utils.bstack11ll1ll1l11_opy_ import bstack11ll1ll1lll_opy_
from bstack_utils.bstack1lll1ll1l_opy_ import bstack11l11l1l_opy_
from bstack_utils.helper import bstack1llll1lll1_opy_
import json
class bstack1llll1l1l_opy_:
    _1ll1ll1l1l1_opy_ = None
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.bstack1111l11l11l_opy_ = bstack11ll1ll1lll_opy_(self.config, logger)
        self.bstack1lll1ll1l_opy_ = bstack11l11l1l_opy_.bstack1llll11l1_opy_(config=self.config)
        self.bstack1111l11l1ll_opy_ = {}
        self.bstack1111l1ll_opy_ = False
        self.bstack1111l11l111_opy_ = (
            self.__1111l111l11_opy_()
            and self.bstack1lll1ll1l_opy_ is not None
            and self.bstack1lll1ll1l_opy_.bstack1lllll111_opy_()
            and config.get(bstack1ll11_opy_ (u"ࠫࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠩẈ"), None) is not None
            and config.get(bstack1ll11_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨẉ"), os.path.basename(os.getcwd())) is not None
        )
    @classmethod
    def bstack1llll11l1_opy_(cls, config, logger):
        if cls._1ll1ll1l1l1_opy_ is None and config is not None:
            cls._1ll1ll1l1l1_opy_ = bstack1llll1l1l_opy_(config, logger)
        return cls._1ll1ll1l1l1_opy_
    def bstack1lllll111_opy_(self):
        bstack1ll11_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࡈࡴࠦ࡮ࡰࡶࠣࡥࡵࡶ࡬ࡺࠢࡷࡩࡸࡺࠠࡰࡴࡧࡩࡷ࡯࡮ࡨࠢࡺ࡬ࡪࡴ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࠲ࠦࡏ࠲࠳ࡼࠤ࡮ࡹࠠ࡯ࡱࡷࠤࡪࡴࡡࡣ࡮ࡨࡨࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡ࠯ࠣࡓࡷࡪࡥࡳ࡫ࡱ࡫ࠥ࡯ࡳࠡࡰࡲࡸࠥ࡫࡮ࡢࡤ࡯ࡩࡩࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࠰ࠤࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠢ࡬ࡷࠥࡔ࡯࡯ࡧࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠭ࠡࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠤ࡮ࡹࠠࡏࡱࡱࡩࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤẊ")
        return self.bstack1111l11l111_opy_ and self.bstack1111l111lll_opy_()
    def bstack1111l111lll_opy_(self):
        bstack1111l11ll1l_opy_ = os.getenv(bstack1ll11_opy_ (u"ࠧࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࡢ࡙ࡘࡋࡄࠨẋ"), self.config.get(bstack1ll11_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫẌ"), None))
        return bstack1111l11ll1l_opy_ in bstack11l1l11l1l1_opy_
    def __1111l111l11_opy_(self):
        bstack11ll1l11lll_opy_ = False
        for fw in bstack11l1l1l111l_opy_:
            if fw in self.config.get(bstack1ll11_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬẍ"), bstack1ll11_opy_ (u"ࠪࠫẎ")):
                bstack11ll1l11lll_opy_ = True
        return bstack1llll1lll1_opy_(self.config.get(bstack1ll11_opy_ (u"ࠫࡹ࡫ࡳࡵࡑࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨẏ"), bstack11ll1l11lll_opy_))
    def bstack1111l11ll11_opy_(self):
        return (not self.bstack1lllll111_opy_() and
                self.bstack1lll1ll1l_opy_ is not None and self.bstack1lll1ll1l_opy_.bstack1lllll111_opy_())
    def bstack1111l111l1l_opy_(self):
        if not self.bstack1111l11ll11_opy_():
            return
        if self.config.get(bstack1ll11_opy_ (u"ࠬࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࠪẐ"), None) is None or self.config.get(bstack1ll11_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩẑ"), os.path.basename(os.getcwd())) is None:
            self.logger.info(bstack1ll11_opy_ (u"ࠢࡕࡧࡶࡸࠥࡘࡥࡰࡴࡧࡩࡷ࡯࡮ࡨࠢࡦࡥࡳ࠭ࡴࠡࡹࡲࡶࡰࠦࡡࡴࠢࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠥࡵࡲࠡࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪࠦࡩࡴࠢࡱࡹࡱࡲ࠮ࠡࡒ࡯ࡩࡦࡹࡥࠡࡵࡨࡸࠥࡧࠠ࡯ࡱࡱ࠱ࡳࡻ࡬࡭ࠢࡹࡥࡱࡻࡥ࠯ࠤẒ"))
        if not self.__1111l111l11_opy_():
            self.logger.info(bstack1ll11_opy_ (u"ࠣࡖࡨࡷࡹࠦࡒࡦࡱࡵࡨࡪࡸࡩ࡯ࡩࠣࡧࡦࡴࠧࡵࠢࡺࡳࡷࡱࠠࡢࡵࠣࡸࡪࡹࡴࡓࡧࡳࡳࡷࡺࡩ࡯ࡩࠣ࡭ࡸࠦࡤࡪࡵࡤࡦࡱ࡫ࡤ࠯ࠢࡓࡰࡪࡧࡳࡦࠢࡨࡲࡦࡨ࡬ࡦࠢ࡬ࡸࠥ࡬ࡲࡰ࡯ࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡼࡱࡱࠦࡦࡪ࡮ࡨ࠲ࠧẓ"))
    def bstack1111l11l1l1_opy_(self):
        return self.bstack1111l1ll_opy_
    def bstack11l1l111_opy_(self, bstack1111l111ll1_opy_):
        self.bstack1111l1ll_opy_ = bstack1111l111ll1_opy_
        self.bstack1llll11ll_opy_(bstack1ll11_opy_ (u"ࠤࡤࡴࡵࡲࡩࡦࡦࠥẔ"), bstack1111l111ll1_opy_)
    def bstack11111l11_opy_(self, test_files):
        try:
            if test_files is None:
                self.logger.debug(bstack1ll11_opy_ (u"ࠥ࡟ࡷ࡫࡯ࡳࡦࡨࡶࡤࡺࡥࡴࡶࡢࡪ࡮ࡲࡥࡴ࡟ࠣࡒࡴࠦࡴࡦࡵࡷࠤ࡫࡯࡬ࡦࡵࠣࡴࡷࡵࡶࡪࡦࡨࡨࠥ࡬࡯ࡳࠢࡲࡶࡩ࡫ࡲࡪࡰࡪ࠲ࠧẕ"))
                return None
            orchestration_strategy = None
            orchestration_metadata = self.bstack1lll1ll1l_opy_.bstack111llll11l1_opy_()
            if self.bstack1lll1ll1l_opy_ is not None:
                orchestration_strategy = self.bstack1lll1ll1l_opy_.bstack11lll11ll1_opy_()
            if orchestration_strategy is None:
                self.logger.error(bstack1ll11_opy_ (u"ࠦࡔࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࠤࡸࡺࡲࡢࡶࡨ࡫ࡾࠦࡩࡴࠢࡑࡳࡳ࡫࠮ࠡࡅࡤࡲࡳࡵࡴࠡࡲࡵࡳࡨ࡫ࡥࡥࠢࡺ࡭ࡹ࡮ࠠࡵࡧࡶࡸࠥࡵࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࠥࡹࡥࡴࡵ࡬ࡳࡳ࠴ࠢẖ"))
                return None
            self.logger.info(bstack1ll11_opy_ (u"ࠧࡘࡥࡰࡴࡧࡩࡷ࡯࡮ࡨࠢࡷࡩࡸࡺࠠࡧ࡫࡯ࡩࡸࠦࡷࡪࡶ࡫ࠤࡴࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࠤࡸࡺࡲࡢࡶࡨ࡫ࡾࡀࠠࡼࡿࠥẗ").format(orchestration_strategy))
            if cli.is_running():
                self.logger.debug(bstack1ll11_opy_ (u"ࠨࡕࡴ࡫ࡱ࡫ࠥࡉࡌࡊࠢࡩࡰࡴࡽࠠࡧࡱࡵࠤࡹ࡫ࡳࡵࠢࡩ࡭ࡱ࡫ࡳࠡࡱࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮࠯ࠤẘ"))
                ordered_test_files = cli.test_orchestration_session(test_files, orchestration_strategy, json.dumps(orchestration_metadata))
            else:
                self.logger.debug(bstack1ll11_opy_ (u"ࠢࡖࡵ࡬ࡲ࡬ࠦࡳࡥ࡭ࠣࡪࡱࡵࡷࠡࡨࡲࡶࠥࡺࡥࡴࡶࠣࡪ࡮ࡲࡥࡴࠢࡲࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯࠰ࠥẙ"))
                self.bstack1111l11l11l_opy_.bstack11lll111111_opy_(test_files, orchestration_strategy, orchestration_metadata)
                ordered_test_files = self.bstack1111l11l11l_opy_.bstack11lll11ll1l_opy_()
            if not ordered_test_files:
                return None
            self.bstack1llll11ll_opy_(bstack1ll11_opy_ (u"ࠣࡷࡳࡰࡴࡧࡤࡦࡦࡗࡩࡸࡺࡆࡪ࡮ࡨࡷࡈࡵࡵ࡯ࡶࠥẚ"), len(test_files))
            self.bstack1llll11ll_opy_(bstack1ll11_opy_ (u"ࠤࡱࡳࡩ࡫ࡉ࡯ࡦࡨࡼࠧẛ"), int(os.environ.get(bstack1ll11_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡑࡓࡉࡋ࡟ࡊࡐࡇࡉ࡝ࠨẜ")) or bstack1ll11_opy_ (u"ࠦ࠵ࠨẝ")))
            self.bstack1llll11ll_opy_(bstack1ll11_opy_ (u"ࠧࡺ࡯ࡵࡣ࡯ࡒࡴࡪࡥࡴࠤẞ"), int(os.environ.get(bstack1ll11_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡔࡏࡅࡇࡢࡇࡔ࡛ࡎࡕࠤẟ")) or bstack1ll11_opy_ (u"ࠢ࠲ࠤẠ")))
            self.bstack1llll11ll_opy_(bstack1ll11_opy_ (u"ࠣࡦࡲࡻࡳࡲ࡯ࡢࡦࡨࡨ࡙࡫ࡳࡵࡈ࡬ࡰࡪࡹࡃࡰࡷࡱࡸࠧạ"), len(ordered_test_files))
            self.bstack1llll11ll_opy_(bstack1ll11_opy_ (u"ࠤࡶࡴࡱ࡯ࡴࡕࡧࡶࡸࡸࡇࡐࡊࡅࡤࡰࡱࡉ࡯ࡶࡰࡷࠦẢ"), self.bstack1111l11l11l_opy_.bstack11ll1lll1l1_opy_())
            return ordered_test_files
        except Exception as e:
            self.logger.debug(bstack1ll11_opy_ (u"ࠥ࡟ࡷ࡫࡯ࡳࡦࡨࡶࡤࡺࡥࡴࡶࡢࡪ࡮ࡲࡥࡴ࡟ࠣࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡵࡲࡥࡧࡵ࡭ࡳ࡭ࠠࡵࡧࡶࡸࠥࡩ࡬ࡢࡵࡶࡩࡸࡀࠠࡼࡿࠥả").format(e))
        return None
    def bstack1llll11ll_opy_(self, key, value):
        self.bstack1111l11l1ll_opy_[key] = value
    def bstack1l1111lll1_opy_(self):
        return self.bstack1111l11l1ll_opy_