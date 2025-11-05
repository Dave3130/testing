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
from datetime import datetime
import os
import threading
from browserstack_sdk.sdk_cli.bstack1llll1l1l11_opy_ import (
    bstack1lllllll1l1_opy_,
    bstack1llllll1111_opy_,
    bstack1lll1111l1l_opy_,
    bstack1llll111l1l_opy_,
)
from browserstack_sdk.sdk_cli.bstack1lllll111ll_opy_ import bstack1lllll1111l_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1ll111l_opy_, bstack1lll1ll1l1l_opy_, bstack1lll1l1ll1l_opy_
from typing import Tuple, Dict, Any, List, Union
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1lllll1l11l_opy_ import bstack1llll111ll1_opy_
from browserstack_sdk.sdk_cli.bstack1lll111111l_opy_ import bstack1ll1lllll1l_opy_
from browserstack_sdk.sdk_cli.bstack1llll1111ll_opy_ import bstack1lll1ll1lll_opy_
from browserstack_sdk.sdk_cli.bstack1lll1lll11l_opy_ import bstack1llll11111l_opy_
from bstack_utils.helper import bstack1l111l1l1l1_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
from bstack_utils.bstack1ll11111ll_opy_ import bstack1llll1ll1l1_opy_
import grpc
import traceback
import json
class bstack1l11llll11l_opy_(bstack1llll111ll1_opy_):
    bstack1l1ll111lll_opy_ = False
    bstack1l111l1llll_opy_ = bstack11111_opy_ (u"ࠨࡳࡦ࡮ࡨࡲ࡮ࡻ࡭࠯ࡹࡨࡦࡩࡸࡩࡷࡧࡵࠦᑥ")
    bstack1l111l111ll_opy_ = bstack11111_opy_ (u"ࠢࡳࡧࡰࡳࡹ࡫࠮ࡸࡧࡥࡨࡷ࡯ࡶࡦࡴࠥᑦ")
    bstack1l11111l1ll_opy_ = bstack11111_opy_ (u"ࠣࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡠ࡫ࡱ࡭ࡹࠨᑧ")
    bstack1l1111llll1_opy_ = bstack11111_opy_ (u"ࠤࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡡ࡬ࡷࡤࡹࡣࡢࡰࡱ࡭ࡳ࡭ࠢᑨ")
    bstack1l1111ll111_opy_ = bstack11111_opy_ (u"ࠥࡨࡷ࡯ࡶࡦࡴࡢ࡬ࡦࡹ࡟ࡶࡴ࡯ࠦᑩ")
    scripts: Dict[str, Dict[str, str]]
    commands: Dict[str, Dict[str, Dict[str, List[str]]]]
    def __init__(self, bstack1l1l11ll1l1_opy_, bstack1ll1ll1ll1l_opy_):
        super().__init__()
        self.scripts = dict()
        self.commands = dict()
        self.accessibility = False
        self.bstack1l1111ll11l_opy_ = False
        self.bstack1l11111llll_opy_ = dict()
        self.bstack1l11111ll11_opy_ = False
        self.bstack1l1111l11l1_opy_ = dict()
        if not self.is_enabled():
            return
        self.bstack1l111lll1ll_opy_ = bstack1ll1ll1ll1l_opy_
        bstack1l1l11ll1l1_opy_.bstack1llll11ll11_opy_((bstack1lllllll1l1_opy_.bstack1lllll1llll_opy_, bstack1llllll1111_opy_.PRE), self.bstack1l111l11ll1_opy_)
        TestFramework.bstack1llll11ll11_opy_((bstack1lll1ll111l_opy_.TEST, bstack1lll1ll1l1l_opy_.PRE), self.bstack1lll11ll1l1_opy_)
        TestFramework.bstack1llll11ll11_opy_((bstack1lll1ll111l_opy_.TEST, bstack1lll1ll1l1l_opy_.POST), self.bstack1lll1ll1ll1_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1lll11ll1l1_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1ll1l_opy_,
        bstack1llll11ll1l_opy_: Tuple[bstack1lll1ll111l_opy_, bstack1lll1ll1l1l_opy_],
        *args,
        **kwargs,
    ):
        tags = self._1l111l11lll_opy_(instance, args)
        test_framework = f.get_state(instance, TestFramework.bstack1lll11l11l1_opy_)
        if self.bstack1l1111ll11l_opy_:
            self.bstack1l11111llll_opy_[bstack11111_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠦᑪ")] = f.get_state(instance, TestFramework.bstack1lll1lll1ll_opy_)
        if bstack11111_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠩᑫ") in instance.bstack1ll11llllll_opy_:
            platform_index = f.get_state(instance, TestFramework.bstack1lllll1ll11_opy_)
            self.accessibility = self.bstack1l111l11111_opy_(tags, self.config[bstack11111_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩᑬ")][platform_index])
        else:
            capabilities = self.bstack1l111lll1ll_opy_.bstack1lll1l11l1l_opy_(f, instance, bstack1llll11ll1l_opy_, *args, **kwargs)
            if not capabilities:
                self.logger.debug(bstack11111_opy_ (u"ࠢࡰࡰࡢࡦࡪ࡬࡯ࡳࡧࡢࡸࡪࡹࡴ࠻ࠢࡱࡳࠥࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠤ࡫ࡵࡵ࡯ࡦࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᑭ") + str(kwargs) + bstack11111_opy_ (u"ࠣࠤᑮ"))
                return
            self.accessibility = self.bstack1l111l11111_opy_(tags, capabilities)
        if self.bstack1l111lll1ll_opy_.pages and self.bstack1l111lll1ll_opy_.pages.values():
            bstack1l11111l111_opy_ = list(self.bstack1l111lll1ll_opy_.pages.values())
            if bstack1l11111l111_opy_ and isinstance(bstack1l11111l111_opy_[0], (list, tuple)) and bstack1l11111l111_opy_[0]:
                bstack1l111111l11_opy_ = bstack1l11111l111_opy_[0][0]
                if callable(bstack1l111111l11_opy_):
                    page = bstack1l111111l11_opy_()
                    def bstack1ll1111l1_opy_():
                        self.get_accessibility_results(page, bstack11111_opy_ (u"ࠤࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠨᑯ"))
                    def bstack1l111l1l111_opy_():
                        self.get_accessibility_results_summary(page, bstack11111_opy_ (u"ࠥࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠢᑰ"))
                    setattr(page, bstack11111_opy_ (u"ࠦ࡬࡫ࡴࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡒࡦࡵࡸࡰࡹࡹࠢᑱ"), bstack1ll1111l1_opy_)
                    setattr(page, bstack11111_opy_ (u"ࠧ࡭ࡥࡵࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡓࡧࡶࡹࡱࡺࡓࡶ࡯ࡰࡥࡷࡿࠢᑲ"), bstack1l111l1l111_opy_)
        self.logger.debug(bstack11111_opy_ (u"ࠨࡳࡩࡱࡸࡰࡩࠦࡲࡶࡰࠣࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡺࡦࡲࡵࡦ࠿ࠥᑳ") + str(self.accessibility) + bstack11111_opy_ (u"ࠢࠣᑴ"))
    def bstack1l111l11ll1_opy_(
        self,
        f: bstack1lllll1111l_opy_,
        driver: object,
        exec: Tuple[bstack1llll111l1l_opy_, str],
        bstack1llll11ll1l_opy_: Tuple[bstack1lllllll1l1_opy_, bstack1llllll1111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        try:
            bstack11lll11111_opy_ = datetime.now()
            self.bstack1l111l1111l_opy_(f, exec, *args, **kwargs)
            instance, method_name = exec
            instance.bstack1llll1l111_opy_(bstack11111_opy_ (u"ࠣࡣ࠴࠵ࡾࡀࡩ࡯࡫ࡷࡣࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡣࡨࡵ࡮ࡧ࡫ࡪࠦᑵ"), datetime.now() - bstack11lll11111_opy_)
            if (
                not f.bstack1l1ll1l1lll_opy_(method_name)
                or f.bstack1l1lll111l1_opy_(method_name, *args)
                or f.bstack1l1lll11111_opy_(method_name, *args)
            ):
                return
            if not f.get_state(instance, bstack1l11llll11l_opy_.bstack1l11111l1ll_opy_, False):
                if not bstack1l11llll11l_opy_.bstack1l1ll111lll_opy_:
                    self.logger.warning(bstack11111_opy_ (u"ࠤ࡞ࡴࡱࡧࡴࡧࡱࡵࡱࡤ࡯࡮ࡥࡧࡻࡁࠧᑶ") + str(f.platform_index) + bstack11111_opy_ (u"ࠥࡡࠥࡧ࠱࠲ࡻࠣࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠢ࡫ࡥࡻ࡫ࠠ࡯ࡱࡷࠤࡧ࡫ࡥ࡯ࠢࡶࡩࡹࠦࡦࡰࡴࠣࡸ࡭࡯ࡳࠡࡵࡨࡷࡸ࡯࡯࡯ࠤᑷ"))
                    bstack1l11llll11l_opy_.bstack1l1ll111lll_opy_ = True
                return
            bstack1l111l11l11_opy_ = self.scripts.get(f.framework_name, {})
            if not bstack1l111l11l11_opy_:
                platform_index = f.get_state(instance, bstack1lllll1111l_opy_.bstack1lllll1ll11_opy_, 0)
                self.logger.debug(bstack11111_opy_ (u"ࠦࡳࡵࠠࡢ࠳࠴ࡽࠥࡹࡣࡳ࡫ࡳࡸࡸࠦࡦࡰࡴࠣࡴࡱࡧࡴࡧࡱࡵࡱࡤ࡯࡮ࡥࡧࡻࡁࢀࡶ࡬ࡢࡶࡩࡳࡷࡳ࡟ࡪࡰࡧࡩࡽࢃࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥ࠾ࠤᑸ") + str(f.framework_name) + bstack11111_opy_ (u"ࠧࠨᑹ"))
                return
            command_name = f.bstack1l1ll1lll1l_opy_(*args)
            if not command_name:
                self.logger.debug(bstack11111_opy_ (u"ࠨ࡭ࡪࡵࡶ࡭ࡳ࡭ࠠࡤࡱࡰࡱࡦࡴࡤࡠࡰࡤࡱࡪࠦࡦࡰࡴࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࡁࢀ࡬࠮ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥࡾࠢࡰࡩࡹ࡮࡯ࡥࡡࡱࡥࡲ࡫࠽ࠣᑺ") + str(method_name) + bstack11111_opy_ (u"ࠢࠣᑻ"))
                return
            bstack1l111111lll_opy_ = f.get_state(instance, bstack1l11llll11l_opy_.bstack1l1111ll111_opy_, False)
            if command_name == bstack11111_opy_ (u"ࠣࡩࡨࡸࠧᑼ") and not bstack1l111111lll_opy_:
                f.bstack1lllllll11l_opy_(instance, bstack1l11llll11l_opy_.bstack1l1111ll111_opy_, True)
                bstack1l111111lll_opy_ = True
            if not bstack1l111111lll_opy_ and not self.bstack1l1111ll11l_opy_:
                self.logger.debug(bstack11111_opy_ (u"ࠤࡱࡳ࡛ࠥࡒࡍࠢ࡯ࡳࡦࡪࡥࡥࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࡀࡿ࡫࠴ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫ࡽࠡࡥࡲࡱࡲࡧ࡮ࡥࡡࡱࡥࡲ࡫࠽ࠣᑽ") + str(command_name) + bstack11111_opy_ (u"ࠥࠦᑾ"))
                return
            scripts_to_run = self.commands.get(f.framework_name, {}).get(method_name, {}).get(command_name, [])
            if not scripts_to_run:
                self.logger.debug(bstack11111_opy_ (u"ࠦࡳࡵࠠࡢ࠳࠴ࡽࠥࡹࡣࡳ࡫ࡳࡸࡸࠦࡦࡰࡴࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࡁࢀ࡬࠮ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥࡾࠢࡦࡳࡲࡳࡡ࡯ࡦࡢࡲࡦࡳࡥ࠾ࠤᑿ") + str(command_name) + bstack11111_opy_ (u"ࠧࠨᒀ"))
                return
            self.logger.info(bstack11111_opy_ (u"ࠨࡲࡶࡰࡱ࡭ࡳ࡭ࠠࡼ࡮ࡨࡲ࠭ࡹࡣࡳ࡫ࡳࡸࡸࡥࡴࡰࡡࡵࡹࡳ࠯ࡽࠡࡵࡦࡶ࡮ࡶࡴࡴࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࡀࡿ࡫࠴ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫ࡽࠡࡥࡲࡱࡲࡧ࡮ࡥࡡࡱࡥࡲ࡫࠽ࠣᒁ") + str(command_name) + bstack11111_opy_ (u"ࠢࠣᒂ"))
            scripts = [(s, bstack1l111l11l11_opy_[s]) for s in scripts_to_run if s in bstack1l111l11l11_opy_]
            for script_name, bstack1lll1ll11l1_opy_ in scripts:
                try:
                    bstack11lll11111_opy_ = datetime.now()
                    if script_name == bstack11111_opy_ (u"ࠣࡵࡦࡥࡳࠨᒃ"):
                        result = self.perform_scan(driver, method=command_name, framework_name=f.framework_name)
                    instance.bstack1llll1l111_opy_(bstack11111_opy_ (u"ࠤࡤ࠵࠶ࡿ࠺ࠣᒄ") + script_name, datetime.now() - bstack11lll11111_opy_)
                    if isinstance(result, dict) and not result.get(bstack11111_opy_ (u"ࠥࡷࡺࡩࡣࡦࡵࡶࠦᒅ"), True):
                        self.logger.warning(bstack11111_opy_ (u"ࠦࡸࡱࡩࡱࠢࡨࡼࡪࡩࡵࡵ࡫ࡱ࡫ࠥࡸࡥ࡮ࡣ࡬ࡲ࡮ࡴࡧࠡࡵࡦࡶ࡮ࡶࡴࡴ࠼ࠣࠦᒆ") + str(result) + bstack11111_opy_ (u"ࠧࠨᒇ"))
                        break
                except Exception as e:
                    self.logger.error(bstack11111_opy_ (u"ࠨࡥࡳࡴࡲࡶࠥ࡫ࡸࡦࡥࡸࡸ࡮ࡴࡧࠡࡵࡦࡶ࡮ࡶࡴ࠾ࡽࡶࡧࡷ࡯ࡰࡵࡡࡱࡥࡲ࡫ࡽࠡࡧࡵࡶࡴࡸ࠽ࠣᒈ") + str(e) + bstack11111_opy_ (u"ࠢࠣᒉ"))
        except Exception as e:
            self.logger.error(bstack11111_opy_ (u"ࠣࡱࡱࡣࡧ࡫ࡦࡰࡴࡨࡣࡪࡾࡥࡤࡷࡷࡩࠥ࡫ࡲࡳࡱࡵࡁࠧᒊ") + str(e) + bstack11111_opy_ (u"ࠤࠥᒋ"))
    def bstack1lll1ll1ll1_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1ll1l_opy_,
        bstack1llll11ll1l_opy_: Tuple[bstack1lll1ll111l_opy_, bstack1lll1ll1l1l_opy_],
        *args,
        **kwargs,
    ):
        tags = self._1l111l11lll_opy_(instance, args)
        capabilities = self.bstack1l111lll1ll_opy_.bstack1lll1l11l1l_opy_(f, instance, bstack1llll11ll1l_opy_, *args, **kwargs)
        self.accessibility = self.bstack1l111l11111_opy_(tags, capabilities)
        if not self.accessibility:
            self.logger.debug(bstack11111_opy_ (u"ࠥࡳࡳࡥࡡࡧࡶࡨࡶࡤࡺࡥࡴࡶ࠽ࠤࡦ࠷࠱ࡺࠢࡱࡳࡹࠦࡥ࡯ࡣࡥࡰࡪࡪࠢᒌ"))
            return
        driver = self.bstack1l111lll1ll_opy_.bstack1llll111l11_opy_(f, instance, bstack1llll11ll1l_opy_, *args, **kwargs)
        test_name = f.get_state(instance, TestFramework.bstack1ll1l11l11l_opy_)
        if not test_name:
            self.logger.debug(bstack11111_opy_ (u"ࠦࡴࡴ࡟ࡢࡨࡷࡩࡷࡥࡴࡦࡵࡷ࠾ࠥࡳࡩࡴࡵ࡬ࡲ࡬ࠦࡴࡦࡵࡷࠤࡳࡧ࡭ࡦࠤᒍ"))
            return
        test_uuid = f.get_state(instance, TestFramework.bstack1lll1lll1ll_opy_)
        if not test_uuid:
            self.logger.debug(bstack11111_opy_ (u"ࠧࡵ࡮ࡠࡣࡩࡸࡪࡸ࡟ࡵࡧࡶࡸ࠿ࠦ࡭ࡪࡵࡶ࡭ࡳ࡭ࠠࡵࡧࡶࡸࠥࡻࡵࡪࡦࠥᒎ"))
            return
        if isinstance(self.bstack1l111lll1ll_opy_, bstack1lll1ll1lll_opy_):
            framework_name = bstack11111_opy_ (u"࠭ࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠪᒏ")
        else:
            framework_name = bstack11111_opy_ (u"ࠧࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࠩᒐ")
        self.bstack1lll1l1ll_opy_(driver, test_name, framework_name, test_uuid)
    def perform_scan(self, driver: object, method: Union[None, str], framework_name: str):
        bstack1ll11llll1l_opy_ = bstack1llll1ll1l1_opy_.bstack1ll1111lll1_opy_(EVENTS.bstack111111lll1_opy_.value)
        if not self.accessibility:
            self.logger.debug(bstack11111_opy_ (u"ࠣࡲࡨࡶ࡫ࡵࡲ࡮ࡡࡶࡧࡦࡴ࠺ࠡࡣ࠴࠵ࡾࠦ࡮ࡰࡶࠣࡩࡳࡧࡢ࡭ࡧࡧࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࡂࢁࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫ࡽࠡࠤᒑ"))
            return
        bstack11lll11111_opy_ = datetime.now()
        bstack1lll1ll11l1_opy_ = self.scripts.get(framework_name, {}).get(bstack11111_opy_ (u"ࠤࡶࡧࡦࡴࠢᒒ"), None)
        if not bstack1lll1ll11l1_opy_:
            self.logger.debug(bstack11111_opy_ (u"ࠥࡴࡪࡸࡦࡰࡴࡰࡣࡸࡩࡡ࡯࠼ࠣࡱ࡮ࡹࡳࡪࡰࡪࠤࠬࡹࡣࡢࡰࠪࠤࡸࡩࡲࡪࡲࡷࠤ࡫ࡵࡲࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦ࠿ࠥᒓ") + str(framework_name) + bstack11111_opy_ (u"ࠦࠥࠨᒔ"))
            return
        if self.bstack1l1111ll11l_opy_:
            arg = dict()
            arg[bstack11111_opy_ (u"ࠧࡳࡥࡵࡪࡲࡨࠧᒕ")] = method if method else bstack11111_opy_ (u"ࠨࠢᒖ")
            arg[bstack11111_opy_ (u"ࠢࡵࡪࡗࡩࡸࡺࡒࡶࡰࡘࡹ࡮ࡪࠢᒗ")] = self.bstack1l11111llll_opy_[bstack11111_opy_ (u"ࠣࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠣᒘ")]
            arg[bstack11111_opy_ (u"ࠤࡷ࡬ࡇࡻࡩ࡭ࡦࡘࡹ࡮ࡪࠢᒙ")] = self.bstack1l11111llll_opy_[bstack11111_opy_ (u"ࠥࡸࡪࡹࡴࡩࡷࡥࡣࡧࡻࡩ࡭ࡦࡢࡹࡺ࡯ࡤࠣᒚ")]
            arg[bstack11111_opy_ (u"ࠦࡦࡻࡴࡩࡊࡨࡥࡩ࡫ࡲࠣᒛ")] = self.bstack1l11111llll_opy_[bstack11111_opy_ (u"ࠧࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽ࡙ࡵ࡫ࡦࡰࠥᒜ")]
            arg[bstack11111_opy_ (u"ࠨࡴࡩࡌࡺࡸ࡙ࡵ࡫ࡦࡰࠥᒝ")] = self.bstack1l11111llll_opy_[bstack11111_opy_ (u"ࠢࡵࡪࡢ࡮ࡼࡺ࡟ࡵࡱ࡮ࡩࡳࠨᒞ")]
            arg[bstack11111_opy_ (u"ࠣࡵࡦࡥࡳ࡚ࡩ࡮ࡧࡶࡸࡦࡳࡰࠣᒟ")] = str(int(datetime.now().timestamp() * 1000))
            bstack1l1111ll1ll_opy_ = self.bstack1l1111l1l1l_opy_(bstack11111_opy_ (u"ࠤࡶࡧࡦࡴࠢᒠ"), self.bstack1l11111llll_opy_[bstack11111_opy_ (u"ࠥࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠥᒡ")])
            if bstack11111_opy_ (u"ࠦࡨ࡫࡮ࡵࡴࡤࡰࡆࡻࡴࡩࡖࡲ࡯ࡪࡴࠢᒢ") in bstack1l1111ll1ll_opy_:
                bstack1l1111ll1ll_opy_ = bstack1l1111ll1ll_opy_.copy()
                bstack1l1111ll1ll_opy_[bstack11111_opy_ (u"ࠧࡩࡥ࡯ࡶࡵࡥࡱࡇࡵࡵࡪࡋࡩࡦࡪࡥࡳࠤᒣ")] = bstack1l1111ll1ll_opy_.pop(bstack11111_opy_ (u"ࠨࡣࡦࡰࡷࡶࡦࡲࡁࡶࡶ࡫ࡘࡴࡱࡥ࡯ࠤᒤ"))
            arg = bstack1l111l1l1l1_opy_(arg, bstack1l1111ll1ll_opy_)
            bstack1l1111l1ll1_opy_ = bstack1lll1ll11l1_opy_ % json.dumps(arg)
            driver.execute_script(bstack1l1111l1ll1_opy_)
            return
        instance = bstack1lll1111l1l_opy_.bstack1ll111llll1_opy_(driver)
        if instance:
            if not bstack1lll1111l1l_opy_.get_state(instance, bstack1l11llll11l_opy_.bstack1l1111llll1_opy_, False):
                bstack1lll1111l1l_opy_.bstack1lllllll11l_opy_(instance, bstack1l11llll11l_opy_.bstack1l1111llll1_opy_, True)
            else:
                self.logger.info(bstack11111_opy_ (u"ࠢࡱࡧࡵࡪࡴࡸ࡭ࡠࡵࡦࡥࡳࡀࠠࡢ࡮ࡵࡩࡦࡪࡹࠡ࡫ࡱࠤࡵࡸ࡯ࡨࡴࡨࡷࡸࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫࠽ࡼࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦࡿࠣࡱࡪࡺࡨࡰࡦࡀࠦᒥ") + str(method) + bstack11111_opy_ (u"ࠣࠤᒦ"))
                return
        self.logger.info(bstack11111_opy_ (u"ࠤࡳࡩࡷ࡬࡯ࡳ࡯ࡢࡷࡨࡧ࡮࠻ࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࡀࡿ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࢂࠦ࡭ࡦࡶ࡫ࡳࡩࡃࠢᒧ") + str(method) + bstack11111_opy_ (u"ࠥࠦᒨ"))
        if framework_name == bstack11111_opy_ (u"ࠫࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠨᒩ"):
            result = self.bstack1l111lll1ll_opy_.bstack1lll1l1llll_opy_(driver, bstack1lll1ll11l1_opy_)
        else:
            result = driver.execute_async_script(bstack1lll1ll11l1_opy_, {bstack11111_opy_ (u"ࠧࡳࡥࡵࡪࡲࡨࠧᒪ"): method if method else bstack11111_opy_ (u"ࠨࠢᒫ")})
        bstack1llll1ll1l1_opy_.end(EVENTS.bstack111111lll1_opy_.value, bstack1ll11llll1l_opy_+bstack11111_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢᒬ"), bstack1ll11llll1l_opy_+bstack11111_opy_ (u"ࠣ࠼ࡨࡲࡩࠨᒭ"), True, None, command=method)
        if instance:
            bstack1lll1111l1l_opy_.bstack1lllllll11l_opy_(instance, bstack1l11llll11l_opy_.bstack1l1111llll1_opy_, False)
            instance.bstack1llll1l111_opy_(bstack11111_opy_ (u"ࠤࡤ࠵࠶ࡿ࠺ࡱࡧࡵࡪࡴࡸ࡭ࡠࡵࡦࡥࡳࠨᒮ"), datetime.now() - bstack11lll11111_opy_)
        return result
        def bstack1l111111ll1_opy_(self, driver: object, framework_name, bstack1l1l1ll111_opy_: str):
            self.bstack1llllll11l1_opy_()
            req = structs.AccessibilityResultRequest()
            req.bin_session_id = self.bin_session_id
            req.bstack1l1111l111l_opy_ = self.bstack1l11111llll_opy_[bstack11111_opy_ (u"ࠥࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠥᒯ")]
            req.bstack1l1l1ll111_opy_ = bstack1l1l1ll111_opy_
            req.session_id = self.bin_session_id
            try:
                r = self.bstack1llll1ll1ll_opy_.AccessibilityResult(req)
                if not r.success:
                    self.logger.debug(bstack11111_opy_ (u"ࠦࡷ࡫ࡣࡦ࡫ࡹࡩࡩࠦࡦࡳࡱࡰࠤࡸ࡫ࡲࡷࡧࡵ࠾ࠥࠨᒰ") + str(r) + bstack11111_opy_ (u"ࠧࠨᒱ"))
                else:
                    bstack1l11111l11l_opy_ = json.loads(r.bstack1l1111l11ll_opy_.decode(bstack11111_opy_ (u"࠭ࡵࡵࡨ࠰࠼ࠬᒲ")))
                    if bstack1l1l1ll111_opy_ == bstack11111_opy_ (u"ࠧࡨࡧࡷࡖࡪࡹࡵ࡭ࡶࡶࠫᒳ"):
                        return bstack1l11111l11l_opy_.get(bstack11111_opy_ (u"ࠣࡦࡤࡸࡦࠨᒴ"), [])
                    else:
                        return bstack1l11111l11l_opy_.get(bstack11111_opy_ (u"ࠤࡧࡥࡹࡧࠢᒵ"), {})
            except grpc.RpcError as e:
                self.logger.error(bstack11111_opy_ (u"ࠥࡶࡵࡩ࠭ࡦࡴࡵࡳࡷࠦࡷࡩ࡫࡯ࡩࠥ࡬ࡥࡵࡥ࡫࡭ࡳ࡭ࠠࡨࡧࡷࡣࡦࡶࡰࡠࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡠࡴࡨࡷࡺࡲࡴࠡࡨࡵࡳࡲࠦࡣ࡭࡫࠽ࠤࠧᒶ") + str(e) + bstack11111_opy_ (u"ࠦࠧᒷ"))
    @measure(event_name=EVENTS.bstack1l11l11l1_opy_, stage=STAGE.bstack111l1l11l_opy_)
    def get_accessibility_results(self, driver: object, framework_name):
        if not self.accessibility:
            self.logger.debug(bstack11111_opy_ (u"ࠧ࡭ࡥࡵࡡࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡡࡵࡩࡸࡻ࡬ࡵࡵ࠽ࠤࡦ࠷࠱ࡺࠢࡱࡳࡹࠦࡥ࡯ࡣࡥࡰࡪࡪࠢᒸ"))
            return
        if self.bstack1l1111ll11l_opy_:
            self.logger.debug(bstack11111_opy_ (u"࠭ࡐࡦࡴࡩࡳࡷࡳࡩ࡯ࡩࠣࡷࡨࡧ࡮ࠡࡨࡲࡶࠥࡧࡰࡱࠢࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩᒹ"))
            self.perform_scan(driver, method=None, framework_name=framework_name)
            return self.bstack1l111111ll1_opy_(driver, framework_name, bstack11111_opy_ (u"ࠢࡨࡧࡷࡖࡪࡹࡵ࡭ࡶࡶࠦᒺ"))
        bstack1lll1ll11l1_opy_ = self.scripts.get(framework_name, {}).get(bstack11111_opy_ (u"ࠣࡩࡨࡸࡗ࡫ࡳࡶ࡮ࡷࡷࠧᒻ"), None)
        if not bstack1lll1ll11l1_opy_:
            self.logger.debug(bstack11111_opy_ (u"ࠤࡰ࡭ࡸࡹࡩ࡯ࡩࠣࠫ࡬࡫ࡴࡓࡧࡶࡹࡱࡺࡳࠨࠢࡶࡧࡷ࡯ࡰࡵࠢࡩࡳࡷࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫࠽ࠣᒼ") + str(framework_name) + bstack11111_opy_ (u"ࠥࠦᒽ"))
            return
        self.perform_scan(driver, method=None, framework_name=framework_name)
        bstack11lll11111_opy_ = datetime.now()
        if framework_name == bstack11111_opy_ (u"ࠫࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠨᒾ"):
            result = self.bstack1l111lll1ll_opy_.bstack1lll1l1llll_opy_(driver, bstack1lll1ll11l1_opy_)
        else:
            result = driver.execute_async_script(bstack1lll1ll11l1_opy_)
        instance = bstack1lll1111l1l_opy_.bstack1ll111llll1_opy_(driver)
        if instance:
            instance.bstack1llll1l111_opy_(bstack11111_opy_ (u"ࠧࡧ࠱࠲ࡻ࠽࡫ࡪࡺ࡟ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿ࡟ࡳࡧࡶࡹࡱࡺࡳࠣᒿ"), datetime.now() - bstack11lll11111_opy_)
        return result
    @measure(event_name=EVENTS.bstack1ll11l11ll_opy_, stage=STAGE.bstack111l1l11l_opy_)
    def get_accessibility_results_summary(self, driver: object, framework_name):
        if not self.accessibility:
            self.logger.debug(bstack11111_opy_ (u"ࠨࡧࡦࡶࡢࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡢࡶࡪࡹࡵ࡭ࡶࡶࡣࡸࡻ࡭࡮ࡣࡵࡽ࠿ࠦࡡ࠲࠳ࡼࠤࡳࡵࡴࠡࡧࡱࡥࡧࡲࡥࡥࠤᓀ"))
            return
        if self.bstack1l1111ll11l_opy_:
            self.perform_scan(driver, method=None, framework_name=framework_name)
            return self.bstack1l111111ll1_opy_(driver, framework_name, bstack11111_opy_ (u"ࠧࡨࡧࡷࡖࡪࡹࡵ࡭ࡶࡶࡗࡺࡳ࡭ࡢࡴࡼࠫᓁ"))
        bstack1lll1ll11l1_opy_ = self.scripts.get(framework_name, {}).get(bstack11111_opy_ (u"ࠣࡩࡨࡸࡗ࡫ࡳࡶ࡮ࡷࡷࡘࡻ࡭࡮ࡣࡵࡽࠧᓂ"), None)
        if not bstack1lll1ll11l1_opy_:
            self.logger.debug(bstack11111_opy_ (u"ࠤࡰ࡭ࡸࡹࡩ࡯ࡩࠣࠫ࡬࡫ࡴࡓࡧࡶࡹࡱࡺࡳࡔࡷࡰࡱࡦࡸࡹࠨࠢࡶࡧࡷ࡯ࡰࡵࠢࡩࡳࡷࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫࠽ࠣᓃ") + str(framework_name) + bstack11111_opy_ (u"ࠥࠦᓄ"))
            return
        self.perform_scan(driver, method=None, framework_name=framework_name)
        bstack11lll11111_opy_ = datetime.now()
        if framework_name == bstack11111_opy_ (u"ࠫࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠨᓅ"):
            result = self.bstack1l111lll1ll_opy_.bstack1lll1l1llll_opy_(driver, bstack1lll1ll11l1_opy_)
        else:
            result = driver.execute_async_script(bstack1lll1ll11l1_opy_)
        instance = bstack1lll1111l1l_opy_.bstack1ll111llll1_opy_(driver)
        if instance:
            instance.bstack1llll1l111_opy_(bstack11111_opy_ (u"ࠧࡧ࠱࠲ࡻ࠽࡫ࡪࡺ࡟ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿ࡟ࡳࡧࡶࡹࡱࡺࡳࡠࡵࡸࡱࡲࡧࡲࡺࠤᓆ"), datetime.now() - bstack11lll11111_opy_)
        return result
    @measure(event_name=EVENTS.bstack1l111ll1111_opy_, stage=STAGE.bstack111l1l11l_opy_)
    def bstack1l1111ll1l1_opy_(
        self,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        hub_url: str,
    ):
        self.bstack1llllll11l1_opy_()
        req = structs.AccessibilityConfigRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.hub_url = hub_url
        try:
            r = self.bstack1llll1ll1ll_opy_.AccessibilityConfig(req)
            if not r.success:
                self.logger.debug(bstack11111_opy_ (u"ࠨࡲࡦࡥࡨ࡭ࡻ࡫ࡤࠡࡨࡵࡳࡲࠦࡳࡦࡴࡹࡩࡷࡀࠠࠣᓇ") + str(r) + bstack11111_opy_ (u"ࠢࠣᓈ"))
            else:
                self.bstack1l1111lllll_opy_(framework_name, r)
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11111_opy_ (u"ࠣࡴࡳࡧ࠲࡫ࡲࡳࡱࡵ࠾ࠥࠨᓉ") + str(e) + bstack11111_opy_ (u"ࠤࠥᓊ"))
            traceback.print_exc()
            raise e
    def bstack1l1111lllll_opy_(self, framework_name: str, result: structs.AccessibilityConfigResponse) -> bool:
        if not result.success or not result.accessibility.success:
            self.logger.debug(bstack11111_opy_ (u"ࠥࡰࡴࡧࡤࡠࡥࡲࡲ࡫࡯ࡧ࠻ࠢࡤ࠵࠶ࡿࠠ࡯ࡱࡷࠤ࡫ࡵࡵ࡯ࡦࠥᓋ"))
            return False
        if result.accessibility.is_app_accessibility:
            self.bstack1l1111ll11l_opy_ = result.accessibility.is_app_accessibility
        if result.testhub.build_hashed_id:
            self.bstack1l11111llll_opy_[bstack11111_opy_ (u"ࠦࡹ࡫ࡳࡵࡪࡸࡦࡤࡨࡵࡪ࡮ࡧࡣࡺࡻࡩࡥࠤᓌ")] = result.testhub.build_hashed_id
        if result.testhub.jwt:
            self.bstack1l11111llll_opy_[bstack11111_opy_ (u"ࠧࡺࡨࡠ࡬ࡺࡸࡤࡺ࡯࡬ࡧࡱࠦᓍ")] = result.testhub.jwt
        if result.accessibility.options:
            options = result.accessibility.options
            if options.capabilities:
                for caps in options.capabilities:
                    self.bstack1l11111llll_opy_[caps.name] = caps.value
            if options.scripts:
                self.scripts[framework_name] = {row.name: row.command for row in options.scripts}
            if options.commands_to_wrap and options.commands_to_wrap.commands:
                scripts_to_run = [s for s in options.commands_to_wrap.scripts_to_run]
                if not scripts_to_run:
                    return False
                bstack1l111l1l1ll_opy_ = dict()
                for command in options.commands_to_wrap.commands:
                    if command.library == self.bstack1l111l1llll_opy_ and command.module == self.bstack1l111l111ll_opy_:
                        if command.method and not command.method in bstack1l111l1l1ll_opy_:
                            bstack1l111l1l1ll_opy_[command.method] = dict()
                        if command.name and not command.name in bstack1l111l1l1ll_opy_[command.method]:
                            bstack1l111l1l1ll_opy_[command.method][command.name] = list()
                        bstack1l111l1l1ll_opy_[command.method][command.name].extend(scripts_to_run)
                self.commands[framework_name] = bstack1l111l1l1ll_opy_
        return bool(self.commands.get(framework_name, None))
    def bstack1l111l1111l_opy_(
        self,
        f: bstack1lllll1111l_opy_,
        exec: Tuple[bstack1llll111l1l_opy_, str],
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if isinstance(self.bstack1l111lll1ll_opy_, bstack1lll1ll1lll_opy_) and method_name != bstack11111_opy_ (u"࠭ࡣࡰࡰࡱࡩࡨࡺࠧᓎ"):
            return
        if bstack1lll1111l1l_opy_.bstack1llllll1lll_opy_(instance, bstack1l11llll11l_opy_.bstack1l11111l1ll_opy_):
            return
        if f.bstack1llllll11ll_opy_(method_name, *args):
            bstack1l111l111l1_opy_ = False
            desired_capabilities = f.bstack1l1lll11l11_opy_(instance)
            if isinstance(desired_capabilities, dict):
                hub_url = f.bstack1l1ll1l1l1l_opy_(instance)
                platform_index = f.get_state(instance, bstack1lllll1111l_opy_.bstack1lllll1ll11_opy_, 0)
                bstack1l1111l1111_opy_ = datetime.now()
                r = self.bstack1l1111ll1l1_opy_(platform_index, f.framework_name, f.framework_version, hub_url)
                instance.bstack1llll1l111_opy_(bstack11111_opy_ (u"ࠢࡨࡴࡳࡧ࠿ࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡤࡩ࡯࡯ࡨ࡬࡫ࠧᓏ"), datetime.now() - bstack1l1111l1111_opy_)
                bstack1l111l111l1_opy_ = r.success
            else:
                self.logger.error(bstack11111_opy_ (u"ࠣ࡯࡬ࡷࡸ࡯࡮ࡨࠢࡧࡩࡸ࡯ࡲࡦࡦࠣࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴ࠿ࠥᓐ") + str(desired_capabilities) + bstack11111_opy_ (u"ࠤࠥᓑ"))
            f.bstack1lllllll11l_opy_(instance, bstack1l11llll11l_opy_.bstack1l11111l1ll_opy_, bstack1l111l111l1_opy_)
    def bstack1llll1ll11_opy_(self, test_tags):
        bstack1l1111ll1l1_opy_ = self.config.get(bstack11111_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪᓒ"))
        if not bstack1l1111ll1l1_opy_:
            return True
        try:
            include_tags = bstack1l1111ll1l1_opy_[bstack11111_opy_ (u"ࠫ࡮ࡴࡣ࡭ࡷࡧࡩ࡙ࡧࡧࡴࡋࡱࡘࡪࡹࡴࡪࡰࡪࡗࡨࡵࡰࡦࠩᓓ")] if bstack11111_opy_ (u"ࠬ࡯࡮ࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪᓔ") in bstack1l1111ll1l1_opy_ and isinstance(bstack1l1111ll1l1_opy_[bstack11111_opy_ (u"࠭ࡩ࡯ࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫᓕ")], list) else []
            exclude_tags = bstack1l1111ll1l1_opy_[bstack11111_opy_ (u"ࠧࡦࡺࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩࠬᓖ")] if bstack11111_opy_ (u"ࠨࡧࡻࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ࠭ᓗ") in bstack1l1111ll1l1_opy_ and isinstance(bstack1l1111ll1l1_opy_[bstack11111_opy_ (u"ࠩࡨࡼࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧᓘ")], list) else []
            excluded = any(tag in exclude_tags for tag in test_tags)
            included = len(include_tags) == 0 or any(tag in include_tags for tag in test_tags)
            return not excluded and included
        except Exception as error:
            self.logger.debug(bstack11111_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡺ࡬࡮ࡲࡥࠡࡸࡤࡰ࡮ࡪࡡࡵ࡫ࡱ࡫ࠥࡺࡥࡴࡶࠣࡧࡦࡹࡥࠡࡨࡲࡶࠥࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡨࡥࡧࡱࡵࡩࠥࡹࡣࡢࡰࡱ࡭ࡳ࡭࠮ࠡࡇࡵࡶࡴࡸࠠ࠻ࠢࠥᓙ") + str(error))
        return False
    def bstack1111lllll1_opy_(self, caps):
        try:
            if self.bstack1l1111ll11l_opy_:
                bstack1l11111ll1l_opy_ = caps.get(bstack11111_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲࡔࡡ࡮ࡧࠥᓚ"))
                if bstack1l11111ll1l_opy_ is not None and str(bstack1l11111ll1l_opy_).lower() == bstack11111_opy_ (u"ࠧࡧ࡮ࡥࡴࡲ࡭ࡩࠨᓛ"):
                    bstack1l111l11l1l_opy_ = caps.get(bstack11111_opy_ (u"ࠨࡡࡱࡲ࡬ࡹࡲࡀࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠣᓜ")) or caps.get(bstack11111_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠤᓝ"))
                    if bstack1l111l11l1l_opy_ is not None and int(bstack1l111l11l1l_opy_) < 11:
                        self.logger.warning(bstack11111_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡽࡩ࡭࡮ࠣࡶࡺࡴࠠࡰࡰ࡯ࡽࠥࡵ࡮ࠡࡃࡱࡨࡷࡵࡩࡥࠢ࠴࠵ࠥࡧ࡮ࡥࠢࡤࡦࡴࡼࡥ࠯ࠢࡆࡹࡷࡸࡥ࡯ࡶࠣࡴࡱࡧࡴࡧࡱࡵࡱࠥࡼࡥࡳࡵ࡬ࡳࡳࠦ࠽ࠣᓞ") + str(bstack1l111l11l1l_opy_) + bstack11111_opy_ (u"ࠤࠥᓟ"))
                        return False
                return True
            bstack1l111l1ll11_opy_ = caps.get(bstack11111_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫᓠ"), {}).get(bstack11111_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࡒࡦࡳࡥࠨᓡ"), caps.get(bstack11111_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࠬᓢ"), bstack11111_opy_ (u"࠭ࠧᓣ")))
            if bstack1l111l1ll11_opy_:
                self.logger.warning(bstack11111_opy_ (u"ࠢࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡼ࡯࡬࡭ࠢࡵࡹࡳࠦ࡯࡯࡮ࡼࠤࡴࡴࠠࡅࡧࡶ࡯ࡹࡵࡰࠡࡤࡵࡳࡼࡹࡥࡳࡵ࠱ࠦᓤ"))
                return False
            browser = caps.get(bstack11111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭ᓥ"), bstack11111_opy_ (u"ࠩࠪᓦ")).lower()
            if browser != bstack11111_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧࠪᓧ"):
                self.logger.warning(bstack11111_opy_ (u"ࠦࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡹ࡬ࡰࡱࠦࡲࡶࡰࠣࡳࡳࡲࡹࠡࡱࡱࠤࡈ࡮ࡲࡰ࡯ࡨࠤࡧࡸ࡯ࡸࡵࡨࡶࡸ࠴ࠢᓨ"))
                return False
            bstack1l111111l1l_opy_ = bstack1l1111lll11_opy_
            if not self.config.get(bstack11111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠧᓩ")) or self.config.get(bstack11111_opy_ (u"࠭ࡴࡶࡴࡥࡳࡸࡩࡡ࡭ࡧࠪᓪ")):
                bstack1l111111l1l_opy_ = bstack1l1111l1lll_opy_
            browser_version = caps.get(bstack11111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨᓫ"))
            if not browser_version:
                browser_version = caps.get(bstack11111_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩᓬ"), {}).get(bstack11111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪᓭ"), bstack11111_opy_ (u"ࠪࠫᓮ"))
            if browser_version and browser_version != bstack11111_opy_ (u"ࠫࡱࡧࡴࡦࡵࡷࠫᓯ") and int(browser_version.split(bstack11111_opy_ (u"ࠬ࠴ࠧᓰ"))[0]) <= bstack1l111111l1l_opy_:
                self.logger.warning(bstack11111_opy_ (u"ࠨࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡻ࡮ࡲ࡬ࠡࡴࡸࡲࠥࡵ࡮࡭ࡻࠣࡳࡳࠦࡃࡩࡴࡲࡱࡪࠦࡢࡳࡱࡺࡷࡪࡸࠠࡷࡧࡵࡷ࡮ࡵ࡮ࠡࡩࡵࡩࡦࡺࡥࡳࠢࡷ࡬ࡦࡴࠠࠣᓱ") + str(bstack1l111111l1l_opy_) + bstack11111_opy_ (u"ࠢ࠯ࠤᓲ"))
                return False
            bstack1l111l1lll1_opy_ = caps.get(bstack11111_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩᓳ"), {}).get(bstack11111_opy_ (u"ࠩࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩᓴ"))
            if not bstack1l111l1lll1_opy_:
                bstack1l111l1lll1_opy_ = caps.get(bstack11111_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨᓵ"), {})
            if bstack1l111l1lll1_opy_ and bstack11111_opy_ (u"ࠫ࠲࠳ࡨࡦࡣࡧࡰࡪࡹࡳࠨᓶ") in bstack1l111l1lll1_opy_.get(bstack11111_opy_ (u"ࠬࡧࡲࡨࡵࠪᓷ"), []):
                self.logger.warning(bstack11111_opy_ (u"ࠨࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡻ࡮ࡲ࡬ࠡࡰࡲࡸࠥࡸࡵ࡯ࠢࡲࡲࠥࡲࡥࡨࡣࡦࡽࠥ࡮ࡥࡢࡦ࡯ࡩࡸࡹࠠ࡮ࡱࡧࡩ࠳ࠦࡓࡸ࡫ࡷࡧ࡭ࠦࡴࡰࠢࡱࡩࡼࠦࡨࡦࡣࡧࡰࡪࡹࡳࠡ࡯ࡲࡨࡪࠦ࡯ࡳࠢࡤࡺࡴ࡯ࡤࠡࡷࡶ࡭ࡳ࡭ࠠࡩࡧࡤࡨࡱ࡫ࡳࡴࠢࡰࡳࡩ࡫࠮ࠣᓸ"))
                return False
            return True
        except Exception as error:
            self.logger.debug(bstack11111_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡶࡢ࡮࡬ࡨࡦࡺࡥࠡࡣ࠴࠵ࡾࠦࡳࡶࡲࡳࡳࡷࡺࠠ࠻ࠤᓹ") + str(error))
            return False
    def bstack1l11111l1l1_opy_(self, test_uuid: str, result: structs.FetchDriverExecuteParamsEventResponse):
        bstack1l111l1l11l_opy_ = {
            bstack11111_opy_ (u"ࠨࡶ࡫ࡘࡪࡹࡴࡓࡷࡱ࡙ࡺ࡯ࡤࠨᓺ"): test_uuid,
        }
        bstack1l11111lll1_opy_ = {}
        if result.success:
            bstack1l11111lll1_opy_ = json.loads(result.accessibility_execute_params)
        return bstack1l111l1l1l1_opy_(bstack1l111l1l11l_opy_, bstack1l11111lll1_opy_)
    def bstack1l1111l1l1l_opy_(self, script_name: str, test_uuid: str) -> dict:
        bstack11111_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࠣࠤࠥࠦࡆࡦࡶࡦ࡬ࠥࡩࡥ࡯ࡶࡵࡥࡱࠦࡡࡶࡶ࡫ࠤࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡨࡵ࡮ࡧ࡫ࡪࡹࡷࡧࡴࡪࡱࡱࠤ࡫ࡵࡲࠡࡶ࡫ࡩࠥ࡭ࡩࡷࡧࡱࠤࡸࡩࡲࡪࡲࡷࠤࡳࡧ࡭ࡦ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࡗ࡫ࡴࡶࡴࡱࡷࠥࡩࡡࡤࡪࡨࡨࠥࡩ࡯࡯ࡨ࡬࡫ࠥ࡯ࡦࠡࡣ࡯ࡶࡪࡧࡤࡺࠢࡩࡩࡹࡩࡨࡦࡦ࠯ࠤࡴࡺࡨࡦࡴࡺ࡭ࡸ࡫ࠠ࡭ࡱࡤࡨࡸࠦࡡ࡯ࡦࠣࡧࡦࡩࡨࡦࡵࠣ࡭ࡹ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡃࡵ࡫ࡸࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡹࡣࡳ࡫ࡳࡸࡤࡴࡡ࡮ࡧ࠽ࠤࡓࡧ࡭ࡦࠢࡲࡪࠥࡺࡨࡦࠢࡶࡧࡷ࡯ࡰࡵࠢࡷࡳࠥ࡬ࡥࡵࡥ࡫ࠤࡨࡵ࡮ࡧ࡫ࡪࠤ࡫ࡵࡲࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡴࡦࡵࡷࡣࡺࡻࡩࡥ࠼࡙࡚ࠣࡏࡄࠡࡱࡩࠤࡹ࡮ࡥࠡࡶࡨࡷࡹࠦࡲࡶࡰࠣࡪࡴࡸࠠࡸࡪ࡬ࡧ࡭ࠦࡴࡰࠢࡩࡩࡹࡩࡨࠡࡥࡲࡲ࡫࡯ࡧࠋࠢࠣࠤࠥࠦࠠࠡࠢࡕࡩࡹࡻࡲ࡯ࡵ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡧ࡭ࡨࡺ࠺ࠡࡅࡲࡲ࡫࡯ࡧࡶࡴࡤࡸ࡮ࡵ࡮ࠡࡦ࡬ࡧࡹ࡯࡯࡯ࡣࡵࡽ࠱ࠦࡥ࡮ࡲࡷࡽࠥࡪࡩࡤࡶࠣ࡭࡫ࠦࡥࡳࡴࡲࡶࠥࡵࡣࡤࡷࡵࡷࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤᓻ")
        try:
            if self.bstack1l11111ll11_opy_:
                return self.bstack1l1111l11l1_opy_
            self.bstack1llllll11l1_opy_()
            req = structs.FetchDriverExecuteParamsEventRequest()
            req.bin_session_id = self.bin_session_id
            req.product = bstack11111_opy_ (u"ࠥࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠥᓼ")
            req.script_name = script_name
            r = self.bstack1llll1ll1ll_opy_.FetchDriverExecuteParamsEvent(req)
            if r.success:
                self.bstack1l1111l11l1_opy_ = self.bstack1l11111l1l1_opy_(test_uuid, r)
                self.bstack1l11111ll11_opy_ = True
            else:
                self.logger.error(bstack11111_opy_ (u"ࠦ࡫࡫ࡴࡤࡪࡆࡩࡳࡺࡲࡢ࡮ࡄࡹࡹ࡮ࡁ࠲࠳ࡼࡇࡴࡴࡦࡪࡩ࠽ࠤࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡧࡧࡷࡧ࡭ࠦࡤࡳ࡫ࡹࡩࡷࠦࡥࡹࡧࡦࡹࡹ࡫ࠠࡱࡣࡵࡥࡲࡹࠠࡧࡱࡵࠤࢀࡹࡣࡳ࡫ࡳࡸࡤࡴࡡ࡮ࡧࢀ࠾ࠥࠨᓽ") + str(r.error) + bstack11111_opy_ (u"ࠧࠨᓾ"))
                self.bstack1l1111l11l1_opy_ = dict()
            return self.bstack1l1111l11l1_opy_
        except Exception as e:
            self.logger.error(bstack11111_opy_ (u"ࠨࡦࡦࡶࡦ࡬ࡈ࡫࡮ࡵࡴࡤࡰࡆࡻࡴࡩࡃ࠴࠵ࡾࡉ࡯࡯ࡨ࡬࡫࠿ࠦࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡩࡩࡹࡩࡨࠡࡦࡵ࡭ࡻ࡫ࡲࠡࡧࡻࡩࡨࡻࡴࡦࠢࡳࡥࡷࡧ࡭ࡴࠢࡩࡳࡷࠦࡻࡴࡥࡵ࡭ࡵࡺ࡟࡯ࡣࡰࡩࢂࡀࠠࠣᓿ") + str(traceback.format_exc()) + bstack11111_opy_ (u"ࠢࠣᔀ"))
            return dict()
    def bstack1lll1l1ll_opy_(self, driver: object, name: str, framework_name: str, test_uuid: str):
        bstack1ll11llll1l_opy_ = None
        try:
            self.bstack1llllll11l1_opy_()
            req = structs.FetchDriverExecuteParamsEventRequest()
            req.bin_session_id = self.bin_session_id
            req.product = bstack11111_opy_ (u"ࠣࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠣᔁ")
            req.script_name = bstack11111_opy_ (u"ࠤࡶࡥࡻ࡫ࡒࡦࡵࡸࡰࡹࡹࠢᔂ")
            r = self.bstack1llll1ll1ll_opy_.FetchDriverExecuteParamsEvent(req)
            if not r.success:
                self.logger.debug(bstack11111_opy_ (u"ࠥࡶࡪࡩࡥࡪࡸࡨࡨࠥࡪࡲࡪࡸࡨࡶࠥ࡫ࡸࡦࡥࡸࡸࡪࠦࡰࡢࡴࡤࡱࡸࠦࡦࡳࡱࡰࠤࡸ࡫ࡲࡷࡧࡵ࠾ࠥࠨᔃ") + str(r.error) + bstack11111_opy_ (u"ࠦࠧᔄ"))
            else:
                bstack1l111l1l11l_opy_ = self.bstack1l11111l1l1_opy_(test_uuid, r)
                bstack1lll1ll11l1_opy_ = r.script
            self.logger.debug(bstack11111_opy_ (u"ࠬࡖࡥࡳࡨࡲࡶࡲ࡯࡮ࡨࠢࡶࡧࡦࡴࠠࡣࡧࡩࡳࡷ࡫ࠠࡴࡣࡹ࡭ࡳ࡭ࠠࡳࡧࡶࡹࡱࡺࡳࠨᔅ") + str(bstack1l111l1l11l_opy_))
            self.perform_scan(driver, name, framework_name=framework_name)
            if not bstack1lll1ll11l1_opy_:
                self.logger.debug(bstack11111_opy_ (u"ࠨࡰࡦࡴࡩࡳࡷࡳ࡟ࡴࡥࡤࡲ࠿ࠦ࡭ࡪࡵࡶ࡭ࡳ࡭ࠠࠨࡵࡤࡺࡪࡘࡥࡴࡷ࡯ࡸࡸ࠭ࠠࡴࡥࡵ࡭ࡵࡺࠠࡧࡱࡵࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࡂࠨᔆ") + str(framework_name) + bstack11111_opy_ (u"ࠢࠡࠤᔇ"))
                return
            bstack1ll11llll1l_opy_ = bstack1llll1ll1l1_opy_.bstack1ll1111lll1_opy_(EVENTS.bstack1l1111lll1l_opy_.value)
            self.bstack1l1111l1l11_opy_(driver, bstack1lll1ll11l1_opy_, bstack1l111l1l11l_opy_, framework_name)
            self.logger.info(bstack11111_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡶࡨࡷࡹ࡯࡮ࡨࠢࡩࡳࡷࠦࡴࡩ࡫ࡶࠤࡹ࡫ࡳࡵࠢࡦࡥࡸ࡫ࠠࡩࡣࡶࠤࡪࡴࡤࡦࡦ࠱ࠦᔈ"))
            bstack1llll1ll1l1_opy_.end(EVENTS.bstack1l1111lll1l_opy_.value, bstack1ll11llll1l_opy_+bstack11111_opy_ (u"ࠤ࠽ࡷࡹࡧࡲࡵࠤᔉ"), bstack1ll11llll1l_opy_+bstack11111_opy_ (u"ࠥ࠾ࡪࡴࡤࠣᔊ"), True, None, command=bstack11111_opy_ (u"ࠫࡸࡧࡶࡦࡔࡨࡷࡺࡲࡴࡴࠩᔋ"),test_name=name)
        except Exception as bstack1l111l1ll1l_opy_:
            self.logger.error(bstack11111_opy_ (u"ࠧࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡸࡥࡴࡷ࡯ࡸࡸࠦࡣࡰࡷ࡯ࡨࠥࡴ࡯ࡵࠢࡥࡩࠥࡶࡲࡰࡥࡨࡷࡸ࡫ࡤࠡࡨࡲࡶࠥࡺࡨࡦࠢࡷࡩࡸࡺࠠࡤࡣࡶࡩ࠿ࠦࠢᔌ") + bstack11111_opy_ (u"ࠨࡳࡵࡴࠫࡴࡦࡺࡨࠪࠤᔍ") + bstack11111_opy_ (u"ࠢࠡࡇࡵࡶࡴࡸࠠ࠻ࠤᔎ") + str(bstack1l111l1ll1l_opy_))
            bstack1llll1ll1l1_opy_.end(EVENTS.bstack1l1111lll1l_opy_.value, bstack1ll11llll1l_opy_+bstack11111_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣᔏ"), bstack1ll11llll1l_opy_+bstack11111_opy_ (u"ࠤ࠽ࡩࡳࡪࠢᔐ"), False, bstack1l111l1ll1l_opy_, command=bstack11111_opy_ (u"ࠪࡷࡦࡼࡥࡓࡧࡶࡹࡱࡺࡳࠨᔑ"),test_name=name)
    def bstack1l1111l1l11_opy_(self, driver, bstack1lll1ll11l1_opy_, bstack1l111l1l11l_opy_, framework_name):
        if framework_name == bstack11111_opy_ (u"ࠫࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠨᔒ"):
            self.bstack1l111lll1ll_opy_.bstack1lll1l1llll_opy_(driver, bstack1lll1ll11l1_opy_, bstack1l111l1l11l_opy_)
        else:
            self.logger.debug(driver.execute_async_script(bstack1lll1ll11l1_opy_, bstack1l111l1l11l_opy_))
    def _1l111l11lll_opy_(self, instance: bstack1lll1l1ll1l_opy_, args: Tuple) -> list:
        bstack11111_opy_ (u"ࠧࠨࠢࡆࡺࡷࡶࡦࡩࡴࠡࡶࡤ࡫ࡸࠦࡢࡢࡵࡨࡨࠥࡵ࡮ࠡࡶ࡫ࡩࠥࡺࡥࡴࡶࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠴ࠢࠣࠤᔓ")
        if bstack11111_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠪᔔ") in instance.bstack1ll11llllll_opy_:
            return args[2].tags if hasattr(args[2], bstack11111_opy_ (u"ࠧࡵࡣࡪࡷࠬᔕ")) else []
        if hasattr(args[0], bstack11111_opy_ (u"ࠨࡱࡺࡲࡤࡳࡡࡳ࡭ࡨࡶࡸ࠭ᔖ")):
            return [marker.name for marker in args[0].own_markers]
        return []
    def bstack1l111l11111_opy_(self, tags, capabilities):
        return self.bstack1llll1ll11_opy_(tags) and self.bstack1111lllll1_opy_(capabilities)