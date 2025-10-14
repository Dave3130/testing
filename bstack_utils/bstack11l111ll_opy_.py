# coding: UTF-8
import sys
bstack1_opy_ = sys.version_info [0] == 2
bstack11l1ll1_opy_ = 2048
bstack1l1l1ll_opy_ = 7
def bstack11l1l11_opy_ (bstack111l1ll_opy_):
    global bstack1l1lll1_opy_
    bstack1l1l11_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack111l1l1_opy_ = bstack111l1ll_opy_ [:-1]
    bstack111ll_opy_ = bstack1l1l11_opy_ % len (bstack111l1l1_opy_)
    bstack11l11l1_opy_ = bstack111l1l1_opy_ [:bstack111ll_opy_] + bstack111l1l1_opy_ [bstack111ll_opy_:]
    if bstack1_opy_:
        bstack1111l1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    else:
        bstack1111l1l_opy_ = str () .join ([chr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    return eval (bstack1111l1l_opy_)
import os
from bstack_utils.constants import *
from browserstack_sdk.sdk_cli.cli import cli
from bstack_utils.bstack11lll11ll11_opy_ import bstack11lll111lll_opy_
from bstack_utils.bstack1llll11l1_opy_ import bstack11l1l111_opy_
from bstack_utils.helper import bstack1lll1ll1l1_opy_
import json
class bstack1lll1ll1l_opy_:
    _1ll1ll1l111_opy_ = None
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.bstack1111l111l11_opy_ = bstack11lll111lll_opy_(self.config, logger)
        self.bstack1llll11l1_opy_ = bstack11l1l111_opy_.bstack1111lll1_opy_(config=self.config)
        self.bstack1111l11ll11_opy_ = {}
        self.bstack11l111l1_opy_ = False
        self.bstack1111l1111ll_opy_ = (
            self.__1111l111ll1_opy_()
            and self.bstack1llll11l1_opy_ is not None
            and self.bstack1llll11l1_opy_.bstack1lllll11l_opy_()
            and config.get(bstack11l1l11_opy_ (u"ࠫࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠩẁ"), None) is not None
            and config.get(bstack11l1l11_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨẂ"), os.path.basename(os.getcwd())) is not None
        )
    @classmethod
    def bstack1111lll1_opy_(cls, config, logger):
        if cls._1ll1ll1l111_opy_ is None and config is not None:
            cls._1ll1ll1l111_opy_ = bstack1lll1ll1l_opy_(config, logger)
        return cls._1ll1ll1l111_opy_
    def bstack1lllll11l_opy_(self):
        bstack11l1l11_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࡈࡴࠦ࡮ࡰࡶࠣࡥࡵࡶ࡬ࡺࠢࡷࡩࡸࡺࠠࡰࡴࡧࡩࡷ࡯࡮ࡨࠢࡺ࡬ࡪࡴ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࠲ࠦࡏ࠲࠳ࡼࠤ࡮ࡹࠠ࡯ࡱࡷࠤࡪࡴࡡࡣ࡮ࡨࡨࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡ࠯ࠣࡓࡷࡪࡥࡳ࡫ࡱ࡫ࠥ࡯ࡳࠡࡰࡲࡸࠥ࡫࡮ࡢࡤ࡯ࡩࡩࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࠰ࠤࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠢ࡬ࡷࠥࡔ࡯࡯ࡧࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠭ࠡࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠤ࡮ࡹࠠࡏࡱࡱࡩࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤẃ")
        return self.bstack1111l1111ll_opy_ and self.bstack1111l11l1ll_opy_()
    def bstack1111l11l1ll_opy_(self):
        bstack1111l11l111_opy_ = os.getenv(bstack11l1l11_opy_ (u"ࠧࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࡢ࡙ࡘࡋࡄࠨẄ"), self.config.get(bstack11l1l11_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫẅ"), None))
        return bstack1111l11l111_opy_ in bstack11l1l1111ll_opy_
    def __1111l111ll1_opy_(self):
        bstack11ll1l11l11_opy_ = False
        for fw in bstack11l1l1ll1ll_opy_:
            if fw in self.config.get(bstack11l1l11_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬẆ"), bstack11l1l11_opy_ (u"ࠪࠫẇ")):
                bstack11ll1l11l11_opy_ = True
        return bstack1lll1ll1l1_opy_(self.config.get(bstack11l1l11_opy_ (u"ࠫࡹ࡫ࡳࡵࡑࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨẈ"), bstack11ll1l11l11_opy_))
    def bstack1111l111lll_opy_(self):
        return (not self.bstack1lllll11l_opy_() and
                self.bstack1llll11l1_opy_ is not None and self.bstack1llll11l1_opy_.bstack1lllll11l_opy_())
    def bstack1111l11l11l_opy_(self):
        if not self.bstack1111l111lll_opy_():
            return
        if self.config.get(bstack11l1l11_opy_ (u"ࠬࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࠪẉ"), None) is None or self.config.get(bstack11l1l11_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩẊ"), os.path.basename(os.getcwd())) is None:
            self.logger.info(bstack11l1l11_opy_ (u"ࠢࡕࡧࡶࡸࠥࡘࡥࡰࡴࡧࡩࡷ࡯࡮ࡨࠢࡦࡥࡳ࠭ࡴࠡࡹࡲࡶࡰࠦࡡࡴࠢࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠥࡵࡲࠡࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪࠦࡩࡴࠢࡱࡹࡱࡲ࠮ࠡࡒ࡯ࡩࡦࡹࡥࠡࡵࡨࡸࠥࡧࠠ࡯ࡱࡱ࠱ࡳࡻ࡬࡭ࠢࡹࡥࡱࡻࡥ࠯ࠤẋ"))
        if not self.__1111l111ll1_opy_():
            self.logger.info(bstack11l1l11_opy_ (u"ࠣࡖࡨࡷࡹࠦࡒࡦࡱࡵࡨࡪࡸࡩ࡯ࡩࠣࡧࡦࡴࠧࡵࠢࡺࡳࡷࡱࠠࡢࡵࠣࡸࡪࡹࡴࡓࡧࡳࡳࡷࡺࡩ࡯ࡩࠣ࡭ࡸࠦࡤࡪࡵࡤࡦࡱ࡫ࡤ࠯ࠢࡓࡰࡪࡧࡳࡦࠢࡨࡲࡦࡨ࡬ࡦࠢ࡬ࡸࠥ࡬ࡲࡰ࡯ࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡼࡱࡱࠦࡦࡪ࡮ࡨ࠲ࠧẌ"))
    def bstack1111l111l1l_opy_(self):
        return self.bstack11l111l1_opy_
    def bstack1111l1l1_opy_(self, bstack1111l11l1l1_opy_):
        self.bstack11l111l1_opy_ = bstack1111l11l1l1_opy_
        self.bstack111l11l1_opy_(bstack11l1l11_opy_ (u"ࠤࡤࡴࡵࡲࡩࡦࡦࠥẍ"), bstack1111l11l1l1_opy_)
    def bstack111lllll_opy_(self, test_files):
        try:
            if test_files is None:
                self.logger.debug(bstack11l1l11_opy_ (u"ࠥ࡟ࡷ࡫࡯ࡳࡦࡨࡶࡤࡺࡥࡴࡶࡢࡪ࡮ࡲࡥࡴ࡟ࠣࡒࡴࠦࡴࡦࡵࡷࠤ࡫࡯࡬ࡦࡵࠣࡴࡷࡵࡶࡪࡦࡨࡨࠥ࡬࡯ࡳࠢࡲࡶࡩ࡫ࡲࡪࡰࡪ࠲ࠧẎ"))
                return None
            orchestration_strategy = None
            bstack1l1l1ll1lll_opy_ = self.bstack1llll11l1_opy_.bstack11l11111lll_opy_()
            if self.bstack1llll11l1_opy_ is not None:
                orchestration_strategy = self.bstack1llll11l1_opy_.bstack111l11l1l1_opy_()
            if orchestration_strategy is None:
                self.logger.error(bstack11l1l11_opy_ (u"ࠦࡔࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࠤࡸࡺࡲࡢࡶࡨ࡫ࡾࠦࡩࡴࠢࡑࡳࡳ࡫࠮ࠡࡅࡤࡲࡳࡵࡴࠡࡲࡵࡳࡨ࡫ࡥࡥࠢࡺ࡭ࡹ࡮ࠠࡵࡧࡶࡸࠥࡵࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࠥࡹࡥࡴࡵ࡬ࡳࡳ࠴ࠢẏ"))
                return None
            self.logger.info(bstack11l1l11_opy_ (u"ࠧࡘࡥࡰࡴࡧࡩࡷ࡯࡮ࡨࠢࡷࡩࡸࡺࠠࡧ࡫࡯ࡩࡸࠦࡷࡪࡶ࡫ࠤࡴࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࠤࡸࡺࡲࡢࡶࡨ࡫ࡾࡀࠠࡼࡿࠥẐ").format(orchestration_strategy))
            if cli.is_running():
                self.logger.debug(bstack11l1l11_opy_ (u"ࠨࡕࡴ࡫ࡱ࡫ࠥࡉࡌࡊࠢࡩࡰࡴࡽࠠࡧࡱࡵࠤࡹ࡫ࡳࡵࠢࡩ࡭ࡱ࡫ࡳࠡࡱࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮࠯ࠤẑ"))
                ordered_test_files = cli.test_orchestration_session(test_files, orchestration_strategy, json.dumps(bstack1l1l1ll1lll_opy_))
            else:
                self.logger.debug(bstack11l1l11_opy_ (u"ࠢࡖࡵ࡬ࡲ࡬ࠦࡳࡥ࡭ࠣࡪࡱࡵࡷࠡࡨࡲࡶࠥࡺࡥࡴࡶࠣࡪ࡮ࡲࡥࡴࠢࡲࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯࠰ࠥẒ"))
                self.bstack1111l111l11_opy_.bstack11lll11l111_opy_(test_files, orchestration_strategy, bstack1l1l1ll1lll_opy_)
                ordered_test_files = self.bstack1111l111l11_opy_.bstack11ll1ll11l1_opy_()
            if not ordered_test_files:
                return None
            self.bstack111l11l1_opy_(bstack11l1l11_opy_ (u"ࠣࡷࡳࡰࡴࡧࡤࡦࡦࡗࡩࡸࡺࡆࡪ࡮ࡨࡷࡈࡵࡵ࡯ࡶࠥẓ"), len(test_files))
            self.bstack111l11l1_opy_(bstack11l1l11_opy_ (u"ࠤࡱࡳࡩ࡫ࡉ࡯ࡦࡨࡼࠧẔ"), int(os.environ.get(bstack11l1l11_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡑࡓࡉࡋ࡟ࡊࡐࡇࡉ࡝ࠨẕ")) or bstack11l1l11_opy_ (u"ࠦ࠵ࠨẖ")))
            self.bstack111l11l1_opy_(bstack11l1l11_opy_ (u"ࠧࡺ࡯ࡵࡣ࡯ࡒࡴࡪࡥࡴࠤẗ"), int(os.environ.get(bstack11l1l11_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡔࡏࡅࡇࡢࡇࡔ࡛ࡎࡕࠤẘ")) or bstack11l1l11_opy_ (u"ࠢ࠲ࠤẙ")))
            self.bstack111l11l1_opy_(bstack11l1l11_opy_ (u"ࠣࡦࡲࡻࡳࡲ࡯ࡢࡦࡨࡨ࡙࡫ࡳࡵࡈ࡬ࡰࡪࡹࡃࡰࡷࡱࡸࠧẚ"), len(ordered_test_files))
            self.bstack111l11l1_opy_(bstack11l1l11_opy_ (u"ࠤࡶࡴࡱ࡯ࡴࡕࡧࡶࡸࡸࡇࡐࡊࡅࡤࡰࡱࡉ࡯ࡶࡰࡷࠦẛ"), self.bstack1111l111l11_opy_.bstack11lll11111l_opy_())
            return ordered_test_files
        except Exception as e:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠥ࡟ࡷ࡫࡯ࡳࡦࡨࡶࡤࡺࡥࡴࡶࡢࡪ࡮ࡲࡥࡴ࡟ࠣࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡵࡲࡥࡧࡵ࡭ࡳ࡭ࠠࡵࡧࡶࡸࠥࡩ࡬ࡢࡵࡶࡩࡸࡀࠠࡼࡿࠥẜ").format(e))
        return None
    def bstack111l11l1_opy_(self, key, value):
        self.bstack1111l11ll11_opy_[key] = value
    def bstack1ll1l111ll_opy_(self):
        return self.bstack1111l11ll11_opy_