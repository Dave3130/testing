# coding: UTF-8
import sys
bstack1lll1l_opy_ = sys.version_info [0] == 2
bstack111l11l_opy_ = 2048
bstack1l1llll_opy_ = 7
def bstack111111l_opy_ (bstack1ll1_opy_):
    global bstack11l1ll_opy_
    bstack11ll1l_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack11ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack1lllll1_opy_ = bstack11ll1l_opy_ % len (bstack11ll_opy_)
    bstack111l1l1_opy_ = bstack11ll_opy_ [:bstack1lllll1_opy_] + bstack11ll_opy_ [bstack1lllll1_opy_:]
    if bstack1lll1l_opy_:
        bstack1111_opy_ = unicode () .join ([unichr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    else:
        bstack1111_opy_ = str () .join ([chr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    return eval (bstack1111_opy_)
from _pytest import fixtures
from _pytest.python import _call_with_optional_argument
from pytest import Module, Class
from bstack_utils.helper import Result, bstack11l1ll11l1l_opy_
from browserstack_sdk.bstack11111l11_opy_ import bstack1llll1111_opy_
def _11l1ll11ll1_opy_(method, this, arg):
    arg_count = method.__code__.co_argcount
    if arg_count > 1:
        method(this, arg)
    else:
        method(this)
class bstack11l1ll1l1ll_opy_:
    def __init__(self, handler):
        self._11l1ll1l111_opy_ = {}
        self._11l1l1lllll_opy_ = {}
        self.handler = handler
        self.patch()
        pass
    def patch(self):
        pytest_version = bstack1llll1111_opy_.version()
        if bstack11l1ll11l1l_opy_(pytest_version, bstack111111l_opy_ (u"ࠧ࠾࠮࠲࠰࠴ࠦ᝭")) >= 0:
            self._11l1ll1l111_opy_[bstack111111l_opy_ (u"࠭ࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᝮ")] = Module._register_setup_function_fixture
            self._11l1ll1l111_opy_[bstack111111l_opy_ (u"ࠧ࡮ࡱࡧࡹࡱ࡫࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨᝯ")] = Module._register_setup_module_fixture
            self._11l1ll1l111_opy_[bstack111111l_opy_ (u"ࠨࡥ࡯ࡥࡸࡹ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨᝰ")] = Class._register_setup_class_fixture
            self._11l1ll1l111_opy_[bstack111111l_opy_ (u"ࠩࡰࡩࡹ࡮࡯ࡥࡡࡩ࡭ࡽࡺࡵࡳࡧࠪ᝱")] = Class._register_setup_method_fixture
            Module._register_setup_function_fixture = self.bstack11l1ll11lll_opy_(bstack111111l_opy_ (u"ࠪࡪࡺࡴࡣࡵ࡫ࡲࡲࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ᝲ"))
            Module._register_setup_module_fixture = self.bstack11l1ll11lll_opy_(bstack111111l_opy_ (u"ࠫࡲࡵࡤࡶ࡮ࡨࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᝳ"))
            Class._register_setup_class_fixture = self.bstack11l1ll11lll_opy_(bstack111111l_opy_ (u"ࠬࡩ࡬ࡢࡵࡶࡣ࡫࡯ࡸࡵࡷࡵࡩࠬ᝴"))
            Class._register_setup_method_fixture = self.bstack11l1ll11lll_opy_(bstack111111l_opy_ (u"࠭࡭ࡦࡶ࡫ࡳࡩࡥࡦࡪࡺࡷࡹࡷ࡫ࠧ᝵"))
        else:
            self._11l1ll1l111_opy_[bstack111111l_opy_ (u"ࠧࡧࡷࡱࡧࡹ࡯࡯࡯ࡡࡩ࡭ࡽࡺࡵࡳࡧࠪ᝶")] = Module._inject_setup_function_fixture
            self._11l1ll1l111_opy_[bstack111111l_opy_ (u"ࠨ࡯ࡲࡨࡺࡲࡥࡠࡨ࡬ࡼࡹࡻࡲࡦࠩ᝷")] = Module._inject_setup_module_fixture
            self._11l1ll1l111_opy_[bstack111111l_opy_ (u"ࠩࡦࡰࡦࡹࡳࡠࡨ࡬ࡼࡹࡻࡲࡦࠩ᝸")] = Class._inject_setup_class_fixture
            self._11l1ll1l111_opy_[bstack111111l_opy_ (u"ࠪࡱࡪࡺࡨࡰࡦࡢࡪ࡮ࡾࡴࡶࡴࡨࠫ᝹")] = Class._inject_setup_method_fixture
            Module._inject_setup_function_fixture = self.bstack11l1ll11lll_opy_(bstack111111l_opy_ (u"ࠫ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࡥࡦࡪࡺࡷࡹࡷ࡫ࠧ᝺"))
            Module._inject_setup_module_fixture = self.bstack11l1ll11lll_opy_(bstack111111l_opy_ (u"ࠬࡳ࡯ࡥࡷ࡯ࡩࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭᝻"))
            Class._inject_setup_class_fixture = self.bstack11l1ll11lll_opy_(bstack111111l_opy_ (u"࠭ࡣ࡭ࡣࡶࡷࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭᝼"))
            Class._inject_setup_method_fixture = self.bstack11l1ll11lll_opy_(bstack111111l_opy_ (u"ࠧ࡮ࡧࡷ࡬ࡴࡪ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨ᝽"))
    def bstack11l1ll11111_opy_(self, bstack11l1ll1lll1_opy_, hook_type):
        bstack11l1ll111l1_opy_ = id(bstack11l1ll1lll1_opy_.__class__)
        if (bstack11l1ll111l1_opy_, hook_type) in self._11l1l1lllll_opy_:
            return
        meth = getattr(bstack11l1ll1lll1_opy_, hook_type, None)
        if meth is not None and fixtures.getfixturemarker(meth) is None:
            self._11l1l1lllll_opy_[(bstack11l1ll111l1_opy_, hook_type)] = meth
            setattr(bstack11l1ll1lll1_opy_, hook_type, self.bstack11l1ll111ll_opy_(hook_type, bstack11l1ll111l1_opy_))
    def bstack11l1ll11l11_opy_(self, instance, bstack11l1ll1l1l1_opy_):
        if bstack11l1ll1l1l1_opy_ == bstack111111l_opy_ (u"ࠣࡨࡸࡲࡨࡺࡩࡰࡰࡢࡪ࡮ࡾࡴࡶࡴࡨࠦ᝾"):
            self.bstack11l1ll11111_opy_(instance.obj, bstack111111l_opy_ (u"ࠤࡶࡩࡹࡻࡰࡠࡨࡸࡲࡨࡺࡩࡰࡰࠥ᝿"))
            self.bstack11l1ll11111_opy_(instance.obj, bstack111111l_opy_ (u"ࠥࡸࡪࡧࡲࡥࡱࡺࡲࡤ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠢក"))
        if bstack11l1ll1l1l1_opy_ == bstack111111l_opy_ (u"ࠦࡲࡵࡤࡶ࡮ࡨࡣ࡫࡯ࡸࡵࡷࡵࡩࠧខ"):
            self.bstack11l1ll11111_opy_(instance.obj, bstack111111l_opy_ (u"ࠧࡹࡥࡵࡷࡳࡣࡲࡵࡤࡶ࡮ࡨࠦគ"))
            self.bstack11l1ll11111_opy_(instance.obj, bstack111111l_opy_ (u"ࠨࡴࡦࡣࡵࡨࡴࡽ࡮ࡠ࡯ࡲࡨࡺࡲࡥࠣឃ"))
        if bstack11l1ll1l1l1_opy_ == bstack111111l_opy_ (u"ࠢࡤ࡮ࡤࡷࡸࡥࡦࡪࡺࡷࡹࡷ࡫ࠢង"):
            self.bstack11l1ll11111_opy_(instance.obj, bstack111111l_opy_ (u"ࠣࡵࡨࡸࡺࡶ࡟ࡤ࡮ࡤࡷࡸࠨច"))
            self.bstack11l1ll11111_opy_(instance.obj, bstack111111l_opy_ (u"ࠤࡷࡩࡦࡸࡤࡰࡹࡱࡣࡨࡲࡡࡴࡵࠥឆ"))
        if bstack11l1ll1l1l1_opy_ == bstack111111l_opy_ (u"ࠥࡱࡪࡺࡨࡰࡦࡢࡪ࡮ࡾࡴࡶࡴࡨࠦជ"):
            self.bstack11l1ll11111_opy_(instance.obj, bstack111111l_opy_ (u"ࠦࡸ࡫ࡴࡶࡲࡢࡱࡪࡺࡨࡰࡦࠥឈ"))
            self.bstack11l1ll11111_opy_(instance.obj, bstack111111l_opy_ (u"ࠧࡺࡥࡢࡴࡧࡳࡼࡴ࡟࡮ࡧࡷ࡬ࡴࡪࠢញ"))
    @staticmethod
    def bstack11l1ll1111l_opy_(hook_type, func, args):
        if hook_type in [bstack111111l_opy_ (u"࠭ࡳࡦࡶࡸࡴࡤࡳࡥࡵࡪࡲࡨࠬដ"), bstack111111l_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡰࡩࡹ࡮࡯ࡥࠩឋ")]:
            _11l1ll11ll1_opy_(func, args[0], args[1])
            return
        _call_with_optional_argument(func, args[0])
    def bstack11l1ll111ll_opy_(self, hook_type, bstack11l1ll111l1_opy_):
        def bstack11l1l1llll1_opy_(arg=None):
            self.handler(hook_type, bstack111111l_opy_ (u"ࠨࡤࡨࡪࡴࡸࡥࠨឌ"))
            result = None
            try:
                bstack1l11111ll1l_opy_ = self._11l1l1lllll_opy_[(bstack11l1ll111l1_opy_, hook_type)]
                self.bstack11l1ll1111l_opy_(hook_type, bstack1l11111ll1l_opy_, (arg,))
                result = Result(result=bstack111111l_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩឍ"))
            except Exception as e:
                result = Result(result=bstack111111l_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪណ"), exception=e)
                self.handler(hook_type, bstack111111l_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࠪត"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack111111l_opy_ (u"ࠬࡧࡦࡵࡧࡵࠫថ"), result)
        def bstack11l1ll1ll11_opy_(this, arg=None):
            self.handler(hook_type, bstack111111l_opy_ (u"࠭ࡢࡦࡨࡲࡶࡪ࠭ទ"))
            result = None
            exception = None
            try:
                self.bstack11l1ll1111l_opy_(hook_type, self._11l1l1lllll_opy_[hook_type], (this, arg))
                result = Result(result=bstack111111l_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧធ"))
            except Exception as e:
                result = Result(result=bstack111111l_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨន"), exception=e)
                self.handler(hook_type, bstack111111l_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࠨប"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack111111l_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࠩផ"), result)
        if hook_type in [bstack111111l_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡱࡪࡺࡨࡰࡦࠪព"), bstack111111l_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࡟࡮ࡧࡷ࡬ࡴࡪࠧភ")]:
            return bstack11l1ll1ll11_opy_
        return bstack11l1l1llll1_opy_
    def bstack11l1ll11lll_opy_(self, bstack11l1ll1l1l1_opy_):
        def bstack11l1ll1l11l_opy_(this, *args, **kwargs):
            self.bstack11l1ll11l11_opy_(this, bstack11l1ll1l1l1_opy_)
            self._11l1ll1l111_opy_[bstack11l1ll1l1l1_opy_](this, *args, **kwargs)
        return bstack11l1ll1l11l_opy_