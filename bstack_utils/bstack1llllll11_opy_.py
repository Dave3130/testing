# coding: UTF-8
import sys
bstack1lll1_opy_ = sys.version_info [0] == 2
bstack11l11_opy_ = 2048
bstack1_opy_ = 7
def bstack1l1_opy_ (bstack1llllll_opy_):
    global bstack1l11111_opy_
    bstack1l111l_opy_ = ord (bstack1llllll_opy_ [-1])
    bstack11l1ll1_opy_ = bstack1llllll_opy_ [:-1]
    bstack11l1l1l_opy_ = bstack1l111l_opy_ % len (bstack11l1ll1_opy_)
    bstack11111l1_opy_ = bstack11l1ll1_opy_ [:bstack11l1l1l_opy_] + bstack11l1ll1_opy_ [bstack11l1l1l_opy_:]
    if bstack1lll1_opy_:
        bstack1lllll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11l11_opy_ - (bstack1l1ll11_opy_ + bstack1l111l_opy_) % bstack1_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11111l1_opy_)])
    else:
        bstack1lllll1_opy_ = str () .join ([chr (ord (char) - bstack11l11_opy_ - (bstack1l1ll11_opy_ + bstack1l111l_opy_) % bstack1_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11111l1_opy_)])
    return eval (bstack1lllll1_opy_)
import os
from bstack_utils.constants import *
from browserstack_sdk.sdk_cli.cli import cli
from bstack_utils.bstack11ll1llllll_opy_ import bstack11ll1ll111l_opy_
from bstack_utils.bstack1111ll11_opy_ import bstack111lll1l_opy_
from bstack_utils.helper import bstack1ll1111ll1_opy_
import json
class bstack1llll111l_opy_:
    _1ll1ll11l1l_opy_ = None
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.bstack11111lllll1_opy_ = bstack11ll1ll111l_opy_(self.config, logger)
        self.bstack1111ll11_opy_ = bstack111lll1l_opy_.bstack1111ll1l_opy_(config=self.config)
        self.bstack1111l1111ll_opy_ = {}
        self.bstack1llll1lll_opy_ = False
        self.bstack11111llll11_opy_ = (
            self.__1111l1111l1_opy_()
            and self.bstack1111ll11_opy_ is not None
            and self.bstack1111ll11_opy_.bstack1lll1llll_opy_()
            and config.get(bstack1l1_opy_ (u"ࠧࡱࡴࡲ࡮ࡪࡩࡴࡏࡣࡰࡩࠬẠ"), None) is not None
            and config.get(bstack1l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫạ"), os.path.basename(os.getcwd())) is not None
        )
    @classmethod
    def bstack1111ll1l_opy_(cls, config, logger):
        if cls._1ll1ll11l1l_opy_ is None and config is not None:
            cls._1ll1ll11l1l_opy_ = bstack1llll111l_opy_(config, logger)
        return cls._1ll1ll11l1l_opy_
    def bstack1lll1llll_opy_(self):
        bstack1l1_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࠣࠤࠥࠦࡄࡰࠢࡱࡳࡹࠦࡡࡱࡲ࡯ࡽࠥࡺࡥࡴࡶࠣࡳࡷࡪࡥࡳ࡫ࡱ࡫ࠥࡽࡨࡦࡰ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠ࠮ࠢࡒ࠵࠶ࡿࠠࡪࡵࠣࡲࡴࡺࠠࡦࡰࡤࡦࡱ࡫ࡤࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࠲ࠦࡏࡳࡦࡨࡶ࡮ࡴࡧࠡ࡫ࡶࠤࡳࡵࡴࠡࡧࡱࡥࡧࡲࡥࡥࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࠳ࠠࡱࡴࡲ࡮ࡪࡩࡴࡏࡣࡰࡩࠥ࡯ࡳࠡࡐࡲࡲࡪࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࠰ࠤࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠠࡪࡵࠣࡒࡴࡴࡥࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧẢ")
        return self.bstack11111llll11_opy_ and self.bstack11111llll1l_opy_()
    def bstack11111llll1l_opy_(self):
        bstack11111lll1ll_opy_ = os.getenv(bstack1l1_opy_ (u"ࠪࡊࡗࡇࡍࡆ࡙ࡒࡖࡐࡥࡕࡔࡇࡇࠫả"), self.config.get(bstack1l1_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧẤ"), None))
        return bstack11111lll1ll_opy_ in bstack11l11lllll1_opy_
    def __1111l1111l1_opy_(self):
        bstack11ll11lll1l_opy_ = False
        for fw in bstack11l1l111111_opy_:
            if fw in self.config.get(bstack1l1_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨấ"), bstack1l1_opy_ (u"࠭ࠧẦ")):
                bstack11ll11lll1l_opy_ = True
        return bstack1ll1111ll1_opy_(self.config.get(bstack1l1_opy_ (u"ࠧࡵࡧࡶࡸࡔࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠫầ"), bstack11ll11lll1l_opy_))
    def bstack1111l111111_opy_(self):
        return (not self.bstack1lll1llll_opy_() and
                self.bstack1111ll11_opy_ is not None and self.bstack1111ll11_opy_.bstack1lll1llll_opy_())
    def bstack1111l111l11_opy_(self):
        if not self.bstack1111l111111_opy_():
            return
        if self.config.get(bstack1l1_opy_ (u"ࠨࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪ࠭Ẩ"), None) is None or self.config.get(bstack1l1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬẩ"), os.path.basename(os.getcwd())) is None:
            self.logger.info(bstack1l1_opy_ (u"ࠥࡘࡪࡹࡴࠡࡔࡨࡳࡷࡪࡥࡳ࡫ࡱ࡫ࠥࡩࡡ࡯ࠩࡷࠤࡼࡵࡲ࡬ࠢࡤࡷࠥࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠡࡱࡵࠤࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠢ࡬ࡷࠥࡴࡵ࡭࡮࠱ࠤࡕࡲࡥࡢࡵࡨࠤࡸ࡫ࡴࠡࡣࠣࡲࡴࡴ࠭࡯ࡷ࡯ࡰࠥࡼࡡ࡭ࡷࡨ࠲ࠧẪ"))
        if not self.__1111l1111l1_opy_():
            self.logger.info(bstack1l1_opy_ (u"࡙ࠦ࡫ࡳࡵࠢࡕࡩࡴࡸࡤࡦࡴ࡬ࡲ࡬ࠦࡣࡢࡰࠪࡸࠥࡽ࡯ࡳ࡭ࠣࡥࡸࠦࡴࡦࡵࡷࡖࡪࡶ࡯ࡳࡶ࡬ࡲ࡬ࠦࡩࡴࠢࡧ࡭ࡸࡧࡢ࡭ࡧࡧ࠲ࠥࡖ࡬ࡦࡣࡶࡩࠥ࡫࡮ࡢࡤ࡯ࡩࠥ࡯ࡴࠡࡨࡵࡳࡲࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡿ࡭࡭ࠢࡩ࡭ࡱ࡫࠮ࠣẫ"))
    def bstack1111l11111l_opy_(self):
        return self.bstack1llll1lll_opy_
    def bstack1lll1l111_opy_(self, bstack11111llllll_opy_):
        self.bstack1llll1lll_opy_ = bstack11111llllll_opy_
        self.bstack1lllll1l1_opy_(bstack1l1_opy_ (u"ࠧࡧࡰࡱ࡮࡬ࡩࡩࠨẬ"), bstack11111llllll_opy_)
    def bstack111ll111_opy_(self, test_files):
        try:
            if test_files is None:
                self.logger.debug(bstack1l1_opy_ (u"ࠨ࡛ࡳࡧࡲࡶࡩ࡫ࡲࡠࡶࡨࡷࡹࡥࡦࡪ࡮ࡨࡷࡢࠦࡎࡰࠢࡷࡩࡸࡺࠠࡧ࡫࡯ࡩࡸࠦࡰࡳࡱࡹ࡭ࡩ࡫ࡤࠡࡨࡲࡶࠥࡵࡲࡥࡧࡵ࡭ࡳ࡭࠮ࠣậ"))
                return None
            orchestration_strategy = None
            orchestration_metadata = self.bstack1111ll11_opy_.bstack111lll1111l_opy_()
            if self.bstack1111ll11_opy_ is not None:
                orchestration_strategy = self.bstack1111ll11_opy_.bstack1ll111ll1l_opy_()
            if orchestration_strategy is None:
                self.logger.error(bstack1l1_opy_ (u"ࠢࡐࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴࠠࡴࡶࡵࡥࡹ࡫ࡧࡺࠢ࡬ࡷࠥࡔ࡯࡯ࡧ࠱ࠤࡈࡧ࡮࡯ࡱࡷࠤࡵࡸ࡯ࡤࡧࡨࡨࠥࡽࡩࡵࡪࠣࡸࡪࡹࡴࠡࡱࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࠡࡵࡨࡷࡸ࡯࡯࡯࠰ࠥẮ"))
                return None
            self.logger.info(bstack1l1_opy_ (u"ࠣࡔࡨࡳࡷࡪࡥࡳ࡫ࡱ࡫ࠥࡺࡥࡴࡶࠣࡪ࡮ࡲࡥࡴࠢࡺ࡭ࡹ࡮ࠠࡰࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴࠠࡴࡶࡵࡥࡹ࡫ࡧࡺ࠼ࠣࡿࢂࠨắ").format(orchestration_strategy))
            if cli.is_running():
                self.logger.debug(bstack1l1_opy_ (u"ࠤࡘࡷ࡮ࡴࡧࠡࡅࡏࡍࠥ࡬࡬ࡰࡹࠣࡪࡴࡸࠠࡵࡧࡶࡸࠥ࡬ࡩ࡭ࡧࡶࠤࡴࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱ࠲ࠧẰ"))
                ordered_test_files = cli.test_orchestration_session(test_files, orchestration_strategy, json.dumps(orchestration_metadata))
            else:
                self.logger.debug(bstack1l1_opy_ (u"࡙ࠥࡸ࡯࡮ࡨࠢࡶࡨࡰࠦࡦ࡭ࡱࡺࠤ࡫ࡵࡲࠡࡶࡨࡷࡹࠦࡦࡪ࡮ࡨࡷࠥࡵࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲ࠳ࠨằ"))
                self.bstack11111lllll1_opy_.bstack11ll1lll111_opy_(test_files, orchestration_strategy, orchestration_metadata)
                ordered_test_files = self.bstack11111lllll1_opy_.bstack11lll111111_opy_()
            if not ordered_test_files:
                return None
            self.bstack1lllll1l1_opy_(bstack1l1_opy_ (u"ࠦࡺࡶ࡬ࡰࡣࡧࡩࡩ࡚ࡥࡴࡶࡉ࡭ࡱ࡫ࡳࡄࡱࡸࡲࡹࠨẲ"), len(test_files))
            self.bstack1lllll1l1_opy_(bstack1l1_opy_ (u"ࠧࡴ࡯ࡥࡧࡌࡲࡩ࡫ࡸࠣẳ"), int(os.environ.get(bstack1l1_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡔࡏࡅࡇࡢࡍࡓࡊࡅ࡙ࠤẴ")) or bstack1l1_opy_ (u"ࠢ࠱ࠤẵ")))
            self.bstack1lllll1l1_opy_(bstack1l1_opy_ (u"ࠣࡶࡲࡸࡦࡲࡎࡰࡦࡨࡷࠧẶ"), int(os.environ.get(bstack1l1_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡐࡒࡈࡊࡥࡃࡐࡗࡑࡘࠧặ")) or bstack1l1_opy_ (u"ࠥ࠵ࠧẸ")))
            self.bstack1lllll1l1_opy_(bstack1l1_opy_ (u"ࠦࡩࡵࡷ࡯࡮ࡲࡥࡩ࡫ࡤࡕࡧࡶࡸࡋ࡯࡬ࡦࡵࡆࡳࡺࡴࡴࠣẹ"), len(ordered_test_files))
            self.bstack1lllll1l1_opy_(bstack1l1_opy_ (u"ࠧࡹࡰ࡭࡫ࡷࡘࡪࡹࡴࡴࡃࡓࡍࡈࡧ࡬࡭ࡅࡲࡹࡳࡺࠢẺ"), self.bstack11111lllll1_opy_.bstack11ll1l1llll_opy_())
            return ordered_test_files
        except Exception as e:
            self.logger.debug(bstack1l1_opy_ (u"ࠨ࡛ࡳࡧࡲࡶࡩ࡫ࡲࡠࡶࡨࡷࡹࡥࡦࡪ࡮ࡨࡷࡢࠦࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡱࡵࡨࡪࡸࡩ࡯ࡩࠣࡸࡪࡹࡴࠡࡥ࡯ࡥࡸࡹࡥࡴ࠼ࠣࡿࢂࠨẻ").format(e))
        return None
    def bstack1lllll1l1_opy_(self, key, value):
        self.bstack1111l1111ll_opy_[key] = value
    def bstack1l1l111111_opy_(self):
        return self.bstack1111l1111ll_opy_